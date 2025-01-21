from kivy.properties import BooleanProperty, ObjectProperty
from kivy.factory import Factory
from kivy.core.window import Window
from typing import Any


class HoverBehavior:
    """
    A mixin class to add hover behavior to a Kivy widget.

    :Events:
        `on_enter`: Fired when the mouse enters the widget's bounding box.
        `on_leave`: Fired when the mouse exits the widget's bounding box.
    """

    # Indicates if the mouse is currently hovering over the widget.
    hovered = BooleanProperty(False)

    # Stores the last relevant mouse position when hovering.
    border_point = ObjectProperty(None)

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize the HoverBehavior and bind mouse position events.
        """
        self.register_event_type("on_enter")
        self.register_event_type("on_leave")
        Window.bind(mouse_pos=self.on_mouse_pos)
        super().__init__(**kwargs)

    def on_mouse_pos(self, *args: Any) -> None:
        """
        Handles mouse position updates and determines if the mouse
        enters or exits the widget's bounding box.

        Args:
            *args: Arguments passed by the Window's `mouse_pos` event.
        """
        if not self.get_root_window():
            return  # Do not proceed if the widget is not displayed (no parent).

        pos = args[1]  # Extract the mouse position.
        inside = self.collide_point(
            *self.to_widget(*pos)
        )  # Adjust for relative layout.

        if self.hovered == inside:
            return  # No change in hover state.

        self.border_point = pos
        self.hovered = inside

        if inside:
            self.dispatch("on_enter")
        else:
            self.dispatch("on_leave")

    def on_enter(self) -> None:
        """
        Event handler triggered when the mouse enters the widget's bounding box.
        Override this method to define custom behavior.
        """
        pass

    def on_leave(self) -> None:
        """
        Event handler triggered when the mouse exits the widget's bounding box.
        Override this method to define custom behavior.
        """
        pass


# Register the HoverBehavior class with the Kivy Factory for dynamic usage.
Factory.register("HoverBehavior", HoverBehavior)
