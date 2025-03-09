import os

from kivy.lang import Builder

from kivyui.config import WIDGETS
from .dropdown import UDropDown

Builder.load_file(os.path.join(WIDGETS, "dropdown", "dropdown.kv"))
