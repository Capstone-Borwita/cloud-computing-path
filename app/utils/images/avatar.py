from os import listdir
from pathlib import Path
import random

USER_AVATAR_PATH = Path("images/user-content/avatar")
USER_AVATAR_PATH.mkdir(parents=True, exist_ok=True)

DEFAULT_USER_AVATAR_PATH = Path("images/default/avatar")
default_user_avatars = [
    str(DEFAULT_USER_AVATAR_PATH / default_user_avatar)
    for default_user_avatar in listdir(DEFAULT_USER_AVATAR_PATH)
]


def random_user_avatar() -> str:
    return random.choice(default_user_avatars)
