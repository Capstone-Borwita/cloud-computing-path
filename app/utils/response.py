from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.response_schema import InvalidRequestResponse


def invalid_request_response(
    message: str, status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY
):
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(InvalidRequestResponse(message=message)),
    )
