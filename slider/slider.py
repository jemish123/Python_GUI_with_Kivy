from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('slider.kv')


class SliderWidget(Widget):

    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = args[1]

class SliderWidgetApp(App):
    def build(self):
        return SliderWidget()


if __name__ == "__main__":
    SliderWidgetApp().run()
