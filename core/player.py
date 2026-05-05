from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Vec3

class Player(FirstPersonController):
    def __init__(self, position=(5, 4, 5)):
        super().__init__(position=position)

        self.spawn_point = Vec3(position)

    def update(self):
        super().update()

        if self.y < -100:
            self.respawn()

    def respawn(self):
        self.position = self.spawn_point