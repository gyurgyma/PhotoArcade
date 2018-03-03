from kivy.app import App
from kivy.uix.widget import Widget


class PhotoArcadeMainMenu(Widget):
    pass


class PhotoArcadeApp(App):
    def build(self):
        return PhotoArcadeMainMenu()


if __name__ == '__main__':
    PhotoArcadeApp().run()
