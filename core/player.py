from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self, position=(0, 2, 0)):
        super().__init__(position=position)