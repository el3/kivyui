from kivy.app import App
from kivy.lang import Builder
from kivyui.widgets import UButton


KV = """
BoxLayout:
    orientation: 'vertical'
    padding: 50
    spacing: 10
    BoxLayout:
        spacing: 10
        UDropDown:
        UButton:
            ucolor: 'stone'
            variant: 'outline'
            text: 'Button'
    BoxLayout:
        spacing: 10
        UButton:
            variant: 'outline'
            text: 'More Button'
            on_release:
                self.text = 'pushed'
        UButton:
            text: 'More Button'
    BoxLayout:
        spacing: 10
        UButton:
            ucolor: 'orange'
            text: 'Button'
        UButton:
            ucolor: 'orange'
            variant: 'outline'
            text: 'Button'
    BoxLayout:
        spacing: 10
        UButton:
            ucolor: 'orange'
            variant: 'outline'
            text: 'More Button'
            on_release:
                self.text = 'pushed'
        UButton:
            ucolor: 'orange'
            text: 'More Button'
    BoxLayout:
        spacing: 10
        UButton:
            ucolor: 'stone'
            text: 'Button'
        UButton:
            ucolor: 'stone'
            variant: 'outline'
            text: 'Button'
    BoxLayout:
        spacing: 10
        UButton:
            ucolor: 'stone'
            variant: 'outline'
            text: 'More Button'
            on_release:
                self.text = 'pushed'
        UButton:
            ucolor: 'stone'
            text: 'More Button'
    BoxLayout:
        spacing: 10
        UTextInput:
            ucolor: 'red'
            text: 'More TextInput'
        UTextInput:
            ucolor: 'sky'
            text: 'More textinput'
    BoxLayout:
        spacing: 10
        UTextInput:
            ucolor: 'green'
            text: 'More TextInput'
        UTextInput:
            ucolor: 'indigo'
            text: 'More textinput'
  
"""


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()