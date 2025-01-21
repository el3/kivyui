from kivy.uix.screenmanager import Screen
from kivyui.theme import UITheme


class UIScreen(Screen, UITheme):
    def __init__(self, **kw):
        super().__init__(**kw)
