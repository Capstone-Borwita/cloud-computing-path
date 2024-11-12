from typing import List, Sequence
from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import select, Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
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
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "a970cdd10ca22de9ea7981a1929a9c13e6b01dc05fad5c1491e67abe5f83554fac3efa57b1da6b00849909c5e18ed856232ed07b2e5a9b4b5ba962ac640f4c78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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

# @router.get("/{id}", response_model=SuccessDataResponse[User])
# def get_user(id: int, session: SessionDep) -> SuccessDataResponse[User]:
#     user = session.get(User, id)
#     if not user:
#         raise user_not_found()
#     return SuccessDataResponse(data=user)

@router.get("/", response_model=SuccessDataResponse[User])
def get_current_user_data(session: SessionDep, current_user: User = Depends(get_current_user)) -> SuccessDataResponse[User]:
    # The `current_user` is automatically populated using the JWT token
    return SuccessDataResponse(data=current_user)


# @router.put("/{id}", response_model=SuccessResponse)
# def update_user(id: int, user_in: UserUpdate, session: SessionDep, current_user: User = Depends(get_current_user) ) -> SuccessResponse:
#     user = session.get(User, id)
#     if not user:
#         raise user_not_found()

#     if user.email != current_user.email:
#         raise HTTPException(status_code=403, detail="You do not have permission to update this user")

#     user_data = user_in.dict(exclude_unset=True)
#     for key, value in user_data.items():
#         setattr(user, key, value)

#     session.add(user)
#     session.commit()
#     session.refresh(user)

#     return SuccessResponse()

@router.put("/", response_model=SuccessResponse)
def update_user( user_in: UserUpdate, session: SessionDep, current_user: User = Depends(get_current_user)) -> SuccessResponse:
    user = session.get(User, current_user.id) 
    if not user:
        raise user_not_found()

    user_data = user_in.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)

    return SuccessResponse()

@router.delete("/{id}", response_model=SuccessResponse)
def delete_user(id: int, session: SessionDep) -> SuccessResponse:
    user = session.get(User, id)
    
    if user is None:
        raise user_not_found()

    session.delete(user)
    session.commit()

    return SuccessResponse()


