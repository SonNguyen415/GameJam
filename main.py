import pygame, sys
from classes import *
from menu import *
import os

PLAYER_START_X = 500
PLAYER_START_Y = 300

clock = pygame.time.Clock()

ctr = 0 
bmrTime = 0
player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_IMG)
npc = Character(PLAYER_START_X + 200, PLAYER_START_Y, PLAYER_IMG)

bmrExist = False
currentScreen = "Main"

spriteList = [npc]

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
        if (ctr <= WAIT_TIME):
            ctr += 1
        PLAY_AREA = pygame.image.load("Map Play Area/W.png").convert_alpha()
        PLAY_AREA = pygame.transform.scale(PLAY_AREA, (WINDOW_LENGTH, WINDOW_HEIGHT))
        screen.blit(PLAY_AREA, (0, 0))
        collidedObject = player.check_collision(spriteList)
        player.handle_keys()
        player.update_rect()

        if (bmrExist == False and pygame.mouse.get_pressed()[0] and ctr > WAIT_TIME):
            bmr = player.spawn_boomerang(screen)
            bmr.spawn_boomerang(mouse, player)
            bmrExist = True
            bmr.returnBoomerang = False
            bmrTime = 0
        elif (bmrExist):
            bmrTime += 1
            bmr.move_boomerang(screen, mouse[0], mouse[1])
            bmrExist = bmr.check_finish(bmrTime, screen, player)
        npc.draw(screen)
        player.draw(screen)

    pygame.display.update()

    clock.tick(25)
