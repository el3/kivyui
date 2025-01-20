from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import AliasProperty, StringProperty, ListProperty
from kivyui.data.colors import colors

KV = """
<UTextInput>:
    canvas.before:
        Color:
            rgba: self.outline_color
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10, 10, 10, 10, 100)
    on_text:
        ti.text = self.text
    orientation: 'vertical'
    Widget:
    BoxLayout:
        size_hint_y: None
        height: ti.height
        padding: [10,0,0,0]
        Widget:
            size_hint_x: None
            width: self.height if root.icon != '' else 0
            canvas:
                Color:
                    rgba: root.icon_color
                Rectangle:
                    pos: self.pos
                    size: self.size
                    source: root._icon
                
        TextInput:
            size_hint_y: None
            height: self.minimum_height
            id: ti
            background_color: 0,0,0,0
            cursor_color: 1,1,1,1
            foreground_color: 1,1,1,1
            multiline: False
            hint_text: root.hint_text
            on_text:
                root.text = self.text
    Widget:
"""


class UTextInput(BoxLayout):
    color = StringProperty('green')
    text = StringProperty('')
    icon = StringProperty('material-symbols--search-rounded.png')
    icon_color = ListProperty([0.5803921568627451, 0.6392156862745098, 0.7215686274509804, 1.0])
    hint_text = StringProperty('Search...')

    def _get_icon(self):
        return f'kivyui/data/icons/{self.icon}'

    _icon = AliasProperty(_get_icon, None, bind=['icon'])

    def _get_outline_color(self):
        return colors.get(self.color).get('fill')

    outline_color = AliasProperty(_get_outline_color, None, bind=['color'])

    def _get_outline_color(self):
        return colors.get(self.color).get('fill')


Builder.load_string(KV)
