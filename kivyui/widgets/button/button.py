from kivy.uix.boxlayout import BoxLayout
from kivyui.behaviors import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import AliasProperty, StringProperty, ListProperty, BooleanProperty
from kivy.core.window import Window

from kivyui.data.colors import colors
from kivyui.utils import get_icon_path


class UButton(HoverBehavior, ButtonBehavior, BoxLayout):

    rounded = BooleanProperty(False)

    font_size = StringProperty("20sp")

    text = StringProperty("")

    color = StringProperty("green")

    variant = StringProperty("solid")

    left_icon = StringProperty("")

    right_icon = StringProperty("")

    def _get_left_icon(self, *args) -> str:
        if self.left_icon != "":
            return get_icon_path(self.left_icon)
        else:
            return ""

    _left_icon = AliasProperty(_get_left_icon, None, bind=["left_icon"])

    def _get_right_icon(self, *args) -> str:
        if self.right_icon != "":
            return get_icon_path(self.right_icon)
        else:
            return ""

    _right_icon = AliasProperty(_get_right_icon, None, bind=["right_icon"])

    def _get_font_color(self, *args) -> list[float] | list:
        if self.variant == "solid":
            return colors.get(self.color).get("font")
        else:
            return colors.get(self.color).get("fill")

    font_color = AliasProperty(
        _get_font_color, None, bind=["color", "hovered", "variant"]
    )

    def _get_fill_color(self, *args) -> list[float] | list:
        if self.hovered:
            if self.variant in ["outline", "ghost"]:
                fill = "outline_hover"
            else:
                fill = "fill_hover"
        if not self.hovered:
            if self.variant in ["outline", "ghost"]:
                return [0, 0, 0, 0]
            else:
                fill = "fill"
        return colors.get(self.color).get(fill)

    fill_color = AliasProperty(
        _get_fill_color, None, bind=["color", "hovered", "variant"]
    )

    def _get_outline_color(self, *args) -> list[float] | list:
        if self.variant == "outline":
            return colors.get(self.color).get("fill")
        else:
            return [0, 0, 0, 0]

    outline_color = AliasProperty(_get_outline_color, None, bind=["color"])

    def on_enter(self, *args) -> None:
        Window.set_system_cursor("hand")

    def on_leave(self, *args) -> None:
        Window.set_system_cursor("arrow")
