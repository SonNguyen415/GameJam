import pygame
import sys

#initialize pygame
pygame.init()

# Generate Window
screen = pygame.display.set_mode((1000, 600))

# Title and Icon
pygame.display.set_caption("Jelly Jammers")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


start_img = pygame.image.load("Button Icons/Play Button.png").convert_alpha()
exit_img = pygame.image.load("Button Icons/Quit Button.png").convert_alpha()

class Button():
    def __init__(self, x, y , image, scale):
        # Call the parent class (Sprite) constructor
       super().__init__()
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x,y)

    def draw(self):
        # Draw button on the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

startButton = Button(100, 200, start_img, 10)
exitButton = Button(500, 200, exit_img, 10)



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            runnning  = False

    screen.fill((202, 228, 241))

    startButton.draw()
    exitButton.draw()

    pygame.display.update()
