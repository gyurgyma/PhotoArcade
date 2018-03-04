from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from games.Tanks import Tank


class CannonGame(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)
        self.is_waiting = False
        self.vector = [(0, 0), (0, 0)]

        button = Button()
        self.number = 0

        button.text = str(self.number)
        button.size_hint_max_x = 1000
        button.size_hint_max_y = 1000

        self.add_widget(button)
        self.button_stuff = Button()
        self.add_widget(self.button_stuff)
        Clock.schedule_interval(self.main_game_loop, 0.5)

        self.terrain = None
        self.collidables = []

        self.number_tanks = 2
        self.tanks = [Tank(x=0, y=0, team=0), Tank(x=0, y=0, team=1)]

    def on_touch_down(self, touch):
        if not self.is_waiting:
            self.vector[0] = (touch.x, touch.y)

    def on_touch_up(self, touch):
        if not self.is_waiting:
            self.vector[1] = (touch.x, touch.y)
            self.is_waiting == False


    def collision(self):
        pass

    def main_game_loop(self, dt):
        if self.is_waiting:
            pass
        else:

            self.number = self.number + 1
            if self.number % 10 == 0:
                self.is_waiting = True

            self.button_stuff.text = str(self.number)

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
