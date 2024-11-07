from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class BaseStore(SQLModel):
    name: str = Field()


class StoreCreate(BaseStore):
    pass


class StoreUpdate(BaseStore):
    pass


class Store(BaseStore, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    submitted_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )
