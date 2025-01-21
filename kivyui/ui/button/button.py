import os
from typing import List, Optional

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import AliasProperty, StringProperty, ListProperty, BooleanProperty
from kivy.core.window import Window

from kivyui.config import UI
from kivyui.theme.color_definitions import colors
from kivyui.behaviors import HoverBehavior

# Load the .kv file for the UIButton component
Builder.load_file(os.path.join(UI, "button", "button.kv"))


class UIButton(HoverBehavior, ButtonBehavior, BoxLayout):
    # Whether the button should have rounded corners
    rounded = BooleanProperty(False)

    # Font size of the button text
    font_size = StringProperty("20sp")

    # Text displayed on the button
    text = StringProperty("")

    # Color name for the button (corresponding to the theme colors)
    color = StringProperty("green")

    # Button variant: "solid", "outline", or "ghost"
    variant = StringProperty("solid")

    # Path to the left icon image
    left_icon = StringProperty("")

    # Path to the right icon image
    right_icon = StringProperty("")

    def _get_left_icon(self) -> str:
        """Get the path to the left icon image."""
        if self.left_icon:
            return f"kivyui/data/icons/{self.left_icon}"
        return ""

    _left_icon = AliasProperty(_get_left_icon, None, bind=["left_icon"])

    def _get_right_icon(self) -> str:
        """Get the path to the right icon image."""
        if self.right_icon:
            return f"kivyui/data/icons/{self.right_icon}"
        return ""

    _right_icon = AliasProperty(_get_right_icon, None, bind=["right_icon"])

    def _get_font_color(self) -> List[float]:
        """Get the font color based on the button's variant and color."""
        if self.variant == "solid":
            return colors.get(self.color).get("font")
        return colors.get(self.color).get("fill")

    font_color = AliasProperty(
        _get_font_color, None, bind=["color", "hovered", "variant"]
    )

    def _get_fill_color(self) -> List[float]:
        """Get the fill color based on the button's hover state and variant."""
        if self.hovered:
            fill = (
                "outline_hover"
                if self.variant in ["outline", "ghost"]
                else "fill_hover"
            )
        else:
            if self.variant in ["outline", "ghost"]:
                return [0, 0, 0, 0]
            fill = "fill"
        return colors.get(self.color).get(fill)

    fill_color = AliasProperty(
        _get_fill_color, None, bind=["color", "hovered", "variant"]
    )

    def _get_outline_color(self) -> List[float]:
        """Get the outline color based on the button's variant."""
        if self.variant == "outline":
            return colors.get(self.color).get("fill")
        return [0, 0, 0, 0]

    outline_color = AliasProperty(_get_outline_color, None, bind=["color"])

    def on_enter(self, *args: Optional[object]) -> None:
        """Change the cursor to a hand when the mouse enters the button area."""
        Window.set_system_cursor("hand")

    def on_leave(self, *args: Optional[object]) -> None:
        """Revert the cursor to the default arrow when the mouse leaves the button area."""
        Window.set_system_cursor("arrow")
