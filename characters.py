import pygame
from constants import *
from boomerang import Boomerang

MOVEMENT_SPEED = 3
SPRINT_SPEED = 6
MAX_STAMINA = 30
STAMINA_RECHARGE_TIME = 3


class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = pygame.image.load("player.png")

        # Resizing image
        self.image = pygame.transform.scale(self.image, (CHARACTER_SIZE, CHARACTER_SIZE))
    
        # Set our transparent color
        self.image.set_colorkey(COLOR_WHITE)

        # Some character data
        self.__health = 100
        self.__xLoc = xLoc
        self.__yLoc = yLoc
        self.__staminaRecharge = 0
        self.__movementSpeed = MOVEMENT_SPEED
        self.__stamina = MAX_STAMINA
        self.__bmrTime = 0
        self.__bmrRecharge = 3


    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and self.__yLoc+CHARACTER_SIZE <= 600: 
            self.__yLoc += self.__movementSpeed 
        elif key[pygame.K_UP] and 0 <= self.__yLoc:
            self.__yLoc -= self.__movementSpeed
        if key[pygame.K_RIGHT] and self.__xLoc+CHARACTER_SIZE <= 1000: 
            self.__xLoc += self.__movementSpeed 
        elif key[pygame.K_LEFT] and 0 <= self.__xLoc: 
            self.__xLoc -= self.__movementSpeed 
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

    def interact(self):
        print("Interacting")

    def restore_stamina(self):
        if(self.__stamina < MAX_STAMINA):
            self.__stamina += 1

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.__xLoc, self.__yLoc))

    def wounded(self, damage):
        self.__health -= damage
        if(self.__health == 0):
            pygame.quit()

    def spawn_boomerang(self, surface):
        bmrX = self.__xLoc + CHARACTER_SIZE/2
        bmrY = self.__yLoc + CHARACTER_SIZE/2
        bmr = Boomerang(bmrX, bmrY)
        bmr.draw(surface)
        return bmr

