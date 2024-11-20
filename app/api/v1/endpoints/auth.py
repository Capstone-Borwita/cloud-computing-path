import os
from uuid import uuid4
from passlib.context import CryptContext
from fastapi import APIRouter, HTTPException, status, File, UploadFile, Form, Depends
from pydantic import EmailStr
from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from app.database import SessionDep
from app.models.user import User, UserGet
from app.schemas.response_schema import (
    CredentialResponse,
    SuccessResponse,
    SuccessDataResponse,
)
from app.schemas.model_schema import Credential
from app.utils.utils import get_current_user, create_access_token
from app.utils.images.avatar import (
    USER_AVATAR_PATH,
    random_user_avatar,
    default_user_avatars,
)
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


@router.post("/login")
def login_user(
    session: SessionDep,
    email: EmailStr = Form(...),
    password: str = Form(..., min_length=8),
) -> CredentialResponse:
    user = session.exec(select(User).filter(User.email == email)).first()

    if user and pwd_context.verify(password, user.password):
        return CredentialResponse(data=Credential(token=user.token))

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
    )


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    session: SessionDep,
    email: EmailStr = Form(...),
    password: str = Form(..., min_length=8),
    name: str = Form(..., min_length=1),
    avatar: UploadFile = File(None),
) -> CredentialResponse:
    hashed_password = pwd_context.hash(password)

    if avatar:
        avatar_extension = avatar.filename.split(".")[-1]
        avatar_filename = f"{uuid4()}.{avatar_extension}"
        avatar_path = USER_AVATAR_PATH / avatar_filename

        with open(avatar_path, "wb") as buffer:
            buffer.write(await avatar.read())
    else:
        avatar_path = random_user_avatar()

    user = User(
        email=email,
        password=hashed_password,
        name=name,
        avatar_path=str(avatar_path),
        token=create_access_token(),
    )

    try:
        session.add(user)
        session.commit()
        session.refresh(user)
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered."
        )

    return CredentialResponse(data=Credential(token=user.token))


@router.put("/edit-profile")
def edit_profile(
    session: SessionDep,
    name: str = Form(None, min_length=1),
    email: EmailStr = Form(None),
    current_user: User = Depends(get_current_user),
) -> SuccessResponse:
    if name:
        current_user.name = name

    if email:
        current_user.email = email

    session.commit()
    session.refresh(current_user)

    return SuccessResponse()


@router.put("/edit-photo-profile")
async def edit_photo_profile(
    session: SessionDep,
    avatar: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
) -> SuccessResponse:
    if current_user.avatar_path not in default_user_avatars and os.path.exists(
        current_user.avatar_path
    ):
        os.remove(current_user.avatar_path)

    avatar_extension = avatar.filename.split(".")[-1]
    avatar_filename = f"{uuid4()}.{avatar_extension}"
    avatar_path = USER_AVATAR_PATH / avatar_filename

    with open(avatar_path, "wb") as buffer:
        buffer.write(await avatar.read())

    current_user.avatar_path = str(avatar_path)

    session.commit()
    session.refresh(current_user)

    return SuccessResponse()


@router.put("/edit-password")
def edit_password(
    session: SessionDep,
    old_password: str = Form(..., min_length=8),
    new_password: str = Form(..., min_length=8),
    current_user: User = Depends(get_current_user),
) -> CredentialResponse:
    if not pwd_context.verify(old_password, current_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="These credentials do not match our records.",
        )

    current_user.password = pwd_context.hash(new_password)
    current_user.token = create_access_token()

    session.commit()
    session.refresh(current_user)

    return CredentialResponse(data=Credential(token=current_user.token))


@router.get("/profile")
def profile(
    current_user: User = Depends(get_current_user),
) -> SuccessDataResponse[UserGet]:
    return SuccessDataResponse(
        data=UserGet(
            email=current_user.email,
            name=current_user.name,
            avatar_path=settings.ORIGIN + current_user.avatar_path,
        )
    )
