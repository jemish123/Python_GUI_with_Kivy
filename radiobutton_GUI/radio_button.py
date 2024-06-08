from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('radio_button.kv')


class RadioButtonWidget(Widget):

    def checkbox_click(self, instance, value, topping):
        if value:
            self.ids.selected_toppings.text = topping

class RadioButtonWidgetApp(App):
    def build(self):
        return RadioButtonWidget()


if __name__ == "__main__":
    RadioButtonWidgetApp().run()
