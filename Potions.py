import bge


def main():

    cont = bge.logic.getCurrentController()
    player = cont.owner
    mouse = cont.sensors["Mouse"]
    if mouse.positive:
        bge.logic.getCurrentScene().addObject("potion",player,200)
    
main()