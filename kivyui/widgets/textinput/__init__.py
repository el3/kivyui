import os

from kivy.lang import Builder

from kivyui.config import WIDGETS
from .textinput import UTextInput

Builder.load_file(os.path.join(WIDGETS, "textinput", "textinput.kv"))
