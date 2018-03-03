from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock


class CannonGame(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)

        button = Button()
        self.number = 0

        button.text = str(self.number)
        button.size_hint_max_x = 1000
        button.size_hint_max_y = 1000

        self.add_widget(button)
        self.button_stuff = Button()
        self.add_widget(self.button_stuff)
        Clock.schedule_interval(self.main_game_loop, 0.5)

    def main_game_loop(self, dt):
        self.number = self.number + 1
        self.button_stuff.text = str(self.number)