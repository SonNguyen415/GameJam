import time
import pygame


WHITE = (255, 255, 255)


class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = pygame.image.load("player.png")
    
        # Set our transparent color
        self.image.set_colorkey(WHITE)

        # Some character data
        self.health = 100
        self.recharge = 3
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.movementSpeed = 5
        self.stamina = 20
        self.usingBMR = True

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]: 
            self.yLoc += self.movementSpeed 
        elif key[pygame.K_UP]:
            self.yLoc -= self.movementSpeed
        if key[pygame.K_RIGHT]: 
            self.xLoc += self.movementSpeed 
        elif key[pygame.K_LEFT]: 
            self.xLoc -= self.movementSpeed 
        
    
    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.xLoc, self.yLoc))

    def sprint(self):
        self.movementSpeed = 7
        while(self.stamina > 0):
            self.stamina -= 1
            time.sleep(0.1)

    def wounded(self):
        self.health -= 10

    # def throw_boomerang(self, boomerang):
        # Boomerang = instance of boomerang
        # Boomerang.spawn_boomerang()


