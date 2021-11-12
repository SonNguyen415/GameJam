import pygame
from settings import *
from boomerang import Boomerang

MOVEMENT_SPEED = 4
SPRINT_SPEED = 8
MAX_STAMINA = 50
STAMINA_RECHARGE_TIME = 3



def draw_speech_bubble(screen, text, textColor, bgColor, pos, size):
    font = pygame.font.SysFont(None, 12)
    textSurface = font.render(text, True, textColor)
    textRect = textSurface.get_rect(midbottom=pos)

    # background
    bgRect = textRect.copy()
    bgRect.inflate_ip(10, 10)

    # Frame
    frameRect = bgRect.copy()
    frameRect.inflate_ip(4, 4)

    pygame.draw.rect(screen, textColor, frameRect)
    pygame.draw.rect(screen, bgColor, bgRect)
    screen.blit(textSurface, textRect)



class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        self.xLoc = xLoc
        self.yLoc = yLoc

        # Load the image
        self.image = pygame.image.load("player.png")
        
        self.image = pygame.transform.scale(self.image, (CHARACTER_SIZE, CHARACTER_SIZE))

        self.rect = self.image.get_rect(center=(xLoc, yLoc))

    
        # Set our transparent color
        self.image.set_colorkey(COLOR_WHITE)

        # Some character data
        self.__health = 10
        # self.xLoc = xLoc
        # self.yLoc = yLoc
        self.__staminaRecharge = 0
        self.__movementSpeed = MOVEMENT_SPEED
        self.__stamina = MAX_STAMINA
        self.__bmrTime = 0
        self.__bmrRecharge = 3
        self.speaking = False


    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and self.yLoc+CHARACTER_SIZE <= 600: 
            self.yLoc += self.__movementSpeed 
          
        elif key[pygame.K_UP] and 0 <= self.yLoc:
            self.yLoc -= self.__movementSpeed
        if key[pygame.K_RIGHT] and self.xLoc+CHARACTER_SIZE <= 1000: 
            self.xLoc += self.__movementSpeed 
        elif key[pygame.K_LEFT] and 0 <= self.xLoc: 
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

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.xLoc, self.yLoc))

    def wounded(self):
        self.__health -= 1
        if(self.__health == 0):
            pygame.quit()

    def spawn_boomerang(self, surface):
        bmrX = self.xLoc + CHARACTER_SIZE/2
        bmrY = self.yLoc + CHARACTER_SIZE/2
        bmr = Boomerang(bmrX, bmrY)
        bmr.draw(surface)
        return bmr

    def check_collision(self, object):
        return self.rect.colliderect(object.rect)
            
    def interact(self, object, isArtifact):
        if(self.check_collision(object)):
            self.speaking = True
       

