import pygame
import time
from settings import *


class Boomerang(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()
        self.xLoc = xLoc
        self.yLoc = yLoc

        self.image = pygame.image.load("icon.png")
        self.rect = self.image.get_rect(topleft=(xLoc, yLoc))

        self.image = pygame.transform.scale(self.image, (BOOMERANG_SIZE, BOOMERANG_SIZE))

        self.returnBoomerang = False
        self.currSpeed = []
        self.accel = []

    def draw(self, surface):
        surface.blit(self.image, (self.xLoc, self.yLoc))


    def check_at_set_point(self, xSetPoint, ySetPoint):
        if ((xSetPoint - LOC_TOLERANCE <= self.xLoc <= xSetPoint + LOC_TOLERANCE and 
        ySetPoint - LOC_TOLERANCE <= self.yLoc  <= ySetPoint + LOC_TOLERANCE) or 
        (-SPEED_TOLERANCE <= self.currSpeed[0] <= SPEED_TOLERANCE and 
        -SPEED_TOLERANCE <= self.currSpeed[1] <= SPEED_TOLERANCE)):
            self.returnBoomerang = True


    def check_finish(self, bmrTime, surface, myPlayer):
        if(bmrTime >= BOOMERANG_TIME):
            self.returnBoomerang = False
            self.xLoc = myPlayer.xLoc + CHARACTER_SIZE/2
            self.yLoc = myPlayer.xLoc + CHARACTER_SIZE/2
            self.draw(surface)
            time.sleep(1)
            return False
        return True


    def find_a(self, xSetPoint, ySetPoint, myPlayer):
        x = xSetPoint - (CHARACTER_SIZE/2 + myPlayer.xLoc)
        y = ySetPoint - (CHARACTER_SIZE/2 + myPlayer.yLoc)
        aX = -x/(BOOMERANG_TIME/2)**2
        aY = -y/(BOOMERANG_TIME/2)**2
        return [aX, aY]


    def move_boomerang(self, surface, xSetPoint, ySetPoint):
        vx = self.currSpeed[0] + self.accel[0]
        vy = self.currSpeed[1] + self.accel[1]
        self.currSpeed = [vx, vy] 
        if(self.check_at_set_point(xSetPoint, ySetPoint)):
            self.xLoc -= vx
            self.yLoc -= vy
        else:
            self.xLoc += vx
            self.yLoc += vy
        self.draw(surface) 

    def spawn_boomerang(self, mouse, myPlayer):
        a = self.find_a(mouse[0], mouse[1], myPlayer)
        self.accel = [2*a[0], 2*a[1]]
        self.currSpeed = [-self.accel[0]*BOOMERANG_TIME/2, -self.accel[1]*BOOMERANG_TIME/2]
    
