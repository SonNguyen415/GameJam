import pygame
from settings import *
from classes import Character, Boomerang, WALK_SPEED
import math


class Enemy (Character, object):
    def __init__(self, xLoc, yLoc, charImg, objID):
        Character.__init__(self, xLoc, yLoc, charImg, objID)
        self.sightLength = 100
        self.__movementSpeed = WALK_SPEED + 1
        self.agro = False
        self.fiveSec = True

    def sense(self, pxLoc, pyLoc):
        #find distance of npc to player
        distance = math.sqrt(((self.xLoc-pxLoc)**2)+((self.yLoc-pyLoc)**2))
        #find the range of sight
        leftRange = (self.orientation*45)-45
        rightRange = (self.orientation*45)+45
        #find the angle from npc to character
        angle = math.degrees(math.atan2(pyLoc - self.yLoc, pxLoc - self.xLoc))
        #if distance is less than sight length
        if (distance<self.sightLength):
            #if angle is between
            if (angle>leftRange and angle<rightRange):
                self.agro = True


    def move_towards_player(self, xLoc, yLoc):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(xLoc - self.xLoc, yLoc - self.yLoc)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.__movementSpeed)
        self.rect.move_ip(dirvect)

    def whacked(self):
        if self.rect.colliderect(Boomerang.rect):
            self.wounded()

    def random_movement(self, k):
        if k == 1 and self.yLoc + CHAR_HEIGHT <= PLAYGROUND_HEIGHT-PLAYGROUND_Y_OFFSET and self.canMoveDown:
            #Move down
            self.orientation = DOWN
            self.yLoc += self.__movementSpeed
            self.increment_sprite()

        elif k == 2 and PLAYGROUND_Y_OFFSET <= self.yLoc+CHAR_HEIGHT-10 and self.canMoveUp:
            #Move up
            self.orientation = UP
            self.yLoc -= self.__movementSpeed
            self.increment_sprite()

        elif k == 3 and self.xLoc + CHAR_WIDTH <= PLAYGROUND_LENGTH+PLAYGROUND_X_OFFSET and self.canMoveRight:
            #Move right
            self.orientation = RIGHT
            self.xLoc += self.__movementSpeed
            self.increment_sprite()

        elif k == 4 and PLAYGROUND_X_OFFSET <= self.xLoc and self.canMoveLeft:
            #Move left
            self.orientation = LEFT
            self.xLoc -= self.__movementSpeed
            self.increment_sprite()


