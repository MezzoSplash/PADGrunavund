import bge

def main():

    cont = bge.logic.getCurrentController()
    player = cont.owner

    scene = bge.logic.getCurrentScene()
    potion = scene.objectsInactive['Potion']
    level = scene.objects['Level']
    keyboard = bge.logic.keyboard
    mouse = bge.logic.mouse

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DKEY]:
        player.localPosition.x += 0.1

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.AKEY]:
        player.localPosition.x += -0.1

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]:
        player.localPosition.y += 0.1
        
    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]:
        player.localPosition.y -= 0.1

    if bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SPACEKEY]:
        new_object = scene.addObject(Potion, player)

    mouseClick = bge.logic.KX_INPUT_JUST_RELEASED == mouse.events[bge.events.LEFTMOUSE]

    life_time = 40

    if mouseClick:
        scene.addObject(potion, player)

main()