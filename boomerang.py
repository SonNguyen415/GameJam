import pygame
import math
from constants import *


BOOMERANG_SIZE = 20
BOOMERANG_SPEED = [30, 30]
LOCATION_TOLERANCE = 3
SPEED_TOLERANCE = 2
DECCELERATION = 3
kP = 200



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



    def move_boomerang(self, surface, xSetPoint, ySetPoint, currSpeed):
        dx = xSetPoint - self.__xLoc
        dy = ySetPoint - self.__yLoc
        distance = math.sqrt(dx**2 + dy**2)
        x_deccel = DECCELERATION * dx/abs(dx)
        y_deccel = DECCELERATION * dy/abs(dy)
        vx = currSpeed[0] - x_deccel * kP/distance 
        vy = currSpeed[1] - y_deccel * kP/distance 
        currSpeed = [vx, vy] 
        print(vx)
        self.__xLoc += vx
        self.__yLoc += vy
        self.draw(surface)
        return currSpeed
