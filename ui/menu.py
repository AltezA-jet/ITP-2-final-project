from ursina import *

class Menu(Entity):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.parent = camera.ui

      
        self.bg = Entity(
            parent=self,
            model='quad',
            scale=(2, 1),
            color=color.black66
        )

       
        self.play_button = Button(
            text="Play",
            parent=self,
            scale=(0.3, 0.1),
            y=0.2
        )
        self.play_button.on_click = self.play

        self.exit_button = Button(
            text="Exit",
            parent=self,
            scale=(0.3, 0.1),
            y=-0.2
        )
        self.exit_button.on_click = application.quit

    def play(self):
        print("PLAY CLICKED")
        self.disable()
        self.game.set_state("playing")
