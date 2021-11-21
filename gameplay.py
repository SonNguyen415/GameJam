import pygame
from pygame import key
from pygame.mixer import pause
from classes import *
from menu import *
from settings import *
import time
import random
from dungeon_generation import *

bmr = object
bmrExist = False
bmrTime = 0
ctr = 0
maxTime = 1
npcTimer = 1
t = 0
p = False
playing = True

completedArtifacts = []


def bmr_gameplay(surface, mouse, spriteList):
    global bmrExist
    global bmrTime
    global ctr
    global bmr
    player = spriteList[0]

    if (bmrExist == False and pygame.mouse.get_pressed()[0] and (pygame.time.get_ticks() - ctr) > (WAIT_TIME * 1000)):
        bmr = player.spawn_boomerang(surface)
        bmr.spawn_boomerang(mouse[0], mouse[1], player)
        bmrExist = True
        bmrTime = 0
    elif (bmrExist):
        bmrTime += 1
        bmr.move_boomerang(surface, mouse[0], mouse[1], player, spriteList)
        if bmr.check_finish(bmrTime, player):
            bmrExist = False
            ctr = pygame.time.get_ticks()



def npc_movement(player, npc):
    global npcTimer
    global t
    global maxTime

    if npc.agro == False:
        if npcTimer == maxTime:
            npcTimer = 0
            maxTime = random.randint(10, 15)
            npc.randK = random.randint(1,5)
        npcTimer += 1
        npc.random_movement(npc.randK)
    else:
        npc.move_towards_player(player.xLoc, player.yLoc)
    if npc.agro:
        npc.slaps(player)
        if npc.coolDown:
            t += 1
            if t == 15:
                t = 0
                npc.coolDown = False


def activate_description(playArea, player):
    global completedArtifacts
    index = 0
    for i, artifact in enumerate(playArea.currArtifacts[0]):
        if player.currArtifact == artifact:
            index = i
    artDescription = playArea.currArtifacts[1][index]
    if artDescription not in completedArtifacts:
        completedArtifacts.append(artDescription)
    return artDescription


def update_game(surface, playArea, playing, mouse):
    player = playArea.spriteList[0]
    key = pygame.key.get_pressed()
    describeArtifact = False
    for sprite in playArea.spriteList:
        sprite.draw(surface)
        if sprite.type == 'player' and sprite.check_collision(playArea) and key[pygame.K_e]:
            artDescription = activate_description(playArea, sprite)
            describeArtifact = True
        elif (sprite.type == 'player' or sprite.type == 'npc') and playing:
            sprite.check_collision(playArea)
            if sprite.type == 'npc':
                sprite.sense(player.xLoc, player.yLoc, playArea.spriteList)
            if sprite.type == 'player':
                sprite.handle_keys()
                bmr_gameplay(surface, mouse, playArea.spriteList)
            else:
                npc_movement(player, sprite)
            sprite.update_rect()
    if describeArtifact == True:
        artDescription.draw(surface)

def check_door(spriteList):
    for i in range(0, len(spriteList)):
        if spriteList[i].type == "npc":
            return
    for j in range(0, len(spriteList)):
        if spriteList[j].type == "door":
            spriteList[j].unlocked = True


def check_living(spriteList):
    currIndex = 0
    while currIndex < len(spriteList):
        sprite = spriteList[currIndex]
        if (sprite.type == 'player' or sprite.type == 'npc') and sprite.health == 0:
            spriteList.pop(currIndex)
        else:
            currIndex += 1








def run_gameplay(surface, mouse, playArea, graphics):
    global playing

    spriteList = playArea.spriteList

    playArea.draw(surface)


    if graphics[1][0].draw(surface):
        playing = False

    check_door(spriteList)
    check_living(spriteList)

    for artifact in playArea.currArtifacts[0]:
        artifact.draw(surface)

    update_game(surface, playArea, playing, mouse)

    if (len(spriteList) > 0 and spriteList[0].type != 'player') or len(spriteList) <= 0:
        return "Defeat"
    elif len(completedArtifacts) > 5:
        return "Victory"

    for i in range(0, spriteList[0].health):
        graphics[0][i].draw(surface)

    pygame.draw.rect(surface, COLOR_STAMINA, pygame.Rect(15, 45, 60, 15), width=2)
    pygame.draw.rect(surface, COLOR_STAMINA, pygame.Rect(15, 45, 60 * playArea.spriteList[0].get_stamina_ratio(), 15))

    if not playing:
        graphics[1][1].draw(surface)
        playing = pause_menu()

    display(surface)

    return "Play"


