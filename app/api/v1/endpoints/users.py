import os
from typing import List, Sequence, Optional
from uuid import uuid4
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
    UploadFile,
    File,
    Depends,
    Form,
)
from sqlmodel import select
from passlib.context import CryptContext
from app.database import SessionDep
from app.models.user import User
from app.utils.utils import get_current_user, create_access_token
from app.utils.images.avatar import USER_AVATAR_PATH, default_user_images
from app.schemas.response_schema import (
    SuccessResponse,
    SuccessDataResponse,
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


def user_not_found():
    return HTTPException(status_code=404, detail="User not found")


@router.get("/all", response_model=SuccessDataResponse[Sequence[User]])
def list_users(
    session: SessionDep, skip: int = 0, limit: int = 10
) -> SuccessDataResponse[List[User]]:
    users = session.exec(select(User).offset(skip).limit(limit)).all()
    return SuccessDataResponse(data=users)


@router.get("/", response_model=SuccessDataResponse[User])
def get_current_user_data(
    current_user: User = Depends(get_current_user),
) -> SuccessDataResponse[User]:
    return SuccessDataResponse(data=current_user)


@router.put("/", response_model=SuccessResponse)
async def update_user(
    session: SessionDep,
    current_user: User = Depends(get_current_user),
    current_password: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    new_password: Optional[str] = Form(None),
    password_confirmation: Optional[str] = Form(None),
    name: Optional[str] = Form(None),
    image: UploadFile = File(None),
) -> SuccessResponse:
    user = session.get(User, current_user.id)
    if not user:
        raise user_not_found()

    new_token = None

    if new_password:
        if not current_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Current password is required to update password",
            )

        if not pwd_context.verify(current_password, user.password):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Current password is incorrect",
            )

        if new_password != password_confirmation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New password and password confirmation do not match",
            )

        user.password = pwd_context.hash(new_password)
        new_token = create_access_token()

    if email:
        user.email = email
    if name:
        user.name = name

    if image:
        image_extension = image.filename.split(".")[-1]
        new_image_filename = f"{uuid4()}.{image_extension}"
        new_image_path = USER_AVATAR_PATH / new_image_filename

        with open(new_image_path, "wb") as buffer:
            buffer.write(await image.read())

        if user.image_path not in default_user_images and os.path.exists(
            user.image_path
        ):
            os.remove(user.image_path)

        user.image_path = str(new_image_path)

    session.add(user)
    session.commit()
    session.refresh(user)

    return SuccessResponse(message="User updated successfully", token=new_token)


@router.delete("/{id}", response_model=SuccessResponse)
def delete_user(id: int, session: SessionDep) -> SuccessResponse:
    user = session.get(User, id)

    if user is None:
        raise user_not_found()

    session.delete(user)
    session.commit()

    return SuccessResponse()
