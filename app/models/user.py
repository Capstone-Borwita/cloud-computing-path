from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from datetime import datetime

class BaseUser(SQLModel):
    email: str = Field(index=True, unique=True)
    password: str = Field()
    name: str = Field()
    token: str = Field()
    avatar_path: str = Field()

class UserCreate(BaseModel):
    email: str
    password: str
    password_confirmation: str
    name: str

class UserGet(BaseModel):
    email: str
    name: str
    avatar_path: str

class UserUpdate(SQLModel):
    pass

class User(BaseUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    news: list["News"] = Relationship(back_populates="user") 
