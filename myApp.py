from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class MainWindow(BoxLayout):
    myString = StringProperty()


class ProtoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == "__main__":
    ProtoApp().run()

