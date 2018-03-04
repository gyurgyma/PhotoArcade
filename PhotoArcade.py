from kivy.app import App

from games.CannonGame import CannonGame
from ui.MainMenu import MainMenu


class PhotoArcadeApp(App):

    def build(self):
        return MainMenu()


if __name__ == '__main__':
    PhotoArcadeApp().run()

