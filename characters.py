import time
import pygame



WHITE = (255, 255, 255)


class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
    
        # Set our transparent color
        self.image.set_colorkey(WHITE)

        # Some character data
        self.__health = 100
        self.__recharge = 3
        self.__xLoc = xLoc
        self.__yLoc = yLoc
        self.__movementSpeed = 2
        self.__stamina = 20
        self.__usingBMR = True

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]: 
            self.__yLoc += self.__movementSpeed 
        elif key[pygame.K_UP]:
            self.__yLoc -= self.__movementSpeed
        if key[pygame.K_RIGHT]: 
            self.__xLoc += self.__movementSpeed 
        elif key[pygame.K_LEFT]: 
            self.__xLoc -= self.__movementSpeed 
        if key[pygame.K_e]:
            self.interact()

    def interact(self):
        print("Interacting")
        
    
    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.__xLoc, self.__yLoc))

    def sprint(self):
        self.__movementSpeed = 7
        while(self.__stamina > 0):
            self.__stamina -= 1
            time.sleep(0.1)

    def wounded(self):
        self.__health -= 10

    # def throw_boomerang(self, boomerang):
        # Boomerang = instance of boomerang
        # Boomerang.spawn_boomerang()


