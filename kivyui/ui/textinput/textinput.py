import os
from typing import List

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import AliasProperty, StringProperty, ListProperty

from kivyui.theme.color_definitions import colors
from kivyui.config import UI

# Load the KV file for the text input widget
Builder.load_file(os.path.join(UI, "textinput", "textinput.kv"))


class UITextInput(BoxLayout):
    """
    A custom text input widget with an icon, hint text, and outline color.
    """

    # The primary color for the widget's outline and styling.
    color = StringProperty("green")

    # The text content of the input field.
    text = StringProperty("")

    # The icon filename to be displayed in the widget.
    icon = StringProperty("material-symbols--search-rounded.png")

    # The RGBA color of the icon.
    icon_color = ListProperty(
        [0.5803921568627451, 0.6392156862745098, 0.7215686274509804, 1.0]
    )

    # The hint text displayed when the input field is empty.
    hint_text = StringProperty("Search...")

    def _get_icon(self) -> str:
        """
        Get the full path to the icon file.

        Returns:
            str: The path to the icon file.
        """
        return f"kivyui/data/icons/{self.icon}"

    # An alias property to dynamically get the icon's file path.
    _icon = AliasProperty(_get_icon, None, bind=["icon"])

    def _get_outline_color(self) -> List[float]:
        """
        Get the outline color based on the current `color` property.

        Returns:
            List[float]: The RGBA values of the outline color.
        """
        return colors.get(self.color).get("fill")

    # An alias property to dynamically get the outline color.
    outline_color = AliasProperty(_get_outline_color, None, bind=["color"])
