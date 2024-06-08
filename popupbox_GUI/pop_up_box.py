from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('pop_up_box.kv')


class PopUpBoxWidget(Widget):
    pass


class PopUpBoxWidgetApp(App):
    def build(self):
        return PopUpBoxWidget()


if __name__ == "__main__":
    PopUpBoxWidgetApp().run()
