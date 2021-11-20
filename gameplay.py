import pygame
from pygame import sprite
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
t = 0

currentArtifacts = [[],[]]



def show_curr_artifact(player):
    for artifact, i in enumerate(currentArtifacts[0]):
        if artifact.rect.colliderect(player.rect):
            player.generate_text()
            if key[pygame.K_e]:
                currentArtifacts[1][i].draw()
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
    if (bmrExist == False and pygame.mouse.get_pressed()[0] and (pygame.time.get_ticks() - ctr) > (WAIT_TIME * 1000)):
        bmr = player.spawn_boomerang(surface)
        bmr.spawn_boomerang(mouse[0], mouse[1], player)
        bmrExist = True
        bmrTime = 0
    elif (bmrExist):
        bmrTime += 1
        bmr.move_boomerang(surface, mouse[0], mouse[1], player, spriteList)
        if bmr.check_finish(bmrTime, surface, player):
            bmrExist = False
            ctr = pygame.time.get_ticks()





def npc_movement(player, npc):
    global npcTimer
    global k
    global t



    if npc.agro == False:
        if npcTimer==10:
            npcTimer = 0
            k = random.randint(1, 5)
        npcTimer += 1
        npc.random_movement(k)
    else:
        npc.move_towards_player(player.xLoc,player.yLoc)
    if npc.agro:
        npc.slaps(player)
        if npc.coolDown:
            t+=1
            if t==15:
                t=0
                npc.coolDown = False



def update_game(player, npc, surface, spriteList):
    npc.sense(player.xLoc, player.yLoc)
    player.check_collision(spriteList)
    npc.check_collision(spriteList)

    player.handle_keys()
    npc_movement(player, npc)
    npc.update_rect()
    player.update_rect()
    for sprite in spriteList:
        sprite.draw(surface)



def get_pause_button():

    return



def run_gameplay(surface, mouse, heartIcons, spriteList):
    playArea = get_playground()

    surface.blit(playArea, (0, 0))

    player = spriteList[0]
    npc = spriteList[1]


    pauseButton = SpriteObject(PLAYGROUND_LENGTH-50, PLAYGROUND_HEIGHT-50, 'Objects/icon.img', 50, 'Graphics')
    pauseButton.draw(surface)

    update_game(player, npc, surface, spriteList)
    #bmr_gameplay(surface, mouse, player, spriteList)


    updateMap(spriteList)
    display(screen)


    for i in range(0, player.health):
        heartIcons[i].draw(surface)

    pygame.draw.rect(surface, (0,203,255), pygame.Rect(15,45,60,15), width=2)
    pygame.draw.rect(surface, (0,203,255), pygame.Rect(15,45,60*player.get_stamina_ratio(),15))
    return "Play"
