from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KMS = 1.61


class MilesToKmsConverterApp(App):
    """ Kivy App responsible for converting miles to kilometres """

    def build(self):
        """ Configures the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kms.kv')
        return self.root

    OUTPUT_KMS = StringProperty()

    def handle_increment(self, text, increment):
        """ function to increment values by 1  with up and down buttons"""
        user_input_miles = self.convert_input_to_float(text) + increment
        self.root.ids.input_miles.text = str(user_input_miles)
        self.handle_conversion(user_input_miles)

    def handle_conversion(self, text):
        """ function which converts miles to kilometres"""
        user_input_miles = self.convert_input_to_float(text)
        calculation = user_input_miles * MILES_TO_KMS
        self.OUTPUT_KMS = str(calculation)

    def convert_input_to_float(self, text):
        """grab user text input, covert to float. Float text if input valid and outputs 0 if error."""
        try:
            return float(text)
        except ValueError:
            return 0


MilesToKmsConverterApp().run()
