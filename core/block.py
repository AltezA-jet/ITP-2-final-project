# from ursina import Button, color
from ursina import *

class Block(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            texture='textures/grass',
            position=position,
            collider='box',
            texture_scale=(1,1)
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)

            if key == 'right mouse down':
                Block(position=self.position + mouse.normal)
class GrassBlock(Block):
    pass
