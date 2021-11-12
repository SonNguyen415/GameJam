import pygame
import math
from constants import *


BOOMERANG_SIZE = 20
BOOMERANG_SPEED = [30, 30]
BOOMERANG_TIME = 100
LOCATION_TOLERANCE = 3
SPEED_TOLERANCE = 2
DECCELERATION = 100



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



    def check_location(self, xSetPoint, ySetPoint, currSpeed):
        if ((xSetPoint - LOCATION_TOLERANCE <= self.__xLoc  <= xSetPoint + LOCATION_TOLERANCE and 
        ySetPoint - LOCATION_TOLERANCE <= self.__yLoc  <= ySetPoint + LOCATION_TOLERANCE) or 
        (-SPEED_TOLERANCE <= currSpeed[0] <= SPEED_TOLERANCE and 
        -SPEED_TOLERANCE <= currSpeed[1] <= SPEED_TOLERANCE)):
            return False
        return True


    def find_a(self, xSetPoint, ySetPoint):
        aX = -xSetPoint/(BOOMERANG_TIME/2)**2
        aY = -ySetPoint/(BOOMERANG_TIME/2)**2
        return [aX, aY]



    def move_boomerang(self, surface, prevSpeed, accel):
        vx = prevSpeed[0] + accel[0]
        vy = prevSpeed[1] + accel[1]
        currSpeed = [vx, vy] 
        self.__xLoc += vx
        self.__yLoc += vy
        self.draw(surface)
        return currSpeed