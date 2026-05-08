from ursina import *

class Hotbar(Entity):
    def __init__(self, game):
        super().__init__(parent=camera.ui)

        self.game = game
        self.selected_index = 0
        self.slots = []

        self.items = [
            'textures/grass',
            'textures/stone',
            'textures/dirt',
            'textures/planks',
            'textures/glass',
            'textures/dirt',
            'textures/grass',
            'textures/stone',
            'textures/dirt',
            'textures/grass',
        ]

        self.build()

    def build(self):
        start_x = -0.45
        spacing = 0.09

        for i in range(10):

            slot = Button(
                parent=self,
                model='quad',
                texture=self.items[i],
                color=color.gray,
                scale=(0.08, 0.08),
                position=(start_x + i * spacing, -0.45),
                highlight_color=color.light_gray,
                pressed_color=color.white
            )

            slot.frame = Entity(
                parent=slot,
                model='quad',
                color=color.gray,
                scale=1.1,
                z=0.01
            )

            self.slots.append(slot)

        self.update_visual()

    def input(self, key):
        if key.isdigit():
            i = int(key)
            if i == 0:
                i = 9
            else:
                i -= 1

            self.selected_index = i
            self.update_visual()
            
        elif key == 'scroll down':
            self.selected_index += 1
            if self.selected_index > 9:
                self.selected_index = 0
            self.update_visual()

        elif key == 'scroll up':
            self.selected_index -= 1
            if self.selected_index < 0:
                self.selected_index = 9
            self.update_visual()

    def update_visual(self):
        for i, slot in enumerate(self.slots):

            if i == self.selected_index:
                slot.frame.color = color.white
            else:
                slot.frame.color = color.gray
    # def update_selection(self):
    #     for i, slot in enumerate(self.slots):
    #         if i == self.selected_index:
    #             slot.color = color.white
    #         else:
    #             slot.color = color.gray