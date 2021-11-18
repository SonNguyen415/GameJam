import pygame
from settings import *
import time

playerPosition = [2,2]


class Door(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, charImg, rotation):
        super().__init__()

        self.xLoc = xLoc
        self.yLoc = yLoc

        self.state = 'locked'

        self.sprite = charImg

        self.sprite = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))

        self.rot = rotation

    def draw(self, surface):
        self.sprite = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))
        surface.blit(self.sprite, (xLoc, yLoc))

    def change_position(self):
        if rotation == 'N':
            playerPosition[1] -= 1
        elif rotation == 'S':
            playerPosition[1] += 1
        elif rotation == 'W':
            playerPosition[0] -= 1
        elif rotation == 'E':
            playerPosition[0] += 1
        
