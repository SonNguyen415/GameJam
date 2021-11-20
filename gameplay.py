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


def pause_button():
    global p
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        print('hello')
        p = True


def pause():
    global p
    if p:
        if key[pygame.K_SPACE]:
            p = False
        time.sleep(1)
        print("hello")
        pause()


def run_gameplay(surface, mouse, playArea):
    playArea.draw(surface)

    update_game(surface, playArea)

    # player = spriteList[0]

    # pauseButton = SpriteObject(PLAYGROUND_LENGTH-50, PLAYGROUND_HEIGHT-50, 'Button Icons/pause.png', 50, 'Graphics')
    # pauseButton.draw(surface)

    # bmr_gameplay(surface, mouse, playArea.spriteList)

    display(screen)

    # for i in range(0, player.health):
    #     heartIcons[i].draw(surface)

    pygame.draw.rect(surface, (0, 203, 255), pygame.Rect(15, 45, 60, 15), width=2)
    pygame.draw.rect(surface, (0, 203, 255), pygame.Rect(15, 45, 60 * playArea.spriteList[0].get_stamina_ratio(), 15))
    return "Play"
