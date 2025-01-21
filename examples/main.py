from kivy.lang import Builder

from kivyui.app import UIApp
from kivyui.ui.dropdown import UIDropDown
from kivyui.ui.screen import UIScreen


class HomeScreen(UIScreen):
    def __init__(self, **kw):
        super().__init__(**kw)


class MyDropDown(UIDropDown):
    def profile(self):
        print("Profile")

    def edit(self):
        print("Edit")

    myitems = [
        [{"label": "Profile", "on_release": profile}],
        [{"label": "Edit", "on_press": edit}, {"label": "Duplicate"}],
        [{"label": "Archive"}, {"label": "Move"}],
        [{"label": "Delete"}],
    ]


class MyApp(UIApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_file("myapp.kv")


if __name__ == "__main__":
    MyApp().run()
