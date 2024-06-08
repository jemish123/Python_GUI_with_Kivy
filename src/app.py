from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image
import random

Builder.load_file('new_one.kv')


class MyLayout(Widget):
    def change_background(self):
        Window.clearcolor = (random.random(), random.random(), random.random(), 1)

    def greet_user(self):
        name = self.ids.name_input.text

        # update the Label
        self.ids.name_label.text = f'Hello, {name}'

        # clear the input box
        self.ids.name_input.text = ""

class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
