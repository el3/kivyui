from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivyui.behaviors import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import AliasProperty, StringProperty, ListProperty, BooleanProperty
from kivyui.data.colors import colors
from kivy.core.window import Window

KV = """
#:import sp kivy.metrics.sp

<UButton>:
    padding: [0,0,0,0] if '' in [self.left_icon, self.text] else [10,0,0,0]
    canvas.before:
        Color:
            rgba: self.fill_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [10] if not self.rounded else [self.height/2]
        Color:
            rgba: self.outline_color
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10 if not self.rounded else self.height/2, 100)
    Widget:
        size_hint_x: None
        width: 0 if all([root.right_icon == '', root.left_icon == '']) else self.height
        canvas:
            Color:
                rgb: root.font_color[:3]
                a: 0 if root.left_icon == '' else 1
            Rectangle:
                pos: self.x, self.center_y-sp(root.font_size[:-2])/2
                size: sp(root.font_size[:-2]), sp(root.font_size[:-2])
                source: root._left_icon
    Label:
        text: root.text
        color: root.font_color
        font_size: root.font_size
    Widget:
        size_hint_x: None
        width: 0 if all([root.right_icon == '', root.left_icon == '']) else self.height
        canvas:
            Color:
                rgb: root.font_color[:3]
                a: 0 if root.right_icon == '' else 1
            Rectangle:
                pos: self.x, self.center_y-sp(root.font_size[:-2])/2
                size: sp(root.font_size[:-2]), sp(root.font_size[:-2])
                source: root._right_icon
"""


class UButton(HoverBehavior,ButtonBehavior,BoxLayout):
    rounded = BooleanProperty(False)
    font_size = StringProperty("20sp")
    text = StringProperty('')
    color = StringProperty('green')
    variant = StringProperty('solid')
    left_icon = StringProperty('')
    right_icon = StringProperty('')

    def _get_left_icon(self):
        if self.left_icon != "":
            return f'kivyui/data/icons/{self.left_icon}'
        else:
            return ""

    _left_icon = AliasProperty(_get_left_icon, None, bind=['left_icon'])


    def _get_right_icon(self):
        if self.right_icon != "":
            return f'kivyui/data/icons/{self.right_icon}'
        else:
            return ""

    _right_icon = AliasProperty(_get_right_icon, None, bind=['right_icon'])

    def _get_font_color(self):
        if self.variant == 'solid':
            return colors.get(self.color).get('font')
        else:
            return colors.get(self.color).get('fill')

    font_color = AliasProperty(_get_font_color, None, bind=['color','hovered','variant'])

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
        return colors.get(self.color).get(fill)

    fill_color = AliasProperty(_get_fill_color, None, bind=['color','hovered','variant'])

    def _get_outline_color(self):
        if self.variant == 'outline':
            return colors.get(self.color).get('fill')
        else:
            return [0,0,0,0]

    outline_color = AliasProperty(_get_outline_color, None, bind=['color'])

    def on_enter(self, *args):
        Window.set_system_cursor('hand')

    def on_leave(self, *args):
        Window.set_system_cursor('arrow')

Builder.load_string(KV)
