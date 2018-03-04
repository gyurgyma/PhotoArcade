import math

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
        self.game_objects = []
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

    def calculate_tank_hits(self):
        for tank in self.tanks:
            for other in self.tanks:
                if tank is not other:
                    if math.hypot(tank.shell.x - other.x, tank.shell.y - other.y) < other.radius:
                        tank.destroy()
                        tank.shell.is_in_flight = False


    def collision(self, terrain):
        self.terrain_collision(terrain)

        pass

    def terrain_collision(self, terrain):
        for tank in self.tanks:
            # len(terrain[0]) is len(row) thus how wide the picture is
            # len(terrain) is len(col) thus how high the picture is
            if(self.x < 0 or self.x > len(terrain[0])) or (self.y < 0 or self.y > len(terrain)):
                tank.reset_shell()
                return True
            elif terrain[self.x][terrain[self.y]:
                

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
            self.check_victory()

        # draw
        self.redraw()


    def redraw(self):
        self.canvas.clear()
        with self.canvas.before:
            Rectangle(source='assets/AgreeableDeer2.png', pos=self.pos, size=self.size)
        with self.canvas:
            Color(0.5, 0.5, 0.5, 0.5)
            for tank in self.tanks:
                Ellipse(pos=(tank.x, tank.y), size=(tank.radius, tank.radius))

    def check_victory(self):
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
