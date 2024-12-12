from pydantic_settings import BaseSettings
from enum import Enum


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings(BaseSettings):
    PROJECT_NAME: str = "API KTP Borwita"
    MODE: ModeEnum = ModeEnum.development
    API_VERSION: str = "v1"
    API_V1_STR: str = "/api/v1"
    PORT: int = 8000
    ORIGIN: str = "http://localhost:8000"

    token_length: int = 32

    class Config:
        env_file = ".env"


settings = Settings()
