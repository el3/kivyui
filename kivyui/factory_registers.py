from kivy.factory import Factory

# Alias for the register function from Factory
register = Factory.register

"""
Registers custom components to the Kivy Factory.

This code registers each component within the "ui" directory to the Kivy Factory. 
Once registered, the components can be used without explicitly importing them elsewhere in the kvlang files.
"""

# Register the component with Kivy's Factory
register("UIButton", module="kivyui.ui.button")
register("UITextInput", module="kivyui.ui.textinput")
register("UIDropdown", module="kivyui.ui.dropdown")
register("UIDatePicker", module="kivyui.ui.datepicker")
