import pygame
from settings import *
from boomerang import Boomerang

MOVEMENT_SPEED = 3
SPRINT_SPEED = 6
MAX_STAMINA = 30
STAMINA_RECHARGE_TIME = 3



class Artifact(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, img):
         # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.xLoc = xLoc
        self.yLoc = yLoc