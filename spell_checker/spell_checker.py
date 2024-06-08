from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.core.spelling import Spelling

Builder.load_file('spell_checker.kv')


class SpellChecker(Widget):
    def submit(self):

        try:
            # Create an instance of spelling
            spell = Spelling()

            # Select the language
            spell.select_language('en_US')

            # List the language options
            # spell.list_langauges()

            # Take input word
            word = self.ids.word_input.text

            # Word Suggestion
            option = spell.suggest(word)

            # Update the suggestions in Labels
            self.ids.word_label.text = "  ".join(option)
        except:
            print("Error")


class SpellCheckerApp(App):
    def build(self):
        return SpellChecker()


if __name__ == "__main__":
    SpellCheckerApp().run()