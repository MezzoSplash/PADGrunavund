import bge
import bpy

def main():

    cont = bge.logic.getCurrentController()
    player = cont.owner
    
    scene = bge.logic.getCurrentScene()
    potion = scene.objectsInactive['Potion']
    keyboard = bge.logic.keyboard
    mouse = bge.logic.mouse

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DKEY]:
        player.localPosition.x += 0.1

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.AKEY]:
        player.localPosition.x -= 0.1

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]:
        player.localPosition.y += 0.1
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]:
        player.localPosition.y -= 0.1
        
    mouseClick = bge.logic.KX_INPUT_JUST_RELEASED == mouse.events[bge.events.LEFTMOUSE]

    life_time = 120
    
    if mouseClick:
        new_potion = scene.addObject(potion, player, life_time)

main()
