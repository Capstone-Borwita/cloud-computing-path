import os
import jwt
from typing import List, Sequence
from app.core.config import Settings
from fastapi import APIRouter, HTTPException, status, Depends, UploadFile, File, Depends, Form
from pathlib import Path
from uuid import uuid4
from sqlmodel import select, Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
from pathlib import Path
from app.database import SessionDep
from app.models.user import User, UserCreate, UserUpdate
from app.schemas.response_schema import (
    SuccessIdResponse,
    SuccessResponse,
    SuccessDataResponse,
)
from app.schemas.model_schema import ModelId
from passlib.context import CryptContext
from app.utils.utils import get_current_user
from typing import Optional
from app.utils.utils import create_access_token



settings = Settings()
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

UPLOAD_DIR = Path("uploads/user-image")
DEFAULT_IMAGE_PATH = UPLOAD_DIR / "default.png"

router = APIRouter()

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def user_not_found():
    return HTTPException(status_code=404, detail="User not found")


@router.get("/all", response_model=SuccessDataResponse[Sequence[User]])
def list_users(session: SessionDep, skip: int = 0, limit: int = 10) -> SuccessDataResponse[List[User]]:
    users = session.exec(select(User).offset(skip).limit(limit)).all()
    return SuccessDataResponse(data=users)


@router.get("/", response_model=SuccessDataResponse[User])
def get_current_user_data(session: SessionDep, current_user: User = Depends(get_current_user)) -> SuccessDataResponse[User]:
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
    image: UploadFile = File(None) 
) -> SuccessResponse:
    user = session.get(User, current_user.id)
    if not user:
        raise user_not_found()

    if new_password:
        if not current_password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Current password is required to update password"
            )

        if not pwd_context.verify(current_password, user.password):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Current password is incorrect"
            )

        if new_password != password_confirmation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New password and password confirmation do not match"
            )

        user.password = pwd_context.hash(new_password)

    if email:
        user.email = email
    if name:
        user.name = name

    if image:
        image_extension = image.filename.split(".")[-1]
        new_image_filename = f"{uuid4()}.{image_extension}"
        new_image_path = UPLOAD_DIR / new_image_filename

        with open(new_image_path, "wb") as buffer:
            buffer.write(await image.read())

        if user.image_path != str(DEFAULT_IMAGE_PATH) and os.path.exists(user.image_path):
            os.remove(user.image_path)

        user.image_path = str(new_image_path)

    session.add(user)
    session.commit()
    session.refresh(user)

    new_token = create_access_token(data={"sub": user.email})

    return SuccessResponse(message="User updated successfully", token=new_token)

@router.delete("/{id}", response_model=SuccessResponse)
def delete_user(id: int, session: SessionDep) -> SuccessResponse:
    user = session.get(User, id)
    
    if user is None:
        raise user_not_found()

    session.delete(user)
    session.commit()

    return SuccessResponse()


