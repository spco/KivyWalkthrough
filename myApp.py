from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainWindow(BoxLayout):
    myString = StringProperty()


class ProtoApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    ProtoApp().run()
