from ursina import Ursina
from ursina import DirectionalLight, AmbientLight
from core.game import Game
from ursina import *



app = Ursina()

DirectionalLight(y=2, z=3, rotation=(45, -45, 45))
AmbientLight(color=color.rgba(120,120,120,0.5))

game = Game()
# window.exit_button.visible = False
app.run()
