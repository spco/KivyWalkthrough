from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)


class ProtoApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window


if __name__ == "__main__":
    ProtoApp().run()
