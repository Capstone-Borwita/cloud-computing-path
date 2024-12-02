import random
import string
from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
)
from pathlib import Path
from app.models.user import User
from app.schemas.model_schema import KTP_OCR_Result
from app.schemas.response_schema import SuccessDataResponse
from app.utils.utils import get_current_user
from app.utils.images.ocr import (
    OCR_IMAGE_PATH,
    OCR_SEGMENTATION_IMAGE_PATH,
    OCR_CROPPED_IMAGE_PATH,
)
from app.utils.response import invalid_request_response
from app.lang.id import indonesia_fields
from modules.ml.api import ktp_ocr

router = APIRouter()

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/jpg"}


def generate_random_string(length: int) -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_random_filename(original_filename: str) -> str:
    file_extension = Path(original_filename).suffix

    return generate_random_string() + file_extension


@router.post("/ktp")
def ocr_ktp(
    ktp_photo: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
) -> SuccessDataResponse[KTP_OCR_Result]:
    if ktp_photo.content_type not in ALLOWED_IMAGE_TYPES:
        return invalid_request_response(
            f"Kolom {indonesia_fields['ktp_photo']} tidak valid. Hanya boleh JPEG atau PNG"
        )

    id = generate_random_string(length=16)

    ktp_photo_filename = id + Path(ktp_photo.filename).suffix
    ktp_photo_prefix = current_user.id

    ktp_photo_path = OCR_IMAGE_PATH / f"{ktp_photo_prefix}_ktp_{ktp_photo_filename}"

    with open(ktp_photo_path, "wb") as f:
        f.write(ktp_photo.file.read())

    segmentation_path = OCR_SEGMENTATION_IMAGE_PATH / id
    cropped_path = OCR_CROPPED_IMAGE_PATH / id

    segmentation_path.mkdir()
    cropped_path.mkdir()

    result = ktp_ocr(
        ktp_photo_path.absolute().as_posix(),
        segmentation_path.absolute().as_posix(),
        cropped_path.absolute().as_posix(),
    )

    if result is None:
        return invalid_request_response("KTP gagal dibaca")

    if type(result) is str:
        return invalid_request_response(result)

    return SuccessDataResponse(
        data=KTP_OCR_Result(
            identifier=ktp_photo_filename,
            nik=result["NIK"],
            name=result["Nama"],
            address=result["Alamat"],
        )
    )
