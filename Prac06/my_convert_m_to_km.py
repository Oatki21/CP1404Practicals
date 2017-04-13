from kivy.app import App
from kivy.lang import Builder

__author__ = 'Oliver Atkinson'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Opens the class through Kivvy's Parent App Object"""

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('my_convert_m_to_km.kv')
        return self.root

    def handle_calculate(self):
        """Passes value through separate function before calculating and
         printing result on label"""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Associated with Up/Down Buttons, a value is passed depending on the button
        before being applied to currently value in textbox"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """If value passed in isn't compatible as a float type, return 0"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
