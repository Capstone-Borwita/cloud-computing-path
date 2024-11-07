from typing import Annotated, Sequence
from fastapi import APIRouter, status, Query, HTTPException
from sqlmodel import select

from app.database import SessionDep
from app.models.store import StoreCreate, StoreUpdate, Store
from app.schemas.model_schema import ModelId
from app.schemas.response_schema import (
    SuccessIdResponse,
    SuccessResponse,
    SuccessDataResponse,
)

router = APIRouter()


def store_not_found():
    return HTTPException(status_code=404, detail="Store not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_store(session: SessionDep, store_in: StoreCreate) -> SuccessIdResponse:
    store = Store.model_validate(store_in)

    session.add(store)
    session.commit()
    session.refresh(store)

    return SuccessIdResponse(data=ModelId(id=store.id))


@router.get("/")
def store_list(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> SuccessDataResponse[Sequence[Store]]:
    stores = session.exec(select(Store).offset(offset).limit(limit)).all()

    return SuccessDataResponse(data=stores)


@router.get("/{id}")
def find_store(session: SessionDep, id: int) -> SuccessDataResponse[Store]:
    store = session.get(Store, id)

    if store is None:
        raise store_not_found()

    return SuccessDataResponse(data=store)


@router.put("/{id}")
def update_store(
    session: SessionDep, id: int, store_in: StoreUpdate
) -> SuccessResponse:
    store = session.get(Store, id)

    if store is None:
        raise store_not_found()

    update_dict = store_in.model_dump(exclude_unset=True)
    store.sqlmodel_update(update_dict)

    session.add(store)
    session.commit()
    session.refresh(store)

    return SuccessResponse()


@router.delete("/{id}")
def delete_item(session: SessionDep, id: int) -> SuccessResponse:
    item = session.get(Store, id)
    if item is None:
        raise store_not_found()

    session.delete(item)
    session.commit()

    return SuccessResponse()
