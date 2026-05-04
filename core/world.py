from core.block import GrassBlock

class World:
    def __init__(self):
        self.blocks = []
        self.generate_flat_world()

    def generate_flat_world(self):
        size = 10

        for x in range(size):
            for z in range(size):
                block = GrassBlock(position=(x, 0, z))
                self.blocks.append(block)
