from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.clock import Clock


class CannonGame(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)

        button = Button()
        self.number = 0

        self.canvas = Canvas()
        button.text = str(self.number)
        button.size_hint_max_x = 1000
        button.size_hint_max_y = 1000

        self.add_widget(self.canvas)
        Clock.schedule_interval(self.main_game_loop, 0.5)

        self.terrain = None
        self.collidables = []

    def collision(self):
        pass

    def main_game_loop(self, dt):

        self.canvas.clear()

        with self.canvas:
            Color(0.5, 0.5, 0.5, 0.5)


        self.collision()
