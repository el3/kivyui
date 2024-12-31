from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.properties import BooleanProperty, ObjectProperty


class NavBar2(BoxLayout):
    pass


KV = """
#:import Calendar calendar.Calendar

<NavButton@HoverBehavior+ButtonBehavior+Label>:


<NavBar2>:


<Day@Button>:
    datepicker: self.parent.datepicker
    color: [1,1,1,1]
    background_color: root.color if self.text != "" else [0,0,0,0]
    disabled: True if self.text == "" else False
    on_release:
        root.datepicker.picked = [int(self.text), root.datepicker.month, root.datepicker.year]

<Week@BoxLayout>:
    datepicker: root.parent
    weekdays: ["","","","","","",""]
    Day:
        text: str(root.weekdays[0])
    Day:
        text: str(root.weekdays[1])
    Day:
        text: str(root.weekdays[2])
    Day:
        text: str(root.weekdays[3])
    Day:
        text: str(root.weekdays[4])
    Day:
        text: str(root.weekdays[5])
    Day:
        text: str(root.weekdays[6])

<WeekDays@BoxLayout>:
    Label:
        text: "Mon"
    Label:
        text: "Tue"
    Label:
        text: "Wed"
    Label:
        text: "Thu"
    Label:
        text: "Fri"
    Label:
        text: "Sat"
    Label:
        text: "Sun"

<NavBar@BoxLayout>:
    datepicker: self.parent
    Spinner:
        values: root.datepicker.months
        text: root.datepicker.months[root.datepicker.month-1]
        on_text:
            root.datepicker.month = root.datepicker.months.index(self.text)+1
    Spinner:
        values: [str(i) for i in range(1970,2100)]
        text: str(root.datepicker.year)
        on_text:
            root.datepicker.year = int(self.text)
    Widget:
    Button:
        text: "<"
        on_release:
            if root.datepicker.month == 1 and spin.text == "Month": root.datepicker.year -= 1
            if spin.text == "Month": root.datepicker.month = 12 if root.datepicker.month == 1 else root.datepicker.month - 1
            if spin.text == "Year": root.datepicker.year -= 1
    Spinner:
        id: spin
        values: ["Month","Year"]
        text: "Month"

    Button:
        text: ">"
        on_release:
            if root.datepicker.month == 12 and spin.text == "Month": root.datepicker.year += 1
            if spin.text == "Month": root.datepicker.month = 1 if root.datepicker.month == 12 else root.datepicker.month + 1
            if spin.text == "Year": root.datepicker.year += 1

<DatePicker@BoxLayout>:
    year: 2020
    month: 1
    picked: ["","",""]
    months: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    calendar: Calendar()
    days: [(i if i > 0 else "") for i in self.calendar.itermonthdays(self.year, self.month)] + [""] * 14
    orientation: "vertical"
    NavBar:
    WeekDays:
    Week:
        weekdays: root.days[0:7]
    Week:
        weekdays: root.days[7:14]
    Week:
        weekdays: root.days[14:21]
    Week:
        weekdays: root.days[21:28]
    Week:
        weekdays: root.days[28:35]
    Week:
        weekdays: root.days[35:]
    Label:
        text: "" if root.picked == ["","",""] else "{}/{}-{}".format(root.picked[0], root.picked[1], root.picked[2])
"""


class DatePicker(BoxLayout):
    pass


class HoverBehavior(object):
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super().__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return  # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass


Factory.register('HoverBehavior', HoverBehavior)

Builder.load_string(KV)
