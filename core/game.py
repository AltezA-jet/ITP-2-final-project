from ui.menu import Menu
from ui.hud import HUD
from core.player import Player

class Game:
    def __init__(self):
        self.state = None

        self.menu = Menu(self)
        self.hud = HUD()
        self.player = None

        self.set_state("menu")

    def set_state(self, new_state):
        self.state = new_state

        if new_state == "menu":
            self.menu.enable()
            self.hud.disable()
            if self.player:
                self.player.disable()

        elif new_state == "playing":
            self.menu.disable()
            self.hud.enable()

            if not self.player:
                self.player = Player()
            else:
                self.player.enable()

        elif new_state == "game_over":
            print("Game Over")
