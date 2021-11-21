import pygame, sys
from classes import *
from menu import *
import os
import button
from gameplay import *

PLAYER_START_X = 500
PLAYER_START_Y = 300

clock = pygame.time.Clock()


bmrExistTime = 0 # time boomerang has existed

generate()
generateStats()

playArea = Playground()
player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_IMG, 0)
playArea.spriteList.append(player)
playArea.initialize_doors()

graphics = []
heartIcons = []


pauseMenu = SpriteObject(PLAYGROUND_LENGTH/2, 150, 'Backgrounds/Pause Menu.png', 300, 'Graphics')

for i in range(0, 10):
    heartIcons.append(SpriteObject(20*i+2, 10, 'Objects/heart.png', 25, 'display'))

P_BUTTON = pygame.image.load("Button Icons/Pause.png").convert_alpha()
pauseButton = button.Button(950, 0, P_BUTTON, 2)


graphics.append(heartIcons)
graphics.append([pauseButton, pauseMenu])


bmrExist = False
currentScreen = "Main"


running = True




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    mouse = pygame.mouse.get_pos()



    # Game states
    if currentScreen == "Main":
        currentScreen = main_menu(currentScreen)
    elif currentScreen == "Credits":
        currentScreen = credit_menu(currentScreen)
    elif currentScreen == "Play":
        currentScreen = run_gameplay(screen, mouse, playArea, graphics)
    elif currentScreen == "Victory":
        victory_screen()
    elif currentScreen == "Defeat":
        defeat_screen()

    pygame.display.update()

    clock.tick(FPS)
