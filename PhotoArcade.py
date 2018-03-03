from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock



class PhotoArcadeMenu(BoxLayout):
    def __init__(self):
        BoxLayout.__init__(self)
        button = Button()
        button.text = "abcd"
        button.size_hint_max_x = 1000
        button.size_hint_max_y = 1000
        self.add_widget(button)
        self.button_stuff = Button()
        self.add_widget(self.button_stuff)
        Clock.schedule_interval(self.main_game_loop, 0.5)

    def main_game_loop(self, dt):
        self.button_stuff.text = self.button_stuff.text + "1"


class PhotoArcadeApp(App):
    def build(self):
        return PhotoArcadeMenu()


if __name__ == '__main__':
    PhotoArcadeApp().run()