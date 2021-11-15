import pygame
from settings import *
import time

MOVEMENT_SPEED = 6
SPRINT_SPEED = 12
MAX_STAMINA = 50
STAMINA_RECHARGE_TIME = 3
POS_TOLERANCE = 1




class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, charImg):
         # Call the parent class (Sprite) constructor
        super().__init__()

        self.xLoc = xLoc
        self.yLoc = yLoc

        # Load the image
        self.image = pygame.image.load(charImg)

        self.image = pygame.transform.scale(self.image, (CHARACTER_SIZE, CHARACTER_SIZE))

        self.rect = self.image.get_rect(topleft=(xLoc, yLoc))


        # Set our transparent color
        self.image.set_colorkey(COLOR_WHITE)

        # Some character data
        self.__health = 10
        self.alive = True
        self.__movementSpeed = MOVEMENT_SPEED

        self.canMoveUp = True
        self.canMoveDown = True
        self.canMoveLeft = True
        self.canMoveRight = True

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.xLoc, self.yLoc))

    def wounded(self):
        self.__health -= 1
        if(self.__health == 0):
            self.alive = False

    def check_collision(self, spriteList):
        for eachSprite in spriteList:
            if(self.rect.colliderect(eachSprite.rect)):
                if(0 < self.rect.top - eachSprite.rect.bottom < POS_TOLERANCE):
                    self.canMoveUp = False
                else:
                    self.canMoveUp = True
                if(0 < eachSprite.rect.top - self.rect.bottom  < POS_TOLERANCE):
                    self.canMoveDown = False
                else:
                    self.canMoveDown = True
                if(0 < self.rect.left - eachSprite.rect.right < POS_TOLERANCE):
                    self.canMoveLeft = False
                else:
                    self.canMoveLeft = False
                if(0 < eachSprite.rect.left - self.rect.right < POS_TOLERANCE):
                    self.canMoveLeft = False
                else:
                    self.canMoveLeft = False



class Player(Character):
    def __init__(self, xLoc, yLoc, charImg):
        Character.__init__(self, xLoc, yLoc, charImg)

        self.__staminaRecharge = 0
        self.__stamina = MAX_STAMINA
        self.__bmrTime = 0
        self.__bmrRecharge = 3
        self.speaking = False

        self.__movementSpeed = MOVEMENT_SPEED

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and self.yLoc+CHARACTER_SIZE <= 600 and self.canMoveDown:
            self.yLoc += self.__movementSpeed
        elif key[pygame.K_UP] and 0 <= self.yLoc and self.canMoveUp:
            self.yLoc -= self.__movementSpeed
        if key[pygame.K_RIGHT] and self.xLoc+CHARACTER_SIZE <= 1000 and self.canMoveRight:
            self.xLoc += self.__movementSpeed
        elif key[pygame.K_LEFT] and 0 <= self.xLoc and self.canMoveLeft:
            self.xLoc -= self.__movementSpeed
        if key[pygame.K_e]:
            self.interact()
        if key[pygame.K_LSHIFT]:
            if(self.__stamina >= 3):
                self.__movementSpeed = SPRINT_SPEED
                self.__stamina -= 3
            else:
                self.__movementSpeed = MOVEMENT_SPEED
        elif (self.__staminaRecharge < STAMINA_RECHARGE_TIME):
            self.__staminaRecharge += 1
        else:
            self.__staminaRecharge = 0
            self.restore_stamina()

    def restore_stamina(self):
        if(self.__stamina < MAX_STAMINA):
            self.__stamina += 1

    def spawn_boomerang(self, surface):
        bmrX = self.xLoc + CHARACTER_SIZE/2
        bmrY = self.yLoc + CHARACTER_SIZE/2
        bmr = Boomerang(bmrX, bmrY)
        bmr.draw(surface)
        return bmr

    def interact(self, object, isArtifact):
        if(self.check_collision(object)):
            self.speaking = True




class Boomerang(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        self.xLoc = xLoc
        self.yLoc = yLoc

        self.image = pygame.image.load("icon.png")
        self.image = pygame.transform.scale(self.image, (BOOMERANG_SIZE, BOOMERANG_SIZE))

        self.rect = self.image.get_rect(topleft=(xLoc, yLoc))


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
            self.xLoc = myPlayer.xLoc
            self.yLoc = myPlayer.yLoc
            self.draw(surface)
            time.sleep(0.01)
            return False
        return True


    def find_a(self, xSetPoint, ySetPoint, myPlayer):
        x = xSetPoint - myPlayer.xLoc
        y = ySetPoint - myPlayer.yLoc
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
