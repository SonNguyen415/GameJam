import pygame
from characters import Character
from menu import *
import os

PLAYER_START_X = 100
PLAYER_START_Y = 100

clock = pygame.time.Clock()


player = Character(PLAYER_START_X, PLAYER_START_Y) 

bmrExist = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and currentScreen == "Main Menu":
           currentScreen = change_menu(mouse, screen)


    screen.fill((100,60,25))
    
    
    mouse = pygame.mouse.get_pos()

    # Game states
    if currentScreen == "Main Menu":
        make_menu(mouse, screen)
    elif currentScreen == "Credits":
        screen.blit(credits , (WIDTH/2,HEIGHT/2))
    elif currentScreen == "Play":
        screen.fill((255,255,255)) 
        player.handle_keys()
        if(bmrExist == False and pygame.mouse.get_pressed()[0]):
            bmr = player.spawn_boomerang(screen)
            xMouse = mouse[0]
            yMouse = mouse[1]
            bmrExist = True
        elif(bmrExist):
            bmrExist = bmr.move_boomerang(screen, xMouse, yMouse)
        player.draw(screen) 
    
    pygame.display.update() 

    clock.tick(50)