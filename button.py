# Button class
import pygame

class Button():
    def __init__(self, x, y , image, scale):
        # Call the parent class (Sprite) constructor
       super().__init__()

       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x,y)
       self.clicked = False

    def draw(self, surface):

        action = False
        pos = pygame.mouse.get_pos()

        # Conditional statement to check if the button is pressed
        if self.rect.collidepoint(pos):
             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                 self.clicked = True
                 action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        # Returns if the button is pressed
        return action
