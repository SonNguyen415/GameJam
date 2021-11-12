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
        if(ctr <= WAIT_TIME):
            ctr += 1
        screen.fill((255,255,255)) 
        player.handle_keys()
        if(bmrExist == False and pygame.mouse.get_pressed()[0] and ctr > WAIT_TIME):
            bmr = player.spawn_boomerang(screen)
            xMouse = mouse[0]
            yMouse = mouse[1]
            a = bmr.find_a(xMouse, yMouse)
            accel = [2*a[0], 2*a[1]]
            print(accel)
            currSpeed = [-accel[0]*BOOMERANG_TIME/2, -accel[1]*BOOMERANG_TIME/2]
            bmrExist = True
            bmrTime = 0
        elif(bmrExist):
            bmrTime += 1
            currSpeed = bmr.move_boomerang(screen, currSpeed, accel)
            bmrExist = bmr.check_location(xMouse, yMouse, currSpeed)
            if(bmrTime >= BOOMERANG_TIME):
                bmrExist = False
        player.draw(screen) 
    
    pygame.display.update() 

    clock.tick(50)