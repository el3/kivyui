import os
from calendar import Calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
from functools import partial

from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import (
    StringProperty,
    ListProperty,
    NumericProperty,
    AliasProperty,
    ObjectProperty,
)
from kivy.clock import Clock

from kivyui.ui.button import UIButton
from kivyui.config import UI

# Load the KV file for UI definitions
Builder.load_file(os.path.join(UI, "datepicker", "datepicker.kv"))


class NavBar(BoxLayout):
    """Navigation bar to handle month transitions."""

    month_object = ObjectProperty(None)
    _date_string = StringProperty("")

    def change_month(self, add_month: int = 1) -> None:
        """Change the displayed month by the given offset.

        Args:
            add_month (int): Number of months to add or subtract.
        """
        dt = datetime.fromtimestamp(self.month_object._timestamp)
        dt += relativedelta(months=add_month)
        self.month_object.set_month(int(dt.timestamp()))
        self._date_string = dt.strftime("%B %Y")


class Day(BoxLayout):
    """Represents an individual day in the calendar."""

    text = StringProperty("")
    year = NumericProperty(0)
    month = NumericProperty(0)
    month_object = ObjectProperty(None)

    def select_date(self, day_button: "Day") -> None:
        """Select a date using the given day button.

        Args:
            day_button (Day): The day button that was clicked.
        """
        self.month_object.select_date(day_button)


class EmptyDay(Widget):
    """Represents an empty day slot."""

    pass


class Week(BoxLayout):
    """Represents a week row in the calendar."""

    pass


class Month(BoxLayout):
    """Represents a month view in the calendar."""

    calendar = Calendar()
    datepicker = ObjectProperty(None)
    _timestamp = 0

    def __init__(self, timestamp: int, **kwargs) -> None:
        """Initialize the Month object.

        Args:
            timestamp (int): The timestamp representing the month to display.
        """
        super().__init__(**kwargs)
        Clock.schedule_once(partial(self.set_month, timestamp))

    def set_month(self, timestamp: int, dt: float = 0) -> None:
        """Set the calendar view to the specified month.

        Args:
            timestamp (int): Timestamp of the month to display.
            dt (float): Optional delay time (default is 0).
        """
        self._timestamp = timestamp
        date = datetime.fromtimestamp(timestamp)
        cal = self.calendar.monthdatescalendar(date.year, date.month)
        self.clear_widgets()
        for week in cal:
            week_box = Week()
            for day in week:
                if day.month == date.month:
                    week_box.add_widget(
                        Day(
                            text=f"{day.day}",
                            year=day.year,
                            month=day.month,
                            month_object=self,
                        )
                    )
                else:
                    week_box.add_widget(EmptyDay())
            self.add_widget(week_box)

    def select_date(self, day_button: "Day") -> None:
        """Highlight the selected date.

        Args:
            day_button (Day): The day button representing the selected date.
        """
        for week in self.children:
            for day in week.children:
                if isinstance(day, Day):
                    day.selected = False
        self.datepicker._set_date(
            day_button.year, day_button.month, int(day_button.text)
        )


class UIDatePickerDropDown(DropDown):
    """Custom drop-down for date picker."""

    pass


class WeekDayNames(BoxLayout):
    """Display the week day names in the date picker."""

    def __init__(self, week_names: list[str], **kwargs) -> None:
        """Initialize the weekday names display.

        Args:
            week_names (list[str]): List of weekday abbreviations.
        """
        super().__init__(**kwargs)
        for name in week_names:
            self.add_widget(Label(text=name))


class UIDatePicker(UIButton):
    """Custom date picker widget."""

    week_day_names = ListProperty(["M", "T", "W", "T", "F", "S", "S"])
    _selected_timestamp = NumericProperty(datetime.now().timestamp())

    @property
    def selected_date(self) -> datetime:
        """Return the currently selected date.

        Returns:
            datetime: The selected date as a datetime object.
        """
        return datetime.fromtimestamp(self._selected_timestamp)

    def __init__(self, **kwargs) -> None:
        """Initialize the date picker widget."""
        super().__init__(**kwargs)
        self.dropdown = UIDatePickerDropDown()
        now = datetime.now().timestamp()
        self.month = Month(now, datepicker=self)
        self.navbar = NavBar(month_object=self.month)
        self._set_text(now)
        self.dropdown.add_widget(self.navbar)
        self.dropdown.add_widget(WeekDayNames(self.week_day_names))
        self.dropdown.add_widget(self.month)

    def _set_text(self, timestamp: float) -> None:
        """Update the button text with the formatted date.

        Args:
            timestamp (float): The timestamp of the selected date.
        """
        self.text = datetime.fromtimestamp(timestamp).strftime("%d %b, %Y")
        self._selected_timestamp = timestamp
        self.navbar._date_string = datetime.fromtimestamp(timestamp).strftime("%B %Y")

    def _set_date(self, year: int, month: int, day: int) -> None:
        """Set the selected date.

        Args:
            year (int): Year of the selected date.
            month (int): Month of the selected date.
            day (int): Day of the selected date.
        """
        timestamp = datetime(year, month, day).timestamp()
        self._set_text(timestamp)

    def on_release(self) -> None:
        """Open the date picker dropdown."""
        self.dropdown.open(self)
