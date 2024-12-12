from typing import Generic, TypeVar, Literal
from pydantic import BaseModel

from app.schemas.model_schema import ModelId, Credential

T = TypeVar("T")


class SuccessResponse(BaseModel):
    detail: Literal["success"] = "success"


class SuccessDataResponse(BaseModel, Generic[T]):
    detail: Literal["success"] = "success"
    data: T


class SuccessIdResponse(BaseModel):
    detail: Literal["success"] = "success"
    data: ModelId


class CredentialResponse(BaseModel):
    detail: Literal["success"] = "success"
    data: Credential


class InvalidRequestResponse(BaseModel):
    detail: Literal["invalid"] = "invalid"
    data: None = None
    message: str
