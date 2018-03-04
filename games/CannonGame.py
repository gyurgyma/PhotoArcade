from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.clock import Clock
from img_proc.image_processor import ImageProcessor

from games.Tanks import Tank


class CannonGame(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)
        self.is_waiting = False
        self.vector = [(0, 0), (0, 0)]

        Clock.schedule_interval(self.main_game_loop, 0.5)

        # game objects
        self.collidables = []
        self.tanks = [Tank(x=0, y=0, team=0), Tank(x=200, y=200, team=1)]
        self.image_processor = ImageProcessor("img_proc/frhs.jpg")
        self.image_processor.find_contours()


    def on_touch_down(self, touch):
        if self.is_waiting:
            self.vector[0] = (touch.x, touch.y)

    def on_touch_up(self, touch):
        if self.is_waiting:
            self.vector[1] = (touch.x, touch.y)
            self.is_waiting = False

    def collision(self, terrain):
        pass

    def main_game_loop(self, dt):

        if self.is_waiting:
            pass

        else:

            # move tanks
            self.tanks[0].x += 1
            self.tanks[0].y += 1

            # set wait for input
            if self.tanks[0].x % 10 == 0:
                self.is_waiting = True

            # collision
            terrain = self.image_processor.terrain
            self.collision(terrain)

            # calculate victory
            alive_tanks = []
            for tank in self.tanks:
                if tank.is_alive:
                    alive_tanks.append(tank)

            if len(alive_tanks) == 1:
                self.victory(alive_tanks[0])
            elif len(alive_tanks) == 0:
                self.victory()

        # draw
        self.canvas.clear()
        with self.canvas.before:
            Rectangle(source='assets/AgreeableDeer2.png', pos=self.pos, size=self.size)
        with self.canvas:
            Color(0.5, 0.5, 0.5, 0.5)
            for tank in self.tanks:
                Ellipse(pos=(tank.x, tank.y), size=(100, 100))

    def victory(self, best_tank=None):
        pass
