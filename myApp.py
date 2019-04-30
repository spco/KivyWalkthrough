from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class MainWindow(BoxLayout):
    text_colour = ObjectProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)


class ProtoApp(App):
    def build(self):
        main_window = MainWindow()
        print(self)
        return main_window


if __name__ == "__main__":
    ProtoApp().run()
