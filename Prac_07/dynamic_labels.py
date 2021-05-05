from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self):
        """Construct main app."""
        super().__init__()
        # data - dictionary of names from Simpsons family :)
        self.character_names = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]

    def build(self):
        """Build and configure the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for character_name in self.character_names:
            print(character_name)
            temp_label = Label(text=character_name)
            self.root.ids.labels_for_names.add_widget(temp_label)


DynamicLabelsApp().run()
