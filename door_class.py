import pygame
from settings import *
import time
from dungeon_generation import playerPosition


class Objects(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, objImg, rotation):
        super().__init__()

        self.xLoc = xLoc
        self.yLoc = yLoc

        self.state = 'locked'

        self.image  = objImg

        self.image = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))

        self.rot = rotation

    def draw(self, surface):
        surface.blit(self.image, (self.xLoc, self.yLoc))


    def change_position(self):
        if self.rot == 'N':
            playerPosition[1] -= 1
        elif self.rot == 'S':
            playerPosition[1] += 1
        elif self.rot == 'W':
            playerPosition[0] -= 1
        elif self.rot == 'E':
            playerPosition[0] += 1
