from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

Builder.load_file('image_viewer.kv')


class ImageViewerLayout(Widget):

    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            pass


class ImageViewerApp(App):
    def build(self):
        return ImageViewerLayout()


if __name__ == "__main__":
    ImageViewerApp().run()