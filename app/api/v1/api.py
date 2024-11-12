from fastapi import APIRouter
from app.api.v1.endpoints import stores
from app.api.v1.endpoints import users
from app.api.v1.endpoints import auth

api_router = APIRouter()
api_router.include_router(stores.router, prefix="/stores", tags=["store"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])

