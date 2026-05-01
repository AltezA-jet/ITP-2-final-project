from ursina import Button, color

class Block(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model='cube',
            color=color.green,
            position=position
        )
class GrassBlock(Block):
    pass
