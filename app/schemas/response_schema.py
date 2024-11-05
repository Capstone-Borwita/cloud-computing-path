from typing import Generic, TypeVar, Literal
from pydantic import BaseModel

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    status: Literal["success"] = "success"
    data: T


class SuccessWithMessageResponse(SuccessResponse):
    message: str


class ErrorResponse(BaseModel, Generic[T]):
    status: Literal["error"] = "error"
    data: T


class ErrorWithMessageResponse(ErrorResponse):
    message: str
