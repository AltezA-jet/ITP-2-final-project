from core.block import GrassBlock
from core.block import StoneBlock
from core.block import DirtBlock
class World:
    def __init__(self):
        self.blocks = []
        self.generate_flat_world()

    def generate_flat_world(self):
        # size = 20

        layers=[
            (2,GrassBlock),
            (0,DirtBlock),
            (-2,DirtBlock),
            (-4,StoneBlock),
            (-6,StoneBlock),
            (-8,StoneBlock),
            (-10,StoneBlock),
            (-12,StoneBlock),
            (-14,StoneBlock)
        ]
        for y , block_class in layers:
            for x in range(1,100,5):
                for z in range(1,100,5):
                    block = block_class(position=(x, y, z))
                    self.blocks.append(block)
                    

        # for x in range(size):
        #     for z in range(size):
        #         block = GrassBlock(position=(x, 2, z))
        #         self.blocks.append(block)
                
        # for x in range(size):
        #     for z in range(size):
        #         block = DirtBlock(position=(x, 0, z))
        #         self.blocks.append(block)

        # for x in range(size):
        #     for z in range(size):
        #         block = DirtBlock(position=(x, 1, z))
        #         self.blocks.append(block)

        # for x in range(size):
        #     for z in range(size):
        #         block = StoneBlock(position=(x, -1, z))
        #         self.blocks.append(block)
        #         block = StoneBlock(position=(x, -2, z))
        #         self.blocks.append(block)
        #         block = StoneBlock(position=(x, -3, z))
        #         self.blocks.append(block)
