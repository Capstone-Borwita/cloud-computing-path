import uvicorn
from app.core.config import settings


def dev():
    uvicorn.run("app.main:app", port=settings.PORT, reload=True)
