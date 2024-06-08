from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# Define Different Screens
class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('screen_manager.kv')


class ScreenManagerApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    ScreenManagerApp().run()
