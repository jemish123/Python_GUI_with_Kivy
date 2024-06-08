from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.animation import Animation

Builder.load_file('animation_GUI.kv')


class AnimationWidget(Widget):
    def animate_it(self, wid, *args):
        # First Animation
        animate = Animation(
            background_color=(0, 0, 1, 1),
            duration=5,
        )

        # Second Animation
        animate += Animation(
            size_hint=(1, 1)
        )

        # Third Animation
        animate += Animation(
            size_hint = (0.5, 0.8)
        )

        animate += Animation(
            pos_hint = {'center_x': 0.1}
        )

        animate += Animation(
            pos_hint={'center_x': 0.5}
        )


        animate.start(wid)
        animate.bind(on_complete=self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = "Animation Completed."


class AnimationWidgetApp(App):
    def build(self):
        return AnimationWidget()


if __name__ == "__main__":
    AnimationWidgetApp().run()
