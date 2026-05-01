class Game:
    def __init__(self):
        self.state = "menu"

    def start(self):
        self.state = "playing"

    def game_over(self):
        self.state = "game_over"
