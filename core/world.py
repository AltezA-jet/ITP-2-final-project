from core.block import GrassBlock
from core.block import StoneBlock
from core.block import DirtBlock
from core.block import OakBlock
from core.block import GlassBlock
class World:
    def __init__(self):
        self.blocks = []
        self.generate_flat_world()

    def generate_flat_world(self):
        size = 20

        layers=[
            (2,GrassBlock),
            (1,DirtBlock),
            (0,DirtBlock),
            (-1,StoneBlock),
            (-2,StoneBlock),
            (-3,StoneBlock),
            (-4,StoneBlock),
            (-5,StoneBlock),
            (-6,StoneBlock)
        ]
        for y , block_class in layers:
            for x in range(size):
                for z in range(size):
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
