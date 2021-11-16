import pygame
from settings import *
import time
from classes import Character, Boomerang, WALK_SPEED
import math 


class Enemy (Character):
    def __init__(self, xLoc, yLoc, charImg):
        Character.__init__(self, xLoc, yLoc, charImg)
        self.sightLength = 100
        self.sight_width
        self.orientation
        self.__movementSpeed = WALK_SPEED + 1

    def draw(self, surface):
        surface.blit(self.image, (self.xLoc, self.yLoc))

    def sense(self, pxLoc, pyLoc, orientation):
        #find distance of npc to player
        distance = math.sqrt(((self.xLoc-pxLoc)**2)+((self.yLoc-pyLoc)**2))
        #find the range of sight
        leftRange = (orientation*45)-45
        rightRange = (orientation*45)+45
        #find the angle from npc to character
        angle = math.degrees(math.atan2(pyLoc - self.yLoc, pxLoc - self.xLoc))
        #if distance is less than sight length
        if (distance<self.sightLength):
            #if angle is between
            if (angle>leftRange and angle<rightRange):
                self.move_towards_player(pxLoc,pyLoc)

    def move_towards_player(self, xLoc, yLoc):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(xLoc - self.xLoc, yLoc - self.yLoc)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.__movementSpeed)
        self.rect.move_ip(dirvect)

    def smacked (self):
        if self.rect.colliderect(Boomerang):
            self.wounded()

    def random_movement(self):
        k = math.randint(0, 8)
        if k == 1 and self.yLoc + CHARACTER_SIZE <= 600 and self.canMoveUp:
            #Move up
            self.orientation = 0
            i = 5
            while i < 5 and self.yLoc + CHARACTER_SIZE <= 600 and self.canMoveUp:
                self.yLoc += self.__movementSpeed
                i+=1
        elif k == 2 and 0 <= self.yLoc and self.canMoveDown:
            #Move down
            self.orientation = 4
            i = 5
            while i < 5 and 0 <= self.yLoc and self.canMoveDown:
                self.yLoc -= self.__movementSpeed
                i+=1
        elif k == 3 and self.xLoc + CHARACTER_SIZE <= 1000 and self.canMoveRight:
            #Move right
            self.orientation = 2
            i = 5
            while i < 5 and self.xLoc + CHARACTER_SIZE <= 1000 and self.canMoveRight:
                self.xLoc += self.__movementSpeed
                i+=1
        elif k == 4 and 0 <= self.xLoc and self.canMoveLeft:
            #Move left
            self.orientation = 6
            i = 5
            while i < 5 and 0 <= self.xLoc and self.canMoveLeft:
                self.xLoc -= self.__movementSpeed
                i+=1
        elif k == 5 and self.yLoc + CHARACTER_SIZE <= 600 and self.canMoveUp and 0 <= self.xLoc and self.canMoveLeft:
            #Move top-left
            self.orientation = 7
            i = 5
            while i < 5 and self.yLoc + CHARACTER_SIZE <= 600 and self.canMoveUp and 0 <= self.xLoc and self.canMoveLeft:
                self.yLoc += (self.__movementSpeed*(math.sqrt(2)/2))
                self.xLoc -= (self.__movementSpeed*(math.sqrt(2)/2))
                i += 1
        elif k == 6 and self.yLoc + CHARACTER_SIZE <= 600 and self.canMoveUp and self.xLoc + CHARACTER_SIZE <= 1000 and self.canMoveRight:
            #Move top-right
            self. orientation = 1
            i = 5
            while i < 5 and self.yLoc + CHARACTER_SIZE <= 600 and self.canMoveUp and self.xLoc + CHARACTER_SIZE <= 1000 and self.canMoveRight:
                self.yLoc += (self.__movementSpeed*(math.sqrt(2)/2))
                self.xLoc += (self.__movementSpeed*(math.sqrt(2)/2))
                i += 1
        elif k == 7 and 0 <= self.yLoc and self.canMoveDown and 0 <= self.xLoc and self.canMoveLeft:
            #Move bottom-left
            self.orientation = 5
            i = 5
            while i < 5 and 0 <= self.yLoc and self.canMoveDown and 0 <= self.xLoc and self.canMoveLeft:
                self.yLoc -= (self.__movementSpeed*(math.sqrt(2)/2))
                self.xLoc -= (self.__movementSpeed*(math.sqrt(2)/2))
                i += 1
        elif k == 8 and 0 <= self.yLoc and self.canMoveDown and self.xLoc + CHARACTER_SIZE <= 1000 and self.canMoveRight:
            #Move bottom-right
            self.orientation = 3
            i = 5
            while i < 5 and 0 <= self.yLoc and self.canMoveDown and self.xLoc + CHARACTER_SIZE <= 1000 and self.canMoveRight:
                self.yLoc -= (self.__movementSpeed*(math.sqrt(2)/2))
                self.xLoc += (self.__movementSpeed*(math.sqrt(2)/2))
                i += 1
        elif k == 0:
            sleep(5)