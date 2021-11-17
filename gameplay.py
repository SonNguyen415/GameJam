import pygame
from classes import *
from settings import *

bmr = object
bmrExist = False
bmrTime = 0
ctr = 0



def get_playground():
    playground = pygame.image.load("Map Play Area/W.png").convert_alpha()
    playground = pygame.transform.scale(playground, (WINDOW_LENGTH, WINDOW_HEIGHT))
    return playground



def bmr_gameplay(surface, mouse, player):
    global bmrExist
    global bmrTime
    global ctr
    global bmr
    if(ctr <  WAIT_TIME):
        ctr += 1
    if (bmrExist == False and pygame.mouse.get_pressed()[0] and ctr >= WAIT_TIME):
        bmr = player.spawn_boomerang(surface)
        bmr.spawn_boomerang(mouse[0], mouse[1], player)
        bmrExist = True
        bmrTime = 0
    elif (bmrExist):
        bmrTime += 1
        bmr.move_boomerang(surface, mouse[0], mouse[1], player)
        bmrExist = not bmr.check_finish(bmrTime, surface, player)




def run_gameplay(surface, mouse, player, npc, spriteList):

    PLAY_AREA = get_playground()

    surface.blit(PLAY_AREA, (0, 0))
    collidedObject = player.check_collision(spriteList)
    player.handle_keys()
    player.update_rect()

    bmr_gameplay(surface, mouse, player)

    npc.draw(surface)
    player.draw(surface)
    return "Play"
