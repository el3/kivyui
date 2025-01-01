from kivy.app import App
from kivy.lang import Builder
import kivyui.widgets


KV = """
BoxLayout:
    orientation: 'vertical'
    padding: 50
    spacing: 10
    BoxLayout:
        spacing: 10
        UDropDown:
        UButton:
            color: 'stone'
            variant: 'outline'
            text: 'Button'
    BoxLayout:
        spacing: 10
        UButton:
            icon: 'material-symbols--search-rounded.png'
            variant: 'outline'
            text: 'More Button'
            on_release:
                self.text = 'pushed'
        DatePicker:
    BoxLayout:
        spacing: 10
        UButton:
            color: 'orange'
            text: 'Button'
        UButton:
            color: 'orange'
            variant: 'outline'
            text: 'Button'
    BoxLayout:
        spacing: 10
        UButton:
            color: 'orange'
            variant: 'outline'
            text: 'More Button'
            on_release:
                self.text = 'pushed'
        UButton:
            color: 'orange'
            text: 'More Button'
    BoxLayout:
        spacing: 10
        UButton:
            color: 'stone'
            text: 'Button'
        UButton:
            color: 'stone'
            variant: 'outline'
            text: 'Button'
    BoxLayout:
        spacing: 10
        UButton:
            color: 'stone'
            variant: 'outline'
            text: 'More Button'
            on_release:
                self.text = 'pushed'
        UButton:
            color: 'stone'
            text: 'More Button'
    BoxLayout:
        spacing: 10
        UTextInput:
            color: 'red'
            text: 'More TextInput'
        UTextInput:
            color: 'sky'
            text: 'More textinput'
    BoxLayout:
        spacing: 10
        UTextInput:
            color: 'green'
            text: 'More TextInput'
        UTextInput:
            color: 'indigo'
            text: 'More textinput'
  
"""


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()