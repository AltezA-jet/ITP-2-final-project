from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *

class Player(FirstPersonController):
    def __init__(self, game, position=(0, 4, 0)):
        super().__init__(position=position)

        self.game = game
        self.spawn_point = Vec3(position)

        # self.crosshair_h = Entity(
        #     parent=camera.ui,
        #     model='quad',
        #     color=color.white,
        #     scale=(0.02, 0.002)
        # )

        # self.crosshair_v = Entity(
        #     parent=camera.ui,
        #     model='quad',
        #     color=color.white,
        #     scale=(0.002, 0.02)
        # )
        # Text(
        #     text='+',
        #     parent=camera.ui,
        #     origin=(0, 0),
        #     scale=2,
        #     color=color.white
        # )
        # self.hit_info = None

    def update(self):
        super().update()

        self.hit_info = raycast(
            origin=camera.world_position,
            direction=camera.forward,
            distance=5,
            ignore=[self]
        )

        if self.y < -100:
            self.respawn()

    def input(self, key):

        if key == 'left mouse down':
            if self.hit_info and self.hit_info.hit:
                destroy(self.hit_info.entity)

        elif key == 'right mouse down':
            if self.hit_info and self.hit_info.hit:
                pos = self.hit_info.entity.position + self.hit_info.normal
                block_class = self.game.get_selected_block()
                block_class(position=pos)

        super().input(key)

    def respawn(self):
        self.position = self.spawn_point
        self.velocity = Vec3(0, 0, 0)