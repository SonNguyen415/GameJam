import pygame
from characters import Character
import os


pygame.init()
screen = pygame.display.set_mode((640, 400))

player = Character(100, 100) 
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            running = False

    player.handle_keys()

    screen.fill((255,255,255)) 
    player.draw(screen) 
    pygame.display.update() 

    clock.tick(10)