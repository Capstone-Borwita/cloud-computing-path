import uvicorn
from fastapi import FastAPI
from app.api.v1.api import api_router as api_router_v1
from app.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


app.include_router(api_router_v1, prefix=settings.API_V1_STR)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
