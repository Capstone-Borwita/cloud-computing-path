import uuid
import os
from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Query, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_session
from app.models.news import News, NewsCreate, NewsUpdate, NewsGet
from app.schemas.response_schema import SuccessDataResponse
from app.schemas.response_schema import InvalidRequestResponse
from app.core.config import settings 
from pathlib import Path
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads/news"
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/jpg"}

@router.post("/", response_model=SuccessDataResponse[News], status_code=201)
def create_news(
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(...),
    session: Session = Depends(get_session),
):

    if not title.strip():
        return JSONResponse(
            status_code=400,
            content=InvalidRequestResponse(message="Title cannot be empty").dict(),
        )
    
    if not content.strip():
        return JSONResponse(
            status_code=400,
            content=InvalidRequestResponse(message="Content cannot be empty").dict(),
        )

    if image.content_type not in ALLOWED_IMAGE_TYPES:
        return JSONResponse(
            status_code=400,
            content=InvalidRequestResponse(message="Unsupported file types, please use jpeg, jpg, and png only").dict(),
        )

    file_extension = image.filename.split(".")[-1].lower()
    unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        new_news = News(title=title, content=content, image=file_path)
        session.add(new_news)
        session.commit()
        session.refresh(new_news)
        new_news.image = settings.ORIGIN + "/" + new_news.image

        return SuccessDataResponse[News](data=new_news)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=InvalidRequestResponse(message="Failed to create news").dict(),
        )

@router.put("/{news_id}", response_model=SuccessDataResponse[News])
def update_news(
    news_id: int, 
    title: str = Form(...), 
    content: str = Form(...), 
    image: UploadFile = File(None), 
    session: Session = Depends(get_session),  
):
    if not title.strip():
        return JSONResponse(
            status_code=400,
            content=InvalidRequestResponse(message="Title cannot be empty").dict(),
        )
    
    if not content.strip():
        return JSONResponse(
            status_code=400,
            content=InvalidRequestResponse(message="Content cannot be empty").dict(),
        )

    news_item = session.query(News).filter(News.id == news_id).first()

    if not news_item:
        raise HTTPException(status_code=404, detail="News not found")

    news_item.title = title
    news_item.content = content

    if image:
        if image.content_type not in ALLOWED_IMAGE_TYPES:
            return JSONResponse(
                status_code=400,
                content=InvalidRequestResponse(message="Unsupported file type").dict(),
            )

        if news_item.image and os.path.exists(news_item.image):
            try:
                os.remove(news_item.image)  
            except Exception as e:
                return JSONResponse(
                    status_code=500,
                    content=InvalidRequestResponse(message="Failed to delete old image").dict(),
                )

        file_extension = image.filename.split(".")[-1].lower()
        unique_filename = f"{uuid.uuid4().hex}.{file_extension}"
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)

            news_item.image = file_path

        except Exception as e:
            return JSONResponse(
                status_code=500,
                content=InvalidRequestResponse(message="Failed to upload image").dict(),
            )

    try:
        session.commit()
        session.refresh(news_item)

        news_item.image = settings.ORIGIN + "/" + news_item.image

        return SuccessDataResponse[News](data=news_item)

    except Exception as e:
        session.rollback() 
        return JSONResponse(
            status_code=500,
            content=InvalidRequestResponse(message="Failed to update news").dict(),
        )

@router.get("/", response_model=SuccessDataResponse[List[NewsGet]])
def get_news(
    limit: int = Query(10, le=100),
    session: Session = Depends(get_session),
):
    news_items = session.query(News).limit(limit).all()

    if not news_items:
        raise HTTPException(status_code=404, detail="No news found")
    
    for news_item in news_items:
        if news_item.image:
            news_item.image = settings.ORIGIN + "/" + news_item.image

    return SuccessDataResponse(data=news_items)

@router.get("/{news_id}", response_model=SuccessDataResponse[News])
def get_news_by_id(
    news_id: int,
    session: Session = Depends(get_session), 
):
    news_item = session.query(News).filter(News.id == news_id).first()

    if not news_item:
        raise HTTPException(status_code=404, detail="News not found")

    if news_item.image:
        news_item.image = settings.ORIGIN + "/" + news_item.image

    return SuccessDataResponse[News](data=news_item)


@router.delete("/{news_id}", response_model=SuccessDataResponse[str])
def delete_news(
    news_id: int, 
    session: Session = Depends(get_session),
):
    news_item = session.query(News).filter(News.id == news_id).first()

    if not news_item:
        raise HTTPException(status_code=404, detail="News not found")

    if news_item.image and os.path.exists(news_item.image):
        try:
            os.remove(news_item.image) 
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to delete image: {str(e)}")

    try:
        session.delete(news_item)
        session.commit()

        return SuccessDataResponse[str](data="News deleted successfully")

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete news")