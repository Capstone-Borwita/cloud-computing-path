from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel

# JWT configurations
SECRET_KEY = "a970cdd10ca22de9ea7981a1929a9c13e6b01dc05fad5c1491e67abe5f83554fac3efa57b1da6b00849909c5e18ed856232ed07b2e5a9b4b5ba962ac640f4c78"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class BaseUser(SQLModel):
    email: str = Field(index=True, unique=True)
    password: str
    name: Optional[str] = None
    token: Optional[str] = None

class UserCreate(BaseModel):
    email: str
    password: str
    password_confirmation: str 
    name: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(SQLModel):
    email: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    token: Optional[str] = None

class User(BaseUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
