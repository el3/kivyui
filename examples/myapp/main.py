from kivy.app import App
from kivy.lang import Builder

from kivyui.widgets.dropdown import UDropDown

KV = """
BoxLayout:
    orientation: 'vertical'
    padding: 50
    spacing: 10
    BoxLayout:
        spacing: 10
        MyDropDown:
            items: self.myitems
        UButton:
            color: 'stone'
            variant: 'outline'
            text: 'Save'
            right_icon: 'material-symbols--save-as-outline-rounded.png'
    BoxLayout:
        spacing: 10
        UButton:
            left_icon: 'material-symbols--search-rounded.png'
            variant: 'outline'
            text: 'More Button'
            on_release:
                self.text = 'pushed'
        DatePicker:
    BoxLayout:
        spacing: 10
        UButton:
            color: 'purple'
            text: 'Button'
            right_icon: 'material-symbols--person-edit-outline.png'
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
            color: 'indigo'
            variant: 'solid'
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


class MyDropDown(UDropDown):
    def profile(self):
        print("Profile")

    def edit(self):
        print("Edit")

    myitems = [
        [{"label": "Profile", "on_release": profile}],
        [{"label": "Edit", "on_press": edit}, {"label": "Duplicate"}],
        [{"label": "Archive"}, {"label": "Move"}],
        [{"label": "Delete"}],
    ]


class MyApp(App):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()
