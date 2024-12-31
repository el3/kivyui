from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from behaviors import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import AliasProperty, StringProperty, ListProperty
from data.colors import colors
from kivy.core.window import Window

KV = """
#:import sp kivy.metrics.sp

<UButton>:
    padding: [10,0,0,0]
    canvas.before:
        Color:
            rgba: self.fill_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)]
        Color:
            rgba: self.outline_color
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10, 10, 10, 10, 100)
    Widget:
        size_hint_x: None
        width: self.height if root.icon != '' else 0
        canvas:
            Color:
                rgba: root.icon_color
            Rectangle:
                pos: self.x, self.center_y-sp(root.font_size[:-2])/2
                size: sp(root.font_size[:-2]), sp(root.font_size[:-2])
                source: f'data/icons/{root.icon}'
    Label:
        text: root.text
        color: root.font_color
        font_size: root.font_size
"""


class UButton(HoverBehavior,ButtonBehavior,BoxLayout):
    font_size = StringProperty("20sp")
    text = StringProperty('')
    ucolor = StringProperty('green')
    variant = StringProperty('solid')
    icon = StringProperty('material-symbols--search-rounded.png')
    icon_color = ListProperty([0.5803921568627451, 0.6392156862745098, 0.7215686274509804, 1.0])

    def _get_font_color(self):
        if self.variant == 'solid':
            return colors.get(self.ucolor).get('font')
        else:
            return colors.get(self.ucolor).get('fill')

    font_color = AliasProperty(_get_font_color, None, bind=['ucolor','hovered','variant'])

    def _get_fill_color(self):
        if self.hovered:
            if self.variant in ['outline', 'ghost']:
                fill = 'outline_hover'
            else:
                fill = 'fill_hover'
        if not self.hovered:
            if self.variant in ['outline', 'ghost']:
                return [0,0,0,0]
            else:
                fill = 'fill'
        return colors.get(self.ucolor).get(fill)

    fill_color = AliasProperty(_get_fill_color, None, bind=['ucolor','hovered','variant'])

    def _get_outline_color(self):
        if self.variant == 'outline':
            return colors.get(self.ucolor).get('fill')
        else:
            return [0,0,0,0]

    outline_color = AliasProperty(_get_outline_color, None, bind=['ucolor'])

    def on_enter(self, *args):
        Window.set_system_cursor('hand')

    def on_leave(self, *args):
        Window.set_system_cursor('arrow')

Builder.load_string(KV)
