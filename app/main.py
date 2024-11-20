import uvicorn
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from app.api.v1.api import api_router as api_router_v1
from app.core.config import settings, ModeEnum
from app.database import create_db_and_tables
from app.schemas.response_schema import InvalidRequestResponse
from app.lang.id import indonesia_fields


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.mount("/images", StaticFiles(directory="images"), name="static")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.exception_handler(RequestValidationError)
async def custom_form_validation_error(_, exception: RequestValidationError):
    fields = []
    for pydantic_error in exception.errors():
        loc = pydantic_error["loc"]
        filtered_loc = loc[1:] if loc[0] in ("body", "query", "path") else loc
        field_string = ".".join(filtered_loc)  # nested fields with dot-notation

        localized_field = indonesia_fields.get(field_string)
        if localized_field is None:
            if settings.MODE == ModeEnum.development:
                raise ValueError(f"Field '{field_string}' is not localized")
            else:
                localized_field = field_string

        fields.append(localized_field)

    fields = " dan".join(", ".join(fields).rsplit(",", 1))
    message = f"Kolom {fields} tidak valid"

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(InvalidRequestResponse(message=message)),
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    app.openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version=settings.API_VERSION,
        routes=app.routes,
    )

    app.openapi_schema["components"]["schemas"]["HTTPValidationError"]["properties"] = {
        "detail": {
            "type": "string",
            "enum": ["invalid"],
            "const": "invalid",
            "title": "Detail",
            "default": "invalid",
        },
        "data": {
            "type": "null",
            "title": "Data",
        },
        "message": {
            "type": "string",
            "title": "Message",
        },
    }

    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(api_router_v1, prefix=settings.API_V1_STR)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.PORT not in [80, 443],
    )
