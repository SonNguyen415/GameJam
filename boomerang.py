import pygame

BOOMERANG_DISTANCE = 100
BOOMERANG_SIZE = 20

class Boomerang(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()
        self.__xLoc = xLoc
        self.__yLoc = yLoc
        
    def spawn_boomerang(self, surface, charX, charY):
        self.image = pygame.image.load("boomerang.png")
        self.image = pygame.transform.scale(self.image, (BOOMERANG_SIZE, BOOMERANG_SIZE))
        surface.blit(self.image, (self.charX, self.charY))

    def move_boomerang(self):
        print("Hi")

    