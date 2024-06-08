from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('checkbox_GUI.kv')


class CheckBoxWidget(Widget):
    
    checks = list()
    def checkbox_click(self, instance, value, topping):
        if value:
            CheckBoxWidget.checks.append(topping)
            tops = ''
            for x in CheckBoxWidget.checks:
                tops += f'{x} '
            self.ids.selected_toppings.text = tops
        else:
            CheckBoxWidget.checks.remove(topping)
            tops = ''
            for x in CheckBoxWidget.checks:
                tops += f'{x} '
            self.ids.selected_toppings.text = tops

class CheckBoxWidgetApp(App):
    def build(self):
        return CheckBoxWidget()


if __name__ == "__main__":
    CheckBoxWidgetApp().run()
