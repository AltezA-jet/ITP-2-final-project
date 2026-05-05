from ursina import *
from core.player import *

class HUD(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)

        self.text = Text("Playing...", position=(-0.7, 0.45))

        self.disable()
