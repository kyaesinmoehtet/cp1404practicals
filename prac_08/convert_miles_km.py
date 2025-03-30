from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        try:
            value = float(self.root.ids.input_miles.text)
            self.root.ids.output_miles.text = str(value * MILES_TO_KM)
        except ValueError:
            self.root.ids.output_miles.text = "0.0"

    def handle_increment(self, change):
        try:
            value = float(self.root.ids.input_miles.text) + change
        except ValueError:
            value = "0.0"
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

MilesConverterApp().run()