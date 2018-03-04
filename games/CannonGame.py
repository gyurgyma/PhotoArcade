from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.clock import Clock

from games.Tanks import Tank


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

        self.number_tanks = 2
        self.tanks = [Tank(x=0, y=0, team=0), Tank(x=0, y=0, team=1)]

    def collision(self):
        pass


    def main_game_loop(self, dt):

        self.canvas.clear()

        with self.canvas:
            Color(0.5, 0.5, 0.5, 0.5)


        self.collision()

        alive_tanks = []
        for tank in self.tanks:
            if tank.is_alive:
                alive_tanks.append(tank)

        if len(alive_tanks) == 1:
            self.victory(alive_tanks[0])
        elif len(alive_tanks) == 0:
            self.victory()

    def victory(self, best_tank=None):
        pass
