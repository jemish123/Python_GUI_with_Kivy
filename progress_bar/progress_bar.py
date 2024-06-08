from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('progress_bar.kv')


class ProgressBarWidget(Widget):
    def progress(self):
        current = self.ids.my_progress_bar.value

        if current == 100:
            current = 0

        current += 25
        self.ids.my_progress_bar.value = current
        self.ids.progress_label.text = f'Progress: {int(current)}%'


class ProgressBarWidgetApp(App):
    def build(self):
        return ProgressBarWidget()


if __name__ == "__main__":
    ProgressBarWidgetApp().run()
