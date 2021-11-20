import pygame
from pygame import sprite
from pygame.mixer import pause
from classes import *
from menu import pause_menu
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
p = False

currentArtifacts = [[], []]

def show_curr_artifact(player):
    for artifact, i in enumerate(currentArtifacts[0]):
        if artifact.rect.colliderect(player.rect):
            player.generate_text()
            if key[pygame.K_e]:
                currentArtifacts[1][i].draw()
                time.sleep(10)


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
        if bmr.check_finish(bmrTime, surface, player):
            bmrExist = False
            ctr = pygame.time.get_ticks()


def npc_movement(player, npc):
    global npcTimer
    global k
    global t

    if npc.agro == False:
        if npcTimer == 10:
            npcTimer = 0
            k = random.randint(1, 5)
        npcTimer += 1
        npc.random_movement(k)
    else:
        npc.move_towards_player(player.xLoc, player.yLoc)
    if npc.agro:
        npc.slaps(player)
        if npc.coolDown:
            t += 1
            if t == 15:
                t = 0
                npc.coolDown = False


def update_game(surface, playArea):
    player = playArea.spriteList[0]
    for sprite in playArea.spriteList:
        if sprite.type == 'player' or sprite.type == 'npc':
            if sprite == 'npc':
                sprite.sense(player.xLoc, player.yLoc)
            sprite.check_collision(playArea)
            sprite.move()
            sprite.update_rect()
        sprite.draw(surface)


def check_door(spriteList):
    for i in range(5, len(spriteList)):
        if spriteList[i].type == "npc":
            return
    for j in range(1, 4):
        spriteList[j].unlocked = True






def run_gameplay(surface, mouse, playArea, graphics):
    playArea.draw(surface)
    check_door(playArea.spriteList)

    update_game(surface, playArea)

    # player = spriteList[0]

    graphics[1].draw()

    if graphics[1].draw(surface):
        pauseMenu = SpriteObject(300, 200, 'Background/Pause Menu.png', 300, 'Graphics')
        pause_menu(pauseMenu)

    # bmr_gameplay(surface, mouse, playArea.spriteList)

    display(surface)

    # for i in range(0, player.health):
    #     heartIcons[i].draw(surface)

    pygame.draw.rect(surface, (0, 203, 255), pygame.Rect(15, 45, 60, 15), width=2)
    pygame.draw.rect(surface, (0, 203, 255), pygame.Rect(15, 45, 60 * playArea.spriteList[0].get_stamina_ratio(), 15))
    return "Play"
