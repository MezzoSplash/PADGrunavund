import bge
from math import pi

def main():

    cont = bge.logic.getCurrentController()
    player = cont.owner
    ori = player.orientation.to_euler()

    scene = bge.logic.getCurrentScene()

    keyboard = bge.logic.keyboard

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DKEY]:
        ori.z = 1.5*pi
        player.orientation = ori

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.AKEY]:
        ori.z = pi/2
        player.orientation = ori
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]:
        ori.z = 0
        player.orientation = ori
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]:
        ori.z = pi
        player.orientation = ori
main()