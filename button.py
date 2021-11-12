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
    def __init__(self, x, y , image):
        # Call the parent class (Sprite) constructor
       super().__init__()

       self.image = image
       self.rect = self.image.get_rect()
       self.rect.topleft = (x,y)

    def draw():
        # Draw button on the screen
        screen.blit(self.image (self.rect.x, self.rect.y))

startButton = Button(100, 200, start_img)
exitButton = Button(500, 200, exit_img)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            runnning = False

    screen.fill((202, 228, 241))

    pygame.display.update()
