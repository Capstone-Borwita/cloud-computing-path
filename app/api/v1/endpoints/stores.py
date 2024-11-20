import random
import string
import os
from datetime import datetime
from typing import List
from fastapi import (
    APIRouter,
    status,
    HTTPException,
    Depends,
    UploadFile,
    File,
    Form,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic_extra_types.coordinate import Longitude, Latitude
from sqlmodel import select
from pathlib import Path
from app.database import SessionDep
from app.models.user import User
from app.models.store import Store
from app.schemas.model_schema import ModelId
from app.schemas.response_schema import (
    SuccessIdResponse,
    SuccessDataResponse,
    SuccessResponse,
    InvalidRequestResponse,
)
from app.utils.utils import get_current_user
from app.utils.images.ktp import KTP_IMAGE_PATH
from app.utils.images.store import STORE_IMAGE_PATH
from app.lang.id import indonesia_fields

router = APIRouter()

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/jpg"}


def generate_random_filename(keeper_nik: int, original_filename: str) -> str:
    random_string = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    file_extension = Path(original_filename).suffix
    return f"{keeper_nik}_{random_string}{file_extension}"


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_store(
    session: SessionDep,
    name: str = Form(..., min_length=1),
    owner_name: str = Form(..., min_length=1),
    keeper_phone_number: str = Form(..., regex=r"^0\d{6,15}$"),
    keeper_nik: str = Form(
        ..., regex=r"^\d{6}(?:0[1-9]|[1-2][0-9]|3[0-1])(?:0[1-9]|1[0-2])\d{5}[1-9]$"
    ),
    keeper_name: str = Form(..., min_length=1),
    keeper_address: str = Form(..., min_length=1),
    longitude: Longitude = Form(...),
    latitude: Latitude = Form(...),
    georeverse: str = Form(..., min_length=1),
    ktp_photo: UploadFile = File(...),
    store_photo: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
) -> SuccessIdResponse:
    user_id = current_user.id

    if ktp_photo.content_type not in ALLOWED_IMAGE_TYPES:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                InvalidRequestResponse(
                    message=f"Kolom {indonesia_fields['ktp_photo']} tidak valid. Hanya boleh JPEG atau PNG"
                )
            ),
        )
    if store_photo.content_type not in ALLOWED_IMAGE_TYPES:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                InvalidRequestResponse(
                    message=f"Kolom {indonesia_fields['store_photo']} tidak valid. Hanya boleh JPEG atau PNG"
                )
            ),
        )

    ktp_photo_filename = generate_random_filename(keeper_nik, ktp_photo.filename)
    store_photo_filename = generate_random_filename(keeper_nik, store_photo.filename)

    ktp_photo_path = KTP_IMAGE_PATH / ktp_photo_filename
    store_photo_path = STORE_IMAGE_PATH / store_photo_filename

    with open(ktp_photo_path, "wb") as f:
        f.write(ktp_photo.file.read())
    with open(store_photo_path, "wb") as f:
        f.write(store_photo.file.read())

    date_str = datetime.now().strftime("%d/%m/%Y")
    suffix = "".join(random.choices(string.ascii_uppercase, k=3))
    store_code = f"{date_str}{suffix}"

    store = Store(
        name=name,
        code=store_code,
        owner_name=owner_name,
        keeper_phone_number=keeper_phone_number,
        keeper_nik=keeper_nik,
        keeper_name=keeper_name,
        keeper_address=keeper_address,
        longitude=longitude,
        latitude=latitude,
        georeverse=georeverse,
        ktp_photo_path=str(ktp_photo_path),
        store_photo_path=str(store_photo_path),
        user_id=user_id,
    )

    session.add(store)
    session.commit()
    session.refresh(store)

    return SuccessIdResponse(data=ModelId(id=store.id))


@router.put("/{store_id}", status_code=status.HTTP_200_OK)
def update_store(
    store_id: int,
    session: SessionDep,
    name: str = Form(None, min_length=1),
    owner_name: str = Form(None, min_length=1),
    keeper_phone_number: str = Form(None, regex=r"^0\d{6,15}$"),
    keeper_nik: str = Form(
        None, regex=r"^\d{6}(?:0[1-9]|[1-2][0-9]|3[0-1])(?:0[1-9]|1[0-2])\d{5}[1-9]$"
    ),
    keeper_name: str = Form(None, min_length=1),
    keeper_address: str = Form(None, min_length=1),
    longitude: Longitude = Form(None),
    latitude: Latitude = Form(None),
    georeverse: str = Form(None, min_length=1),
    ktp_photo: UploadFile = File(None),
    store_photo: UploadFile = File(None),
    current_user: User = Depends(get_current_user),
) -> SuccessIdResponse:
    store = session.exec(
        select(Store).where(Store.id == store_id).where(User.id == current_user.id)
    ).first()
    if not store:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Store not found."
        )

    if name:
        store.name = name
    if owner_name:
        store.owner_name = owner_name
    if keeper_phone_number:
        store.keeper_phone_number = keeper_phone_number
    if keeper_nik:
        store.keeper_nik = keeper_nik
    if keeper_name:
        store.keeper_name = keeper_name
    if keeper_address:
        store.keeper_address = keeper_address
    if longitude:
        store.longitude = longitude
    if latitude:
        store.latitude = latitude
    if georeverse:
        store.georeverse = georeverse

    if ktp_photo:
        if ktp_photo.content_type not in ALLOWED_IMAGE_TYPES:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content=jsonable_encoder(
                    InvalidRequestResponse(
                        message=f"Kolom {indonesia_fields['ktp_photo']} tidak valid. Hanya boleh JPEG atau PNG"
                    )
                ),
            )

        if store.ktp_photo_path and os.path.exists(store.ktp_photo_path):
            os.remove(store.ktp_photo_path)

        random_suffix = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        ktp_photo_extension = ktp_photo.filename.split(".")[-1]
        ktp_photo_filename = f"{store.keeper_nik}_{random_suffix}.{ktp_photo_extension}"
        ktp_photo_path = KTP_IMAGE_PATH / ktp_photo_filename

        with open(ktp_photo_path, "wb") as f:
            f.write(ktp_photo.file.read())
        store.ktp_photo_path = str(ktp_photo_path)

    if store_photo:
        if store_photo.content_type not in ALLOWED_IMAGE_TYPES:
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content=jsonable_encoder(
                    InvalidRequestResponse(
                        message=f"Kolom {indonesia_fields['store_photo']} tidak valid. Hanya boleh JPEG atau PNG"
                    )
                ),
            )

        if store.store_photo_path and os.path.exists(store.store_photo_path):
            os.remove(store.store_photo_path)

        random_suffix = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=6)
        )
        store_photo_extension = store_photo.filename.split(".")[-1]
        store_photo_filename = (
            f"{store.keeper_nik}_{random_suffix}.{store_photo_extension}"
        )
        store_photo_path = STORE_IMAGE_PATH / store_photo_filename

        with open(store_photo_path, "wb") as f:
            f.write(store_photo.file.read())
        store.store_photo_path = str(store_photo_path)

    session.commit()
    session.refresh(store)

    return SuccessIdResponse(data=ModelId(id=store.id))


@router.get("/", response_model=SuccessDataResponse[List[Store]], status_code=200)
def get_all_stores(
    session: SessionDep, current_user: User = Depends(get_current_user)
) -> SuccessDataResponse[List[Store]]:
    stores = session.exec(select(Store).where(User.id == current_user.id)).all()

    return SuccessDataResponse(data=stores)


@router.get("/{store_id}", response_model=SuccessDataResponse[Store], status_code=200)
def get_store_by_id(
    store_id: int, session: SessionDep, current_user: User = Depends(get_current_user)
) -> SuccessDataResponse[Store]:
    store = session.exec(
        select(Store).where(Store.id == store_id).where(User.id == current_user.id)
    ).first()

    if not store:
        raise HTTPException(status_code=404, detail="Store not found.")

    return SuccessDataResponse(data=store)


@router.get("/", response_model=SuccessDataResponse)
def get_store_by_user_token(
    session: SessionDep,
    current_user: User = Depends(get_current_user),
) -> SuccessDataResponse:
    stores = session.exec(select(Store).where(Store.user_id == current_user.id)).all()

    return SuccessDataResponse(data=stores)


@router.delete("/{store_id}")
def delete_store(
    store_id: int,
    session: SessionDep,
    current_user: User = Depends(get_current_user),
) -> SuccessResponse:
    store = session.exec(
        select(Store)
        .where(Store.id == store_id)
        .where(Store.user_id == current_user.id)
    ).first()

    if not store:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Store not found."
        )

    if store.ktp_photo_path and os.path.exists(store.ktp_photo_path):
        os.remove(store.ktp_photo_path)

    if store.store_photo_path and os.path.exists(store.store_photo_path):
        os.remove(store.store_photo_path)

    session.delete(store)
    session.commit()

    return SuccessResponse()
