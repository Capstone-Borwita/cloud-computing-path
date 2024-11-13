from os import listdir
from pathlib import Path
import random

USER_AVATAR_PATH = Path("images/user-content/avatar")
USER_AVATAR_PATH.mkdir(exist_ok=True)

DEFAULT_USER_AVATAR_PATH = Path("images/default/avatar")
default_user_images = listdir(DEFAULT_USER_AVATAR_PATH)


def random_user_avatar() -> str:
    return f"/{DEFAULT_USER_AVATAR_PATH}/{random.choice(default_user_images)}"
