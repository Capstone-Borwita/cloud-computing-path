from fastapi import APIRouter

from app.schemas.response_schema import SuccessDataResponse

router = APIRouter()


@router.get("/")
async def hello() -> SuccessDataResponse:
    """
    Returns "Hello World".
    """

    return SuccessDataResponse(data="Hello World")
