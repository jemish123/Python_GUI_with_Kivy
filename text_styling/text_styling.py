from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('text_styling.kv')


class TextStyle(Widget):
    pass


class TextStyleApp(App):
    def build(self):
        return TextStyle()


if __name__ == "__main__":
    TextStyleApp().run()
