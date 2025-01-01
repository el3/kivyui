from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, NumericProperty, AliasProperty, ObjectProperty
from kivy.clock import Clock
from kivyui.widgets import UButton
from calendar import Calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta
from functools import partial


KV = """
#:import rgba kivy.utils.rgba
<NavBar>:
    padding: [10,10,10,10]
    size_hint_y: None
    height: 44
    UButton:
        color: 'sky'
        variant: 'ghost'
        icon: 'material-symbols--arrow-back-ios-new-rounded.png'
        size_hint_x: None
        width: self.height
    UButton:
        color: 'sky'
        variant: 'ghost'
        text: root._date_string
    UButton:
        color: 'sky'
        variant: 'ghost'
        icon: 'material-symbols--arrow-forward-ios-rounded.png'
        size_hint_x: None
        width: self.height
        on_release:
            root.change_month()

<WeekDayNames>:
    padding: [10,0,10,0]
    size_hint_y: None
    height: 44
    
<DatePicker>:
    icon: 'material-symbols--calendar-month-rounded.png'
    icon_color: [0,0,0,1]

<Month>:
    spacing: 10
    orientation: 'vertical'
    size_hint_y: None
    height: 44*6
    padding: [10,0,10,10]
    
<Week>:
    size_hint_y: None
    height: 36

<Day>:
    selected: False
    text: ''
    Widget:
    UButton:
        color: 'sky' if not root.selected else 'green'
        rounded: True
        text: root.text
        size_hint_x: None
        width: self.height
        id: day
        on_release:
            root.select_date(root)
            root.selected = True
    Widget:


<DatePickerDropDown>:
    canvas.before:
        Color:
            rgba: rgba('#0f172a')
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [10]
        Color:
            rgba: .5,.5,.5,1
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10, 10, 10, 10, 100)
    size_hint_x: None
    width: self.height/8*7
    auto_width: False
"""


class NavBar(BoxLayout):
    month_object = ObjectProperty(None)
    _date_string = StringProperty("")

    #def _set_date_string

    def change_month(self):
        dt = datetime.fromtimestamp(self.month_object._timestamp)
        dt = dt + relativedelta(months=1)
        dt = int(dt.timestamp())
        self.month_object.set_month(dt)
        self._date_string = datetime.fromtimestamp(dt).strftime("%b %Y")

class Day(BoxLayout):
    text = StringProperty("")
    year = NumericProperty(0)
    month = NumericProperty(0)

    def select_date(self, day_button):
        self.parent.parent.select_date(day_button)


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
        # for i in c.itermonthdays4(2025,1): print(i)
        self._timestamp = timestamp
        date = datetime.fromtimestamp(timestamp)
        cal = self.calendar.monthdatescalendar(date.year, date.month)
        self.clear_widgets()
        for w in cal:
            bl = Week()
            for d in w:
                if d.month == date.month:
                    bl.add_widget(Day(text=f"{d.day}", year=d.year, month=d.month))
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
        self.text = datetime.fromtimestamp(timestamp).strftime("%-d %b, %Y")
        self.navbar._date_string = datetime.fromtimestamp(timestamp).strftime("%b %Y")

    def _set_date(self, year, month, day):
        timestamp = datetime(year, month, day).timestamp()
        self._set_text(timestamp)

    def on_release(self):
        self.dropdown.open(self)


Builder.load_string(KV)