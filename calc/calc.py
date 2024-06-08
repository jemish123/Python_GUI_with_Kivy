from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

# Load the Layout Builder File
Builder.load_file('calc.kv')

# Set the App Size and non-resizable
Window.size = (500, 700)


class CalcLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def remove(self):
        expr = self.ids.calc_input.text

        # Remove the last input
        if len(expr) == 1:
            self.ids.calc_input.text = "0"
        else:
            self.ids.calc_input.text = expr[:-1]

    def button_press(self, button):
        expr = self.ids.calc_input.text

        if 'Error' in expr:
            print("Trueeee")
            expr = ""

        if expr == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{expr}{button}'

    def math_sign(self, sign):
        expr = self.ids.calc_input.text

        # Add + to the string
        self.ids.calc_input.text += sign

    # Decimal Function
    def dot(self):
        expr = self.ids.calc_input.text

        num_list = expr.split("+")

        if "+" in expr and "." not in num_list[-1]:
            self.ids.calc_input.text = f'{expr}.'
        elif "." in expr:
            pass
        else:
            self.ids.calc_input.text += "."

    # function to make positive or negative
    def pos_neg(self):
        expr = self.ids.calc_input.text

        if "-" in expr:
            self.ids.calc_input.text = expr.replace("-", "")
        else:
            self.ids.calc_input.text = f'-{expr}'

    def equals(self):
        try:
            expr = self.ids.calc_input.text
            self.ids.calc_input.text = str(eval(expr))
        except:
            self.ids.calc_input.text = "Error!"
        # Addition
        # if "+" in expr:
        #     num_list = expr.split("+")
        #     answer = 0.0
        #
        #     for num in num_list:
        #         answer += float(num)
        #
        #     self.ids.calc_input.text = str(answer)

        # if "-" in expr:
        #     num_list = expr.split("-")
        #     answer = 0
        #
        #     for num in num_list:
        #         answer -= int(num)
        #
        #     self.ids.calc_input.text = str(answer)
        #
        # if "x" in expr:
        #     num_list = expr.split("x")
        #     answer = 0
        #
        #     for num in num_list:
        #         answer *= int(num)
        #
        #     self.ids.calc_input.text = str(answer)
        #
        # if "/" in expr:
        #     num_list = expr.split("/")
        #     answer = 0.0
        #
        #     for num in num_list:
        #         answer /= float(num)
        #
        #     self.ids.calc_input.text = str(answer)


class CalcApp(App):
    def build(self):
        return CalcLayout()


if __name__ == "__main__":
    CalcApp().run()
