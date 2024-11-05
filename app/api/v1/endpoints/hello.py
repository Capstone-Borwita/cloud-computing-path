from fastapi import APIRouter

from app.schemas.response_schema import SuccessResponse

router = APIRouter()


@router.get("/")
async def hello() -> SuccessResponse:
    """
    Returns "Hello World".
    """

    return SuccessResponse(data="Hello World")
