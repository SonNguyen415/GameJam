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




playArea = Playground()
player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_IMG, 0)
playArea.spriteList.append(player)
playArea.updateMap()



graphics = []
heartIcons = []
for i in range(0, 10):
    heartIcons.append(SpriteObject(20*i+2, 10, 'Objects/heart.png', 25, 'display'))

<<<<<<< Updated upstream
P_BUTTON = pygame.image.load("Button Icons/Pause.png").convert_alpha()
pauseButton = startButton = button.Button(50, 100, P_BUTTON, 4)
=======
# pauseButton = startButton = button.Button(50, 100, 'Button Icons/Pause.png', 4)
>>>>>>> Stashed changes


graphics.append(heartIcons)
# graphics.append(pauseButton)


bmrExist = False
currentScreen = "Main"


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
        currentScreen = run_gameplay(screen, mouse, playArea, graphics)


    pygame.display.update()

    clock.tick(FPS)
