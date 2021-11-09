import time
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([5, 5])
        self.image.fill('red')
        self.health = 100
        self.recharge = 3
        self.stamina = 20
        self.bmrUse = True
    
    def sprint(self):
        while(self.stamina > 0):
            self.stamina -= 1
            time.sleep(0.1)

    def wounded(self):
        self.health -= 10


    

        
