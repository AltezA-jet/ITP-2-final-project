from ursina import *

class Menu(Entity):
    def __init__(self, game):
        super().__init__(parent=camera.ui)

        self.game = game

        self.play_button = Button(text="Play", y=0.2, on_click=self.play)
        self.settings_button = Button(text="Settings", y=0)
        self.exit_button = Button(text="Exit", y=-0.2, on_click=application.quit)

    def play(self):
        self.game.set_state("playing")
