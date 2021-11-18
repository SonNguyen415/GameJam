import pygame
from settings import *
import time

class Door(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, charImg, rotation):
        super().__init__()

        self.xLoc = xLoc
        self.yLoc = yLoc

        self.sprite = charImg

        self.sprite = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))

        self.rot = rotation

    def draw(self, surface):
        self.sprite = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))
        surface.blit(self.sprite, (xLoc, yLoc))
