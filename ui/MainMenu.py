
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from games.CannonGame import CannonGame
from kivy.uix.label import Label


class MainMenu(GridLayout):

    def __init__(self):
        GridLayout.__init__(self)
        self.button = Button(text="Tank Tops")
        self.add_widget(self.button)
        self.button.on_press = self.on_click_tank_tops

    def on_click_tank_tops(self):
        self.cannon_game = CannonGame()
        self.cannon_game.victory_callback = self.show_victory
        self.add_widget(self.cannon_game)

    def show_victory(self):
        self.add_widget(Label(text= "Game Over"))
        self.remove_widget(self.cannon_game)
        self.remove_widget(self.button)
