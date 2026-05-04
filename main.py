from ursina import *
from core.game import Game
from core.block import Block

app = Ursina()

DirectionalLight(y=2, z=3, rotation=(45, -45, 45))
AmbientLight(color=color.rgba(120,120,120,0.5))

game = Game()

Block.game = game

app.run()