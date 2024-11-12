from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class BaseUser(SQLModel):
    email: str = Field(index=True, unique=True)
    password: str = Field()
    name: str = Field()
    token: str = Field()
    image_path: str = Field()


class UserCreate(BaseModel):
    email: str
    password: str
    password_confirmation: str 
    name: str


class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(SQLModel):
    pass


class User(BaseUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)