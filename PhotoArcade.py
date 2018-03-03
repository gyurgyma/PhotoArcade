from kivy.properties import NumericProperty

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import *

class PhotoArcadeMenu(Widget):
    count = NumericProperty(0)


    def __init__(self):
        Widget.__init__(self)
        Clock.schedule_interval(self.main_loop, 0.05)

    def main_loop(self, deltaTime):
        self.count = self.count + 1


class PhotoArcadeApp(App):
    def build(self):
        return PhotoArcadeMenu()


if __name__ == '__main__':
    PhotoArcadeApp().run()