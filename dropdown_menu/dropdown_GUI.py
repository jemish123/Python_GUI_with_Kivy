from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('dropdown_GUI.kv')


class DropdownWidget(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'Your Subject: {value}'


class DropdownWidgetApp(App):
    def build(self):
        return DropdownWidget()


if __name__ == "__main__":
    DropdownWidgetApp().run()
