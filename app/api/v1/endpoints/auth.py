from uuid import uuid4
from passlib.context import CryptContext
from fastapi import APIRouter, HTTPException, status, File, UploadFile, Form
from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from app.database import SessionDep
from app.models.user import User, UserLogin
from app.schemas.response_schema import CredentialResponse
from app.schemas.model_schema import Credential
from app.utils.utils import create_access_token
from app.utils.images.avatar import USER_AVATAR_PATH, random_user_avatar

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


@router.post("/login")
def login_user(session: SessionDep, user_in: UserLogin) -> CredentialResponse:
    user = session.exec(select(User).filter(User.email == user_in.email)).first()

    if user and pwd_context.verify(user_in.password, user.password):
        return CredentialResponse(data=Credential(id=user.id, token=user.token))

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
    )


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    session: SessionDep,
    email: str = Form(...),
    password: str = Form(...),
    name: str = Form(...),
    image: UploadFile = File(None),
) -> CredentialResponse:
    hashed_password = pwd_context.hash(password)

    if image:
        image_extension = image.filename.split(".")[-1]
        image_filename = f"{uuid4()}.{image_extension}"
        image_path = USER_AVATAR_PATH / image_filename

        with open(image_path, "wb") as buffer:
            buffer.write(await image.read())
    else:
        image_path = random_user_avatar()

    user = User(
        email=email,
        password=hashed_password,
        name=name,
        image_path=str(image_path),
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

    return CredentialResponse(data=Credential(id=user.id, token=user.token))
