from fastapi import APIRouter
from app.api.v1.endpoints import auth
from app.api.v1.endpoints import ocr
from app.api.v1.endpoints import stores
from app.api.v1.endpoints import news

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(ocr.router, prefix="/ocr", tags=["OCR"])
api_router.include_router(stores.router, prefix="/stores", tags=["store"])
api_router.include_router(news.router, prefix="/news", tags=["news"])
