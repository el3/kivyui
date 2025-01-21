import os

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty, ListProperty

from kivyui.config import UI
from kivyui.ui.button import UIButton

# Load the associated .kv file for styling and layout
Builder.load_file(os.path.join(UI, "dropdown", "dropdown.kv"))


class UIDropDownLabel(ButtonBehavior, Label):
    """
    A label widget that behaves like a button, designed for dropdown items.
    """

    pass


class UIDropDownWidget(DropDown):
    """
    Custom dropdown widget to display a list of items.
    """

    pass


class UIDropDown(UIButton):
    """
    Custom dropdown button with dynamic item handling.
    """

    text = StringProperty("Options")  # Text displayed on the button
    items = ListProperty([])  # List of items to populate the dropdown

    def __init__(self, **kwargs) -> None:
        """
        Initialize the dropdown button and its associated dropdown widget.
        """
        super().__init__(**kwargs)
        self.dropdown = UIDropDownWidget()

    def on_items(self, *args) -> None:
        """
        Populate the dropdown with items whenever the 'items' property changes.

        Each section in 'items' is represented as a list of dictionaries,
        where each dictionary contains the 'label' text and optional 'on_release' or 'on_press' handlers.
        """
        for section in self.items:
            section_layout = UBoxLayout(size_hint_y=None)
            section_layout.bind(minimum_height=section_layout.setter("height"))
            for widget_data in section:
                label = UIDropDownLabel(text=widget_data.get("label", ""))
                if widget_data.get("on_release"):
                    label.bind(on_release=widget_data["on_release"])
                if widget_data.get("on_press"):
                    label.bind(on_press=widget_data["on_press"])
                section_layout.add_widget(label)
            self.dropdown.add_widget(section_layout)

    def on_release(self) -> None:
        """
        Open the dropdown menu when the button is released.
        """
        self.dropdown.open(self)


class UBoxLayout(BoxLayout):
    """
    Custom box layout for organizing dropdown sections.
    """

    pass
