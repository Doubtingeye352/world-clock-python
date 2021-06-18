from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from  kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from datetime import datetime
import pytz



Window.clearcolor= (1,1,1,1)

text = TextInput()
btn = Button(text="calculate time!")

def func(instance):
    tz_NY = pytz.timezone(text.text)
    datetime_NY = datetime.now(tz_NY)
    print("time:", datetime_NY.strftime("%H:%M:%S"))

class app(App):
    def build(self):
        scr = Screen()
        box = BoxLayout(orientation="vertical")
        btn.bind(on_press=func)
        scr.add_widget(box)
        box.add_widget(text)
        box.add_widget(btn)
        return scr

app().run()
