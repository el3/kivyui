from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty, ListProperty

from kivyui.widgets.button.button import UButton


class UDropDownLabel(ButtonBehavior, Label):
    pass


class UDropDownWidget(DropDown):
    pass


class UDropDown(UButton):

    text = StringProperty("Options")

    items = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = UDropDownWidget()

    def on_items(self, *args) -> None:
        for section in self.items:
            bl = UBoxLayout(size_hint_y=None)
            bl.bind(minimum_height=bl.setter("height"))
            for widget in section:
                label = UDropDownLabel(text=widget.get("label"))
                if widget.get("on_release"):
                    label.bind(on_release=widget.get("on_release"))
                if widget.get("on_press"):
                    label.bind(on_press=widget.get("on_press"))
                bl.add_widget(label)
            self.dropdown.add_widget(bl)

    def on_release(self, *args) -> None:
        self.dropdown.open(self)


class UBoxLayout(BoxLayout):
    pass
