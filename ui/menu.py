from ursina import Button, application

class Menu:
    def __init__(self, game):
        self.game = game

        self.play_btn = Button(text="Play", on_click=self.play)
        self.exit_btn = Button(text="Exit", y=-0.2, on_click=application.quit)

    def play(self):
        self.game.start()
