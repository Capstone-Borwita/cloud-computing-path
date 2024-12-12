from abc import ABC
from pydantic import BaseModel


class ModelId(BaseModel):
    id: int


class Credential(BaseModel):
    token: str


class OCRResult(BaseModel, ABC):
    identifier: str


class KTP_OCR_Result(OCRResult):
    nik: str
    name: str
    address: str
