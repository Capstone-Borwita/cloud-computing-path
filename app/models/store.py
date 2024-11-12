from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class BaseStore(SQLModel):
    name: str = Field()
    owner_name: str = Field()
    keeper_phone_number: str = Field()
    ktp_photo_path: str = Field()
    keeper_nik: int = Field()
    keeper_address: str = Field()
    store_photo_path: str = Field()
    longitude: str = Field()
    latitude: str = Field()
    georeverse: str = Field()
    users_id: Optional[int] = Field(default=None, foreign_key="users.id")


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
