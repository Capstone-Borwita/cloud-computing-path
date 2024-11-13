import random
import string
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import select
from app.core.config import settings
from app.models.user import User
from app.database import SessionDep

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(session: SessionDep, token: str = Depends(oauth2_scheme)) -> User:
    user = session.exec(select(User).filter(User.token == token)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


def create_access_token() -> str:
    randomizer = random.SystemRandom()
    dictionary = string.ascii_letters + string.digits
    length = settings.token_length

    return "".join([randomizer.choice(dictionary) for _ in range(length)])
