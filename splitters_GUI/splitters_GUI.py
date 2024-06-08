from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('splitters_GUI.kv')


class SplittersWidget(Widget):
    pass


class SplittersWidgetApp(App):
    def build(self):
        return SplittersWidget()


if __name__ == "__main__":
    SplittersWidgetApp().run()
