import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.api import api_router as api_router_v1
from app.core.config import settings
from app.database import create_db_and_tables


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.mount("/images", StaticFiles(directory="images"), name="static")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(api_router_v1, prefix=settings.API_V1_STR)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
