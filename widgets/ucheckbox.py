from kivy.lang import Builder
from kivy.uix.label import Label
from behaviors import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import AliasProperty, StringProperty
from data.colors import colors
from kivy.core.window import Window

KV = """
<UButton>:
    color: self.font_color
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
"""


class UButton(HoverBehavior,ButtonBehavior,Label):
    ucolor = StringProperty('green')
    variant = StringProperty('solid')
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
