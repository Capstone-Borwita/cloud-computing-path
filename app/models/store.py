from typing import Optional
from sqlmodel import Field, SQLModel
from fastapi import UploadFile, File
from .user import User


class BaseStore(SQLModel):
    name: str = Field()
    code: str = Field()
    owner_name: str = Field()
    keeper_phone_number: str = Field()
    ktp_photo_path: str = Field()
    keeper_name: str = Field()
    keeper_nik: str = Field()
    keeper_address: str = Field()
    store_photo_path: str = Field()
    longitude: str = Field()
    latitude: str = Field()
    georeverse: str = Field()
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class StoreCreate(BaseStore):
    name: str
    code: str
    owner_name: str
    keeper_phone_number: str
    keeper_nik: str
    keeper_address: str
    longitude: str
    latitude: str
    georeverse: str
    user_id: Optional[int] = None
    ktp_photo: UploadFile = File(...)
    store_photo: UploadFile = File(...)


class StoreUpdate(BaseStore):
    pass


class Store(BaseStore, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
