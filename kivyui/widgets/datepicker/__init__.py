import os

from kivy.lang import Builder

from kivyui.config import WIDGETS
from .datepicker import DatePicker

Builder.load_file(os.path.join(WIDGETS, "datepicker", "datepicker.kv"))
