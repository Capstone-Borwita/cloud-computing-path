import uuid
import os
from typing import List
from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    UploadFile,
    File,
    Query,
    Form,
    status,
)
from sqlalchemy.orm import Session
from app.database import get_session
from app.models.news import News, NewsGet
from app.schemas.response_schema import SuccessDataResponse
from app.core.config import settings
import shutil
from pathlib import Path
from app.utils.images.news import NEWS_IMAGE_PATH
from app.utils.utils import get_current_user
from app.models.user import User


router = APIRouter()

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/jpg"}


@router.post("/", response_model=SuccessDataResponse[News], status_code=201)
def create_news(
    title: str = Form(...),
    content: str = Form(...),
    poster: UploadFile = File(...),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if not title.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Title cannot be empty",
        )

    if not content.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Content cannot be empty",
        )

    if poster.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Unsupported file types, please use jpeg, jpg, and png only",
        )

    file_extension = Path(poster.filename).suffix[1:].lower()
    unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
    file_path = NEWS_IMAGE_PATH / unique_filename

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(poster.file, buffer)

        image_url = f"{settings.ORIGIN}/{str(file_path)}"

        new_news = News(
            title=title,
            content=content,
            poster=str(file_path),
            author_id=current_user.id,
        )
        session.add(new_news)
        session.commit()
        session.refresh(new_news)

        return SuccessDataResponse[News](data=new_news)

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create news")


@router.put("/{news_id}", response_model=SuccessDataResponse[News])
def update_news(
    news_id: int,
    title: str = Form(...),
    content: str = Form(...),
    poster: UploadFile = File(None),
    session: Session = Depends(get_session),
    _: User = Depends(get_current_user),
):
    if not title.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Title cannot be empty",
        )

    if not content.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Content cannot be empty",
        )

    news_item = session.query(News).filter(News.id == news_id).first()
    if not news_item:
        raise HTTPException(status_code=404, detail="News not found")

    news_item.title = title
    news_item.content = content

    if poster:
        if poster.content_type not in ALLOWED_IMAGE_TYPES:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Unsupported file types, please use jpeg, jpg, and png only",
            )

        if news_item.poster:
            old_poster_path = Path(news_item.poster)
            if old_poster_path.exists():
                old_poster_path.unlink()

        file_extension = Path(poster.filename).suffix[1:].lower()
        unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
        file_path = NEWS_IMAGE_PATH / unique_filename

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(poster.file, buffer)

            news_item.poster = str(file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to upload new poster")

    try:
        session.commit()
        session.refresh(news_item)

        return SuccessDataResponse[News](data=news_item)

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Failed to update news")


@router.get("/", response_model=SuccessDataResponse[List[NewsGet]])
def get_news(
    limit: int = Query(10, le=100),
    session: Session = Depends(get_session),
    _: User = Depends(get_current_user),
):
    news_items = session.query(News).limit(limit).all()

    if not news_items:
        raise HTTPException(status_code=404, detail="No news found")

    for news_item in news_items:
        if news_item.poster:
            news_item.poster = settings.ORIGIN + "/" + news_item.poster

    return SuccessDataResponse(data=news_items)


@router.get("/{news_id}", response_model=SuccessDataResponse[News])
def get_news_by_id(
    news_id: int,
    session: Session = Depends(get_session),
):
    news_item = session.query(News).filter(News.id == news_id).first()

    if not news_item:
        raise HTTPException(status_code=404, detail="News not found")

    if news_item.poster:
        news_item.poster = settings.ORIGIN + "/" + news_item.poster

    return SuccessDataResponse[News](data=news_item)


@router.delete("/{news_id}", response_model=SuccessDataResponse[str])
def delete_news(
    news_id: int,
    session: Session = Depends(get_session),
    _: User = Depends(get_current_user),
):
    news_item = session.query(News).filter(News.id == news_id).first()

    if not news_item:
        raise HTTPException(status_code=404, detail="News not found or access denied")

    if news_item.poster and os.path.exists(news_item.poster):
        try:
            os.remove(news_item.poster)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to delete poster: {str(e)}"
            )

    try:
        session.delete(news_item)
        session.commit()

        return SuccessDataResponse[str](data="News deleted successfully")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete news")
