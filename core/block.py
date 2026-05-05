from ursina import *

class Block(Entity):
    def __init__(self, position=(0,0,0), texture='white_cube'):
        super().__init__(
            model='cube',
            texture=texture,
            position=position,
            collider='box',
            game = None
        )

    # def input(self, key):
    #     if self.hovered:
    #         if key == 'left mouse down':
    #             destroy(self)

    #         if key == 'right mouse down':
    #             block_class = Block.game.get_selected_block()
    #             block_class(position=self.position + mouse.normal)

class GrassBlock(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position=position,
            texture='textures/grass'
        )

class DirtBlock(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position=position,
            texture='textures/dirt'
        )

class StoneBlock(Block):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            position=position,
            texture='textures/stone'
        )