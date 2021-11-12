import pygame

BOOMERANG_SIZE = 20

class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        
    def spawn_boomerang(self):
        self.image = pygame.image.load("boomerang.png")
        self.image = pygame.transform.scale(self.image, (BOOMERANG_SIZE, BOOMERANG_SIZE))
