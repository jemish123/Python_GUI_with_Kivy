from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file('image_button.kv')


class ImageButtonWidget(Widget):
    def hello_button_pressed(self):
        self.ids.my_label.text = "Button Pressed."
        self.ids.my_image.source = "../src/p1.png"

    def hello_button_released(self):
        self.ids.my_image.source = "../src/logo.jpg"
        self.ids.my_label.text = "Button Released."


class ImageButtonWidgetApp(App):
    def build(self):
        return ImageButtonWidget()


if __name__ == "__main__":
    ImageButtonWidgetApp().run()
