from typing import List, Sequence
from fastapi import APIRouter, HTTPException, status, Depends
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
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "a970cdd10ca22de9ea7981a1929a9c13e6b01dc05fad5c1491e67abe5f83554fac3efa57b1da6b00849909c5e18ed856232ed07b2e5a9b4b5ba962ac640f4c78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

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
    user.token = access_token
    session.add(user)
    session.commit()
    session.refresh(user)
    
    user_response = UserLoginResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        token=user.token
    )

    return SuccessResponseLogin(data=user_response)



@router.post("/register", response_model=SuccessIdResponse, status_code=status.HTTP_201_CREATED)
def register_user(session: SessionDep, user_in: UserCreate) -> SuccessIdResponse:
    if user_in.password != user_in.password_confirmation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password and password confirmation do not match"
        )

    hashed_password = pwd_context.hash(user_in.password)
    user = User(email=user_in.email, password=hashed_password, name=user_in.name)

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
    user.token = access_token
    session.add(user)
    session.commit()
    session.refresh(user)

    return SuccessIdResponse(data={"id": user.id, "token": user.token})

