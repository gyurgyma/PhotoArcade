from kivy.app import App

from games.CannonGame import CannonGame


class PhotoArcadeApp(App):

    def build(self):
        return CannonGame()


if __name__ == '__main__':
    PhotoArcadeApp().run()

