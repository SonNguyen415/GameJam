from pygame.locals import *
import pygame
import glob

pygame.init()


map1 ="""                             
                             
wwwww  www   www  ww   ww  ww
w             w             w
w                           w
w    wwwwww    wwwww      www
www    w                  w w
w      w          w         w
w   wwwww     wwwwwww      ww
w      wwwwww     w     w   w
w    w      w   www  wwww   w
w      w          w     w   w
w   wwwwww www wwww     w   w
w     w              ww w   w
w                           w
wwwwwwwwwwwwwwwwwwwwwwwwwwwww"""


def init_display():
    global screen, tile
    screen = pygame.display.set_mode((462, 256))
    tile = pygame.image.load("imgs\\tiles\\wall.png")


def tiles(map1):
    global tile
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == "w":
                screen.blit(tile, (x * 16, y * 16))


map1 = map1.splitlines()
pygame.init()
init_display()
loop = 1
while loop:

    # screen.fill((0, 0, 0))
    tiles(map1)
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0

    pygame.display.update()
pygame.quit()












#screen = pygame.display.set_mode((800, 600))

#running = True 
#while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False