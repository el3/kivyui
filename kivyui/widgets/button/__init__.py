import os

from kivy.lang import Builder

from kivyui.config import WIDGETS
from .button import UButton

Builder.load_file(os.path.join(WIDGETS, "button", "button.kv"))
