from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivyui.widgets.ubutton import UButton

KV = """
<UDropDown>:
    left_icon: 'material-symbols--keyboard-arrow-down.png'
    text: root.text
    color: 'stone'
    variant: 'outline'


<UBoxLayout>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: .7,.7,.7,1
        Line:
            points: self.x+10, self.y, self.x+self.width-10, self.y   

<UDropDownWidget>:
    canvas.before:
        Color:
            rgba: .1,.2,.3, 1
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)]
        Color:
            rgba: .7,.7,.7,1
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10, 10, 10, 10, 100)    

    background: ''
    background_color: 0,0,0,0
    
<UDropDownLabel>:
    size_hint_y: None
    text_size: root.width, None
    height: self.texture_size[1]+20
    halign: 'left'
    valign: 'middle'
    padding: [40,0,0,0]
"""

class UDropDownLabel(ButtonBehavior,Label):
    pass

class UDropDownWidget(DropDown):
    pass
class UDropDown(UButton):
    text = StringProperty('Options')
    items = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = UDropDownWidget()

    def on_items(self, *args):
        for section in self.items:
            bl = UBoxLayout(size_hint_y=None)
            bl.bind(minimum_height=bl.setter('height'))
            for widget in section:
                label = UDropDownLabel(text=widget.get('label'))
                if widget.get('on_release'):
                    label.bind(on_release=widget.get('on_release'))
                if widget.get('on_press'):
                    label.bind(on_press=widget.get('on_press'))
                bl.add_widget(label)
            self.dropdown.add_widget(bl)

    def on_release(self):
        self.dropdown.open(self)


class UBoxLayout(BoxLayout):
    pass



Builder.load_string(KV)
