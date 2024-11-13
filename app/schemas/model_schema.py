from pydantic import BaseModel


class ModelId(BaseModel):
    id: int


class Credential(BaseModel):
    id: int
    token: str
