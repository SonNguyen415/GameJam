import pygame, sys
from classes import *
from menu import *
import os
from dungeon_generation import *
from gameplay import *

PLAYER_START_X = 500
PLAYER_START_Y = 300

clock = pygame.time.Clock()


bmrTime = 0 # time boomerang has existed
player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_IMG)
npc = Character(PLAYER_START_X + 200, PLAYER_START_Y, PLAYER_IMG)

bmrExist = False
currentScreen = "Main"

spriteList = [npc]

#-----------#

generate()
generateStats()

#-----------#


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    mouse = pygame.mouse.get_pos()

    # Game states
    if currentScreen == "Main":
        currentScreen = main_menu(currentScreen)
    elif currentScreen == "Credits":
        currentScreen = credit_menu(currentScreen)
    elif currentScreen == "Play":
        currentScreen = run_gameplay(screen, mouse, player, npc, spriteList)

    pygame.display.update()

    clock.tick(20)
