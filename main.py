import pygame
from characters import Character
from menu import *
import os


pygame.init()
clock = pygame.time.Clock()

player = Character(100, 100) 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
           current_screen = change_menu(mouse, screen)

    screen.fill((100,60,25))
    
    mouse = pygame.mouse.get_pos()

    if current_screen == "Main Menu":
        # Credit button
        make_menu(mouse, screen)
    elif current_screen == "Credits":
        screen.blit(credits , (width/2,height/2))

       

     # screen.fill((255,255,255)) 
    # player.handle_keys()
    # player.draw(screen) 
    
    pygame.display.update() 

    clock.tick(50)