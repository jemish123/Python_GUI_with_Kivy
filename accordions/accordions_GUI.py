from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('accordions_GUI.kv')


class AccordionsWidget(Widget):
    pass


class AccordionsWidgetApp(App):
    def build(self):
        return AccordionsWidget()


if __name__ == "__main__":
    AccordionsWidgetApp().run()
