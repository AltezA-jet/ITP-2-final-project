from ursina import *

class Hotbar(Entity):
    def __init__(self, game):
        super().__init__(parent=camera.ui)
        self.game = game

        self.selected_index = 0
        self.slots = []

        self.create_slots()

    def create_slots(self):
        for i in range(5):
            slot = Entity(
                parent=self,
                model='quad',
                color=color.dark_gray,
                scale=(0.08, 0.08),
                x=-0.2 + i * 0.1,
                y=-0.45
            )
            self.slots.append(slot)

        self.update_ui()

    def input(self, key):
        if key in ['1','2','3','4','5']:
            self.selected_index = int(key) - 1
            self.update_ui()

    def update_ui(self):
        for i, slot in enumerate(self.slots):
            slot.color = color.white if i == self.selected_index else color.dark_gray