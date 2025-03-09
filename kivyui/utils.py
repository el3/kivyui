import os

from kivyui.config import DATA


def get_icon_path(filename: str) -> str:
    return os.path.join(DATA, "icons", filename)
