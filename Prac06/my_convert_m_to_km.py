"""
CP1404/CP5632 Practical 06
Kivy GUI program to convert miles to kilometres
Oliver Atkinson, IT@JCU
Started 10/04/2017
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
__author__ = 'Oliver Atkinson'


class MilestoKilometresApp(App):
    """ MilestoKilometresApp is a Kivy App for converting Miles to Kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('my_convert_m_to_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value ** 2
        self.root.ids.output_label.text = str(result)


MilestoKilometresApp().run()
