from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import AliasProperty, StringProperty, ListProperty

from kivyui.data.colors import colors
from kivyui.utils import get_icon_path


class UTextInput(BoxLayout):

    color = StringProperty("green")

    text = StringProperty("")

    icon = StringProperty("material-symbols--search-rounded.png")

    icon_color = ListProperty(
        [0.5803921568627451, 0.6392156862745098, 0.7215686274509804, 1.0]
    )

    hint_text = StringProperty("Search...")

    def _get_icon(self, *args) -> str:
        return get_icon_path(self.icon)

    _icon = AliasProperty(_get_icon, None, bind=["icon"])

    def _get_outline_color(self, *args) -> list[float] | list:
        return colors.get(self.color).get("fill")

    outline_color = AliasProperty(_get_outline_color, None, bind=["color"])

    # repeated
    # def _get_outline_color(self) -> (list[float] | list):
    #     return colors.get(self.color).get('fill')
