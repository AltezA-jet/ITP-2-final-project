from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *

class Player(FirstPersonController):
    def __init__(self, game, position=(0, 4, 0)):
        super().__init__(position=position)

        self.game = game
        self.spawn_point = Vec3(position)

        self.crosshair = Entity(
            parent=camera.ui,
            model='quad',
            color=color.white,
            scale=0.01
        )

    def update(self):
        super().update()

        hit_info = raycast(
            origin=camera.world_position,
            direction=camera.forward,
            distance=5
        )

        if hit_info.hit:
            if held_keys['left mouse']:
                destroy(hit_info.entity)

            if held_keys['right mouse']:
                pos = hit_info.entity.position + hit_info.normal
                block_class = self.game.get_selected_block()
                block_class(position=pos)

        if self.y < -100:
            self.respawn()

    def respawn(self):
        self.position = self.spawn_point
        self.velocity = Vec3(0,0,0)