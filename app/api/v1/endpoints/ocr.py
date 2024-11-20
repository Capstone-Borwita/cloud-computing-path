import random
import string
from fastapi import (
    APIRouter,
    status,
    Depends,
    UploadFile,
    File,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pathlib import Path
from app.models.user import User
from app.schemas.model_schema import KTP_OCR_Result
from app.schemas.response_schema import (
    SuccessDataResponse,
    InvalidRequestResponse,
)
from app.utils.utils import get_current_user
from app.utils.images.ocr import OCR_IMAGE_PATH
from app.lang.id import indonesia_fields

router = APIRouter()

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/jpg"}


def generate_random_filename(original_filename: str) -> str:
    random_string = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=16)
    )
    file_extension = Path(original_filename).suffix

    return random_string + file_extension


@router.post("/ktp")
def ocr_ktp(
    ktp_photo: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
) -> SuccessDataResponse[KTP_OCR_Result]:
    if ktp_photo.content_type not in ALLOWED_IMAGE_TYPES:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                InvalidRequestResponse(
                    message=f"Kolom {indonesia_fields['ktp_photo']} tidak valid. Hanya boleh JPEG atau PNG"
                )
            ),
        )

    ktp_photo_filename = generate_random_filename(ktp_photo.filename)
    ktp_photo_prefix = current_user.id

    ktp_photo_path = OCR_IMAGE_PATH / f"{ktp_photo_prefix}_ktp_{ktp_photo_filename}"

    with open(ktp_photo_path, "wb") as f:
        f.write(ktp_photo.file.read())

    return SuccessDataResponse(
        data=KTP_OCR_Result(
            identifier=ktp_photo_filename,
            nik="1234567890123456",
            name="Budi",
            address="Jl. Jend. Sudirman No. 1",
        )
    )
