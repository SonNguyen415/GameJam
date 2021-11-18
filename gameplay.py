import pygame
from classes import *
from settings import *
import time
import random
from dungeon_generation import *


bmr = object
bmrExist = False
bmrTime = 0
ctr = 0
npcTimer = 0
k = 1


artifactList = [[],[]]


def show_curr_artifact(player):
    for artifact, i in enumerate(artifactList[0]):
        if artifact.rect.colliderect(player.rect):
            player.generate_text()
            if key[pygame.K_e]:
                artifactList[1][i].draw()
                time.sleep(10)


def get_playground():
    playground = pygame.image.load("Base Room.png").convert_alpha()
    playground = pygame.transform.scale(playground, (WINDOW_LENGTH, WINDOW_HEIGHT))
    return playground



def bmr_gameplay(surface, mouse, player, spriteList):
    global bmrExist
    global bmrTime
    global ctr
    global bmr
    if(ctr <  WAIT_TIME):
        ctr += 1
    if (bmrExist == False and pygame.mouse.get_pressed()[0] and ctr >= WAIT_TIME):
        print(mouse)
        bmr = player.spawn_boomerang(surface)
        bmr.spawn_boomerang(mouse[0], mouse[1], player)
        bmrExist = True
        bmrTime = 0
    elif (bmrExist):
        bmrTime += 1
        bmr.move_boomerang(surface, mouse[0], mouse[1], player, spriteList)
        bmrExist = not bmr.check_finish(bmrTime, surface, player)




def npc_movement(npc):
    global npcTimer
    global k
    if (npcTimer==10):
        npcTimer = 0
        k = random.randint(0, 5)
    npcTimer+=1
    npc.random_movement(k)



def update_game(player, npc, surface, spriteList):
    player.handle_keys()
    npc_movement(npc)
    npc.draw(surface)
    player.draw(surface)
    npc.update_rect()
    player.update_rect()
    player.check_collision(spriteList)
    npc.check_collision(spriteList)


def run_gameplay(surface, mouse, player, npc, heartIcons, spriteList):
    PLAY_AREA = get_playground()

    surface.blit(PLAY_AREA, (0, 0))

    update_game(player, npc, surface, spriteList)
    bmr_gameplay(surface, mouse, player, spriteList)

    generate()
    generateStats()

    updateMap()

    for i in range(0, player.health):
        heartIcons[i].draw(surface)
    return "Play"
