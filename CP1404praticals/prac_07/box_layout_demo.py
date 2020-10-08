from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        # print('greet')
        print('test')
        self.root.ids.output_label.text = 'Hello'
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text + " its nice to meet you."

    def clear_all(self):

        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""




BoxLayoutDemo().run()
