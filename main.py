import pygame
from boomerang import *
from characters import Character
from menu import *
import os

PLAYER_START_X = 100
PLAYER_START_Y = 100

clock = pygame.time.Clock()

ctr = 0
bmrTime = 0
player = Character(PLAYER_START_X, PLAYER_START_Y) 
bmrExist = False
currentScreen = "Main"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
       


    screen.fill((100,60,25))
    
    
    mouse = pygame.mouse.get_pos()

    # Game states
    if currentScreen == "Main":
        currentScreen = main_menu()
    elif currentScreen == "Credits":
        currentScreen = credit_menu()
    elif currentScreen == "Play":
        if(ctr <= WAIT_TIME):
            ctr += 1
        screen.fill((255,255,255)) 
        player.handle_keys()

        if(bmrExist == False and pygame.mouse.get_pressed()[0] and ctr > WAIT_TIME):
            bmr = player.spawn_boomerang(screen)
            bmr.spawn_boomerang(mouse, player)
            bmrExist = True
            bmr.returnBoomerang = False
            bmrTime = 0
        elif(bmrExist):
            bmrTime += 1
            bmr.move_boomerang(screen, mouse[0], mouse[1])
            bmrExist = bmr.check_finish(bmrTime, screen, player)
        player.draw(screen) 
    
    pygame.display.update() 

    clock.tick(50)