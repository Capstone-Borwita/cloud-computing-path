from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import datetime


class BaseNews(SQLModel):
    title: str = Field()
    content: str = Field()
    image: str = Field()
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, index=True)


class NewsCreate(BaseModel):
    title: str
    content: str
    image: str


class NewsGet(BaseModel):
    id: int
    title: str
    content: str
    image: str
    created_at: Optional[datetime]


class NewsUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None


class News(BaseNews, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
