import math

from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.label import Label
from img_proc.image_processor import ImageProcessor

import copy

from games.Tanks import Tank


def vector_add(vector1, vector2):
    return [((vector2[0][0] + vector1[0][0]), (vector2[0][1] + vector1[0][1])),
            ((vector2[1][0] + vector1[1][0]), (vector2[1][1] + vector1[1][1]))]



class CannonGame(FloatLayout):
    def __init__(self):

        FloatLayout.__init__(self)
        self.is_waiting = True
        self.vector = [(0, 0), (0, 0)]
        self.gravity_vector = [(0, 0), (0, -1)]
        self.shot_multiplier = 0.5
        self.player_twos_turn = False

        Clock.schedule_interval(self.main_game_loop, 0.5)

        # game objects
        self.image_processor = ImageProcessor("img_proc/frhs.jpg")
        self.image_processor.find_contours()
        self.tanks = []
        self.spawn_tanks(2)

        # set size
        image_x = len(self.image_processor.terrain)
        image_y = len(self.image_processor.terrain[1])
        # #self.size_hint_x = image_x
        # #self.size_hint_y = image_y
        # self.size_hint_max_x= image_x
        # self.size_hint_max_y= image_y
        # self.size_hint_min_x = image_x
        # self.size_hint_min_y = image_y

    def spawn_tanks(self, num_players):
        terrain = self.image_processor.terrain
        terrain_length = len(terrain[0])
        terrain_max_height = len(terrain)
        space = terrain_length / num_players

        #tank_position = 0

        #for ii in range(num_players):
            # tank_kv_position = self.img_to_kv_coord(tank_position, terrain_max_height)
            # self.tanks.append(Tank(x=tank_kv_position[0], y=tank_kv_position[0]))
        self.tanks.append(Tank(x=50, y=terrain_max_height-10))
        self.tanks.append(Tank(x=terrain_length - 50, y=terrain_max_height-10))
        #tank_position += int(space)

    def on_touch_down(self, touch):
        if self.is_waiting:
            self.vector[0] = (int(self.shot_multiplier * touch.x), int(self.shot_multiplier * touch.y))

    def on_touch_up(self, touch):
        if self.is_waiting:
            self.vector[1] = (int( self.shot_multiplier * touch.x), int(self.shot_multiplier * touch.y))
            if self.player_twos_turn:
                self.tanks[1].shoot(self.vector)
                self.player_twos_turn = False
            else:
                self.tanks[0].shoot(self.vector)
                self.player_twos_turn = True
            self.is_waiting = False

    def collision(self, terrain):
        self.terrain_collision(terrain)
        self.shell_tank_collision()
        pass

    def terrain_collision(self, terrain):
        for tank in self.tanks:
            # len(terrain[0]) is len(row) thus how wide the picture is
            # len(terrain) is len(col) thus how high the picture is

            tank_shell_im_coord = self.kv_to_img_coord(tank.shell.x, tank.shell.y)

            if(tank_shell_im_coord[0] < 0 or tank_shell_im_coord[0] > len(terrain[0])) \
                    or (tank_shell_im_coord[1] < 0 or tank_shell_im_coord[1] > len(terrain)):

                tank.reset_shell()
                self.is_waiting = True

            elif tank.shell.is_in_flight and terrain[tank_shell_im_coord[1]][tank_shell_im_coord[0]] :
                self.image_processor.chomp(tank_shell_im_coord, 50)
                print (str(tank.shell.x) + "," + str(tank.shell.y))
                tank.reset_shell()
                self.is_waiting = True

            # check if the tank is sitting on the ground
            tank_im_coord = self.kv_to_img_coord(tank.x, tank.y)
            if not terrain[tank_im_coord[1] + tank.radius][tank_im_coord[0]]:
                # fall "up to" 10 pixels this "tick"
                # for ii in range(self.gravity_vector[1][1] - self.gravity_vector[1][0]):
                for ii in range(13):
                    tank_im_coord = self.kv_to_img_coord(tank.x, tank.y)
                    if not terrain[tank_im_coord[1] + tank.radius][tank_im_coord[0]]:
                        tank.y -= 1
                    else:
                        break

    def shell_tank_collision(self):
        for tank in self.tanks:
            for other in self.tanks:
                # "is not" returns true if memory addresses are different
                if tank is not other:
                    if math.hypot(tank.shell.x - other.x, tank.shell.y - other.y) < other.radius:
                        other.destroy()
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

    def kv_to_img_coord(self, pos_x, pos_y):
        terrain_max_height = len(self.image_processor.terrain)
        return int(pos_x), int(terrain_max_height - pos_y)

    def img_to_kv_coord(self, pos_x, pos_y):
        terrain_max_height = len(self.image_processor.terrain)
        terrain_max_width = len(self.image_processor.terrain[0])
        win_width = self.size[0]
        win_height = self.size[1]

        width_ratio = win_width / terrain_max_width
        height_ratio = win_height / terrain_max_height

        final_width = width_ratio * pos_x
        final_height = height_ratio * (terrain_max_height - pos_y)
        return final_width, final_height

    def update(self):

        for tank in self.tanks:
            if tank.shell.is_in_flight:
                # keep flying along the vector
                tank.shell.x += int(tank.shell.vector[1][0] - tank.shell.vector[0][0])
                tank.shell.y += int(tank.shell.vector[1][1] - tank.shell.vector[0][1])
                tank.shell.vector = vector_add(tank.shell.vector, self.gravity_vector)

    def redraw(self):
        self.canvas.clear()

        # redraw the image
        with self.canvas.before:
            rect = Rectangle(source=self.image_processor.im_name, pos=self.pos, size=(len(self.image_processor.terrain[1]),
                             len(self.image_processor.terrain)))
        # redraw the tanks
        with self.canvas:
            Color(100, 0.5, 0.5, 0.5)
            for tank in self.tanks:
                #Line(circle=(tank.x, tank.y, tank.radius))
                if tank.is_alive:
                    Ellipse(pos=(tank.x - tank.radius, tank.y - tank.radius), size=(tank.radius * 2, tank.radius * 2))

        # redraw the shells
        with self.canvas:
            Color(0.5, 100, 0.5, 0.5)
            for tank in self.tanks:
                if tank.shell.is_in_flight:
                    #Line(circle=(tank.shell.x, tank.shell.y, tank.radius/10))
                    Ellipse(pos=(tank.shell.x - tank.radius/10, tank.shell.y - tank.radius/10), size=(tank.radius/5, tank.radius/5))

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
        # Popup(title="Game Over", content=Label(text='Hello world'),size_hint=(None, None), size=(400, 400))
        self.victory_callback()

        #self.add_widget(Label(text= 'Game Over'))
        pass
