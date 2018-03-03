from kivy.app import App
from kivy.uix.widget import Widget


class PhotoArcadeMenu(Widget):
    pass


class PhotoArcadeApp(App):
    def build(self):
        return PhotoArcadeMenu()


if __name__ == '__main__':
    PhotoArcadeApp().run()