import math

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.clock import Clock
from img_proc.image_processor import ImageProcessor

from games.Tanks import Tank


def vector_add(vector1, vector2):
    return [((vector2[0][0] - vector1[0][0]), (vector2[0][1] - vector1[0][1])),
            ((vector2[1][0] - vector1[1][0]), (vector2[1][1] - vector1[1][1]))]


class CannonGame(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)
        self.is_waiting = True
        self.vector = [(0, 0), (0, 0)]
        self.gravity_vector = [(0, 0), (0, -10)]

        Clock.schedule_interval(self.main_game_loop, 0.5)

        # game objects
        self.image_processor = ImageProcessor("img_proc/frhs.jpg")
        self.image_processor.find_contours()
        self.tanks = []
        self.spawn_tanks(2)

    def spawn_tanks(self, num_players):
        terrain = self.image_processor.terrain
        terrain_length = len(terrain[0])
        terrain_max_height = len(terrain)
        space = terrain_length / num_players

        tank_position = 0
        for ii in range(num_players):
            self.tanks.append(Tank(x=int(tank_position), y=terrain_max_height))
            tank_position += space

    def on_touch_down(self, touch):
        if self.is_waiting:
            self.vector[0] = (touch.x, touch.y)

    def on_touch_up(self, touch):
        if self.is_waiting:
            self.vector[1] = (touch.x, touch.y)
            self.tanks[0].shoot(self.vector)
            self.is_waiting = False

    def collision(self, terrain):
        self.terrain_collision(terrain)
        self.shell_tank_collision()
        pass

    def terrain_collision(self, terrain):
        for tank in self.tanks:
            # len(terrain[0]) is len(row) thus how wide the picture is
            # len(terrain) is len(col) thus how high the picture is
            if(tank.shell.x < 0 or tank.shell.x > len(terrain[0])) or (tank.shell.y < 0 or tank.shell.y > len(terrain)):
                tank.reset_shell()
                self.is_waiting = True
            elif terrain[int(tank.shell.x)][int(tank.shell.y)] and tank.shell.is_in_flight:
                self.image_processor.chomp((tank.shell.x, tank.shell.y), 50)
                tank.reset_shell()
                self.is_waiting = True

            # check if the tank is sitting on the ground
            if not terrain[tank.x][tank.y - tank.radius]:
                # fall "up to" 10 pixels this "tick"
                for ii in range(self.gravity_vector[1][1] - self.gravity_vector[1][0]):
                    if not terrain[tank.x][tank.y - 1]:
                        tank.y -= 1
                    else:
                        break

    def shell_tank_collision(self):
        for tank in self.tanks:
            for other in self.tanks:
                # "is not" returns true if memory addresses are different
                if tank is not other:
                    if math.hypot(tank.shell.x - other.x, tank.shell.y - other.y) < other.radius:
                        tank.destroy()
                        tank.reset_shell()
                        self.is_waiting = True

    def main_game_loop(self, dt):
        if not self.is_waiting:
            # move tanks and move shells
            self.update()

            # collision
            terrain = self.image_processor.terrain
            self.collision(terrain)

            # calculate victory
            self.check_victory()

        # draw
        self.redraw()

    def update(self):
        for tank in self.tanks:
            # keep flying along the vector
            tank.shell.x += tank.shell.vector[1][0] - tank.shell.vector[0][0]
            tank.shell.y += tank.shell.vector[1][1] - tank.shell.vector[0][1]
            tank.shell.vector = vector_add(tank.shell.vector, self.gravity_vector)

    def redraw(self):
        self.canvas.clear()

        # redraw the image
        with self.canvas.before:
            Rectangle(source='img_proc/frhs.jpg', pos=self.pos, size=self.size)

        # redraw the tanks
        with self.canvas:
            Color(0.5, 0.5, 0.5, 0.5)
            for tank in self.tanks:
                Line(circle=(tank.x, tank.y, tank.radius))
                #Ellipse(pos=(tank.x - tank.radius/2, tank.y - tank.radius/2), size=(tank.radius, tank.radius))

        # redraw the shells
        with self.canvas:
            Color(0.5, 10, 0.5, 0.5)
            for tank in self.tanks:
                Line(circle=(tank.shell.x, tank.shell.y, tank.radius/10))
                #Ellipse(pos=(tank.shell.x - tank.radius/20, tank.shell.y - tank.radius/20), size=(tank.radius/10, tank.radius/10))

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
