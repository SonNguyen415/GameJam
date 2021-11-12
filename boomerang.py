import pygame
from constants import *

BOOMERANG_DISTANCE = 100
BOOMERANG_SIZE = 20
BOOMERANG_RANGE = 100

class Boomerang(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()
        self.__xLoc = xLoc
        self.__yLoc = yLoc
        

        self.image = pygame.image.load("icon.png")
        self.image = pygame.transform.scale(self.image, (BOOMERANG_SIZE, BOOMERANG_SIZE))
        

    def draw(self, surface):
        surface.blit(self.image, (self.__xLoc, self.__yLoc))

    def move_boomerang(self, surface, xDestination, yDestination):
        if(self.__xLoc == xDestination and self.__yLoc == yDestination):
            return False
        else:
            if(xDestination > self.__xLoc):
                self.__xLoc += 1
            elif(xDestination < self.__xLoc):
                self.__xLoc -= 1
            if(yDestination > self.__yLoc):
                self.__yLoc += 1
            elif(yDestination < self.__yLoc):
                self.__yLoc -= 1
            self.draw(surface)
            return True
            
        