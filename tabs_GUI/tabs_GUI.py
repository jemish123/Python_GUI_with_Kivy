from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.tabbedpanel import TabbedPanel


Builder.load_file('tabs_GUI.kv')


class TabsWidget(TabbedPanel):
    pass


class TabsWidgetApp(App):
    def build(self):
        return TabsWidget()


if __name__ == "__main__":
    TabsWidgetApp().run()
