from pydantic import BaseModel


class ModelId(BaseModel):
    id: int
