"""
Subject: CP1404

Created a program that can turn miles into km.

Student name: Matthew Ballarino
Student number: 13291475
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * FACTOR_MILES_TO_KM
        self.root.ids.output_label.text = str(result)


    def handle_increment(self, change):

        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()


    #
    # def update_result(self, miles):
    #     self.output_km = str(miles * FACTOR_MILES_TO_KM)
    #
    # @staticmethod
    # def convert_to_number(text):
    #     try:
    #         return float(text)
    #     except ValueError:
    #         return 0.0

