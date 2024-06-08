from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('carousel_GUI.kv')


class CarouselWidget(Widget):
    pass


class CarouselWidgetApp(App):
    def build(self):
        return CarouselWidget()


if __name__ == "__main__":
    CarouselWidgetApp().run()
