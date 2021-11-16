import pygame
from settings import *
import time

WALK_SPEED = 6
SPRINT_SPEED = 12
MAX_STAMINA = 50
STAMINA_RECHARGE_TIME = 3
POS_TOLERANCE = -10



class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, charImg):
         # Call the parent class (Sprite) constructor
        super().__init__()

        self.type = "Character"

        self.xLoc = xLoc
        self.yLoc = yLoc

        # Load the image
        self.sprites = charImg
        self.currSprite = 0
        self.image = self.sprites[DOWN][self.currSprite]

        self.image = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))

        self.rect = self.image.get_rect(topleft=(xLoc, yLoc))


        # Set our transparent color
        self.image.set_colorkey(COLOR_WHITE)

        self.orientation = 0

        # Some character data
        self.__health = 10
        self.alive = True
        self.canMoveUp = True
        self.canMoveDown = True
        self.canMoveLeft = True
        self.canMoveRight = True
        self.movementSpeed = WALK_SPEED

    def draw(self, surface):
        # blit yourself at your current position
        if(self.orientation == UP):
            self.image = self.sprites[UP][self.currSprite]
        if(self.orientation == DOWN):
            self.image = self.sprites[DOWN][self.currSprite]
        if(self.orientation == LEFT):
            self.image = self.sprites[LEFT][self.currSprite]
        if(self.orientation == RIGHT):
            self.image = self.sprites[RIGHT][self.currSprite]

        surface.blit(self.image, (self.xLoc, self.yLoc))

    def wounded(self):
        self.__health -= 1
        if(self.__health == 0):
            self.alive = False

    def increment_sprite(self):
        if(self.currSprite < 2):
            self.currSprite += 1
        else:
            self.currSprite = 0

    def update_rect(self):
        self.rect.update(self.xLoc, self.yLoc, CHAR_WIDTH, CHAR_HEIGHT)

    def check_collision(self, spriteList):
        for eachSprite in spriteList:
            if(self.rect.colliderect(eachSprite.rect)):
                if(POS_TOLERANCE < self.rect.top - eachSprite.rect.bottom <= 0):
                    self.canMoveUp = False
                if(POS_TOLERANCE < eachSprite.rect.top - self.rect.bottom  <= 0):
                    self.canMoveDown = False
                if(POS_TOLERANCE < self.rect.left - eachSprite.rect.right <= 0):
                    self.canMoveLeft = False
                if(POS_TOLERANCE < eachSprite.rect.left - self.rect.right <= 0):
                    self.canMoveRight = False
                return eachSprite
            else:
                self.canMoveRight = True
                self.canMoveLeft = True
                self.canMoveUp = True
                self.canMoveDown = True
        return self


class Player(Character, object):
    def __init__(self, xLoc, yLoc, charImg):
        Character.__init__(self, xLoc, yLoc, charImg)

        self.__staminaRecharge = 0
        self.__stamina = MAX_STAMINA
        self.speaking = False

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and self.yLoc+CHAR_HEIGHT <= PLAYGROUND_HEIGHT+128 and self.canMoveDown:
            self.yLoc += self.movementSpeed
            self.orientation = DOWN
            self.increment_sprite()
        elif key[pygame.K_UP] and 128-CHAR_HEIGHT <= self.yLoc and self.canMoveUp:
            self.yLoc -= self.movementSpeed
            self.orientation = UP
            self.increment_sprite()
        if key[pygame.K_RIGHT] and self.xLoc+CHAR_WIDTH <= PLAYGROUND_LENGTH+148 and self.canMoveRight:
            self.xLoc += self.movementSpeed
            self.orientation = RIGHT
            self.increment_sprite()
        elif key[pygame.K_LEFT] and 148 <= self.xLoc and self.canMoveLeft:
            self.xLoc -= self.movementSpeed
            self.orientation = LEFT
            self.increment_sprite()

        # if key[pygame.K_e] and collidedObject.type == "Artifacts":
        #     self.interact()
        if key[pygame.K_LSHIFT]:
            if(self.__stamina >= 3):
                self.movementSpeed = SPRINT_SPEED
                self.__stamina -= 3
            else:
                self.movementSpeed = WALK_SPEED
        elif (self.__staminaRecharge < STAMINA_RECHARGE_TIME):
            self.__staminaRecharge += 1
        else:
            self.__staminaRecharge = 0
            self.restore_stamina()
       

    def restore_stamina(self):
        if(self.__stamina < MAX_STAMINA):
            self.__stamina += 1

    def spawn_boomerang(self, surface):
        bmrX = self.xLoc + CHAR_WIDTH/2
        bmrY = self.yLoc + CHAR_HEIGHT/2
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
