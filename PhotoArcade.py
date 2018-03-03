from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from games.CannonGame import CannonGame


class PhotoArcadeApp(App):

    def build(self):
        return CannonGame()


if __name__ == '__main__':
    PhotoArcadeApp().run()

