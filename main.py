import pygame, sys
from classes import *
from menu import *
import os
from gameplay import *

PLAYER_START_X = 500
PLAYER_START_Y = 300

clock = pygame.time.Clock()


bmrExistTime = 0 # time boomerang has existed
player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_IMG, 0)
npc = Enemy(PLAYER_START_X + 200, PLAYER_START_Y, PLAYER_IMG, 1)
rock = SpriteObject(PLAYER_START_X - 200, PLAYER_START_Y, ROCK_IMG, 30, 'obstacle')

heartIcons = []

for i in range(0, 10):
    heartIcons.append(SpriteObject(20*i+2, 10, 'Objects/heart.png', 25, 'display'))

bmrExist = False
currentScreen = "Main"

spriteList = [player, npc, rock]


running = True

generate()
generateStats()


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
        currentScreen = run_gameplay(screen, mouse, heartIcons, spriteList)


    pygame.display.update()

    clock.tick(FPS)
