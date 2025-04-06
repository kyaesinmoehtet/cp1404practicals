from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Claire', 'Rebecca', 'Sherry']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name, color=(0, 1, 1, 1))
            temp_label.background_colour = (1, 0.5, 0.5, 1)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()
