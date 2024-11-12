from typing import List, Sequence
from pathlib import Path
from app.core.config import Settings
from fastapi import APIRouter, HTTPException, status, Depends, File, UploadFile, Form
from sqlmodel import select, Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
from app.database import SessionDep
from app.models.user import User, UserCreate, UserUpdate, UserLogin
from app.schemas.response_schema import (
    SuccessIdResponse,
    SuccessResponse,
    SuccessResponseLogin,
    SuccessDataResponse,
    UserLoginResponse,
)
from app.schemas.model_schema import ModelId
from passlib.context import CryptContext
from app.utils.utils import create_access_token
from uuid import uuid4
import jwt
import shutil

settings = Settings()
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

UPLOAD_DIR = Path("uploads/user-image")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
DEFAULT_IMAGE_PATH = UPLOAD_DIR / "default.png"

def user_not_found():
    return HTTPException(status_code=404, detail="User not found")

@router.post("/login", response_model=SuccessResponseLogin)
def login_user(session: SessionDep, user_in: UserLogin) -> SuccessResponseLogin:
    user = session.exec(select(User).filter(User.email == user_in.email)).first()

    if not user or not pwd_context.verify(user_in.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(data={"sub": user.email})
    
    user_response = UserLoginResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        token=access_token
    )

    return SuccessResponseLogin(data=user_response)

@router.post("/register", response_model=SuccessIdResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    session: SessionDep, 
    email: str = Form(...),
    password: str = Form(...),
    password_confirmation: str = Form(...),
    name: str = Form(...),
    image: UploadFile = File(None)
) -> SuccessIdResponse:
    if password != password_confirmation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password and password confirmation do not match"
        )

    hashed_password = pwd_context.hash(password)

    if image:
        image_extension = image.filename.split(".")[-1]
        image_filename = f"{uuid4()}.{image_extension}"
        image_path = UPLOAD_DIR / image_filename

        with open(image_path, "wb") as buffer:
            buffer.write(await image.read())
    else:
        image_filename = f"{uuid4()}.png"
        image_path = UPLOAD_DIR / image_filename
        shutil.copy(DEFAULT_IMAGE_PATH, image_path)

    user = User(
        email=email, 
        password=hashed_password, 
        name=name, 
        image_path=str(image_path),
        token=""
    )

    try:
        session.add(user)
        session.commit()
        session.refresh(user)
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )

    access_token = create_access_token(data={"sub": user.email})

    return SuccessIdResponse(data={"id": user.id, "token": access_token})