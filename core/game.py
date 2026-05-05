from ui.menu import Menu
from ui.hud import HUD
from core.player import Player
from core.world import World
from ui.hotbar import Hotbar
from core.block import GrassBlock, DirtBlock, StoneBlock


class Game:
    def __init__(self):
        self.state = None

        self.menu = Menu(self)
        self.hud = HUD()
        self.hotbar = Hotbar(self)

        self.player = None
        self.world = None

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
                self.player = Player(position=(5, 4, 5))

            if not self.world:
                self.world = World()

    def get_selected_block(self):
        index = self.hotbar.selected_index

        if index == 0:
            return GrassBlock
        elif index == 1:
            return StoneBlock
        elif index == 2:
            return DirtBlock
        else:
            return GrassBlock