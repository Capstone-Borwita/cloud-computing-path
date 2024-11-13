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
from sqlmodel import select
from pathlib import Path
from app.database import SessionDep
from app.models.store import Store
from app.schemas.model_schema import ModelId
from app.schemas.response_schema import (
    SuccessIdResponse,
    SuccessDataResponse,
    SuccessResponse,
)
from app.utils.utils import get_current_user
from app.utils.images.ktp import KTP_IMAGE_PATH
from app.utils.images.store import STORE_IMAGE_PATH

router = APIRouter()

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/jpg"}


def generate_random_filename(keeper_nik: int, original_filename: str) -> str:
    random_string = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    file_extension = Path(original_filename).suffix
    return f"{keeper_nik}_{random_string}{file_extension}"


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_store(
    session: SessionDep,
    name: str = Form(...),
    owner_name: str = Form(...),
    keeper_phone_number: str = Form(...),
    keeper_nik: str = Form(...),
    keeper_name: str = Form(...),
    keeper_address: str = Form(...),
    longitude: str = Form(...),
    latitude: str = Form(...),
    georeverse: str = Form(...),
    ktp_photo: UploadFile = File(...),
    store_photo: UploadFile = File(...),
    current_user: dict = Depends(get_current_user),
) -> SuccessIdResponse:
    user_id = current_user.id

    required_fields = [
        name,
        owner_name,
        keeper_phone_number,
        keeper_nik,
        keeper_address,
        longitude,
        latitude,
        georeverse,
    ]
    for field, field_name in zip(
        required_fields,
        [
            "name",
            "owner_name",
            "keeper_phone_number",
            "keeper_nik",
            "keeper_name",
            "keeper_address",
            "longitude",
            "latitude",
            "georeverse",
        ],
    ):
        if field is None or field == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Field '{field_name}' is required.",
            )

    if not ktp_photo or not store_photo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both 'ktp_photo' and 'store_photo' are required.",
        )

    if ktp_photo.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type for 'ktp_photo'. Only JPEG and PNG images are allowed.",
        )
    if store_photo.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type for 'store_photo'. Only JPEG and PNG images are allowed.",
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
    name: str = Form(None),
    owner_name: str = Form(None),
    keeper_phone_number: str = Form(None),
    keeper_nik: str = Form(None),
    keeper_name: str = Form(None),
    keeper_address: str = Form(None),
    longitude: str = Form(None),
    latitude: str = Form(None),
    georeverse: str = Form(None),
    ktp_photo: UploadFile = File(None),
    store_photo: UploadFile = File(None),
    current_user: dict = Depends(get_current_user),
) -> SuccessIdResponse:
    user_id = current_user.id

    store = session.exec(select(Store).where(Store.id == store_id)).first()
    if not store:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Store not found."
        )

    if store.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this store.",
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
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file type for 'ktp_photo'. Only JPEG and PNG images are allowed.",
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
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file type for 'store_photo'. Only JPEG and PNG images are allowed.",
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
def get_all_stores(session: SessionDep) -> SuccessDataResponse[List[Store]]:
    stores = session.exec(select(Store)).all()
    if not stores:
        raise HTTPException(status_code=404, detail="No stores found.")
    return SuccessDataResponse(data=stores)


@router.get("/{store_id}", response_model=SuccessDataResponse[Store], status_code=200)
def get_store_by_id(store_id: int, session: SessionDep) -> SuccessDataResponse[Store]:
    store = session.get(Store, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found.")
    return SuccessDataResponse(data=store)


@router.get("/", response_model=SuccessDataResponse)
def get_store_by_user_token(
    session: SessionDep,
    current_user: dict = Depends(get_current_user),
) -> SuccessDataResponse:
    user_id = current_user.id

    print(f"User ID from token: {user_id}")

    stores = session.exec(select(Store).where(Store.user_id == user_id)).all()

    if not stores:
        print(f"No stores found for user ID: {user_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No stores found for the user.",
        )

    return SuccessDataResponse(data=stores)


@router.delete("/{store_id}")
def delete_store(store_id: int, session: SessionDep) -> SuccessResponse:
    store = session.exec(select(Store).where(Store.id == store_id)).first()

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
