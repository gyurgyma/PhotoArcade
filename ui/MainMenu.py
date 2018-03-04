
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from games.CannonGame import CannonGame


class MainMenu(GridLayout):

    def __init__(self):
        GridLayout.__init__(self)
        self.button = Button(text="Tank Tops")
        self.add_widget(self.button)
        self.button.on_press = self.on_click_tank_tops

    def on_click_tank_tops(self):
        self.add_widget(CannonGame())
