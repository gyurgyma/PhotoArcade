from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import *
from kivy.clock import Clock

from games.Tanks import Tank


class CannonGame(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)

        Clock.schedule_interval(self.main_game_loop, 0.5)

        self.terrain = None
        self.collidables = []

        self.tanks = [Tank(x=0, y=0, team=0), Tank(x=200, y=200, team=1)]

    def collision(self):
        pass

    def main_game_loop(self, dt):

        self.canvas.clear()

        self.tanks[0].x += 1
        self.tanks[0].y += 1

        with self.canvas:
            Color(0.5, 0.5, 0.5, 0.5)
            for tank in self.tanks:
                Ellipse(pos=(tank.x, tank.y), size=(100, 100))


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
