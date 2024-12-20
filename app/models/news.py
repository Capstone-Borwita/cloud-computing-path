from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel
from datetime import datetime


class BaseNews(SQLModel):
    title: str = Field()
    content: str = Field()
    poster: str = Field()
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    updated_at: Optional[datetime] = Field(
        default=None, sa_column_kwargs={"onupdate": datetime.utcnow}
    )


class NewsCreate(BaseModel):
    title: str
    content: str
    poster: str
    author_id: int


class NewsUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    poster: Optional[str] = None


class News(BaseNews, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional["User"] = Relationship(back_populates="news")
