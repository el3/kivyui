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
from kivy.properties import StringProperty, ListProperty, NumericProperty, AliasProperty, ObjectProperty
from kivy.clock import Clock

from kivyui.ui import UButton
from kivyui.config import UI


Builder.load_file(os.path.join(UI, "datepicker", "datepicker.kv"))


class NavBar(BoxLayout):

    month_object = ObjectProperty(None)

    _date_string = StringProperty("")

    def change_month(self, add_month=1):
        dt = datetime.fromtimestamp(self.month_object._timestamp)
        dt = dt + relativedelta(months=add_month)
        dt = int(dt.timestamp())
        self.month_object.set_month(dt)
        self._date_string = datetime.fromtimestamp(dt).strftime("%B %Y")


class Day(BoxLayout):
    text = StringProperty("")
    year = NumericProperty(0)
    month = NumericProperty(0)
    month_object = ObjectProperty(None)

    def select_date(self, day_button):
        self.month_object.select_date(day_button)


class EmptyDay(Widget):
    pass


class Week(BoxLayout):
    pass


class Month(BoxLayout):
    calendar = Calendar()
    datepicker = ObjectProperty(None)
    _timestamp = 0

    def __init__(self,timestamp,**kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(partial(self.set_month,timestamp))

    def set_month(self,timestamp, dt=0):
        self._timestamp = timestamp
        date = datetime.fromtimestamp(timestamp)
        cal = self.calendar.monthdatescalendar(date.year, date.month)
        self.clear_widgets()
        for w in cal:
            bl = Week()
            for d in w:
                if d.month == date.month:
                    bl.add_widget(Day(text=f"{d.day}", year=d.year, month=d.month, month_object=self))
                else:
                    bl.add_widget(Widget())
            self.add_widget(bl)

    def select_date(self, day_button):
        for w in self.children:
            for d in w.children:
                if isinstance(d, Day):
                    d.selected = False
        self.datepicker._set_date(day_button.year, day_button.month, int(day_button.text))


class DatePickerDropDown(DropDown):
    pass


class WeekDayNames(BoxLayout):
    def __init__(self, wn, **kwargs):
        super().__init__(**kwargs)
        for d in wn:
            self.add_widget(Label(text=d))


class DatePicker(UButton):
    week_day_names = ListProperty(['M','T','W','T','F','S','S'])
    _selected_timestamp = NumericProperty(datetime.now().timestamp())

    def get_selected_date(self):
        return datetime.fromtimestamp(self._selected_timestamp)

    selected_date = AliasProperty(get_selected_date,None,bind=['_selected_timestamp'])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = DatePickerDropDown()
        now = datetime.now().timestamp()
        self.month = Month(now, datepicker=self)
        self.navbar = NavBar(month_object=self.month)
        self._set_text(now)
        self.dropdown.add_widget(self.navbar)
        self.dropdown.add_widget(WeekDayNames(self.week_day_names))
        self.dropdown.add_widget(self.month)

    def _set_text(self, timestamp):
        self.text = datetime.fromtimestamp(timestamp).strftime("%d %b ,%Y")
        self._selected_timestamp = timestamp
        self.navbar._date_string = datetime.fromtimestamp(timestamp).strftime("%B %Y")

    def _set_date(self, year, month, day):
        timestamp = datetime(year, month, day).timestamp()
        self._set_text(timestamp)

    def on_release(self):
        self.dropdown.open(self)
