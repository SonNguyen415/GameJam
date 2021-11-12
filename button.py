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


# Set image path as variables for later use
start_img = pygame.image.load("Button Icons/Play Button.png").convert_alpha()
exit_img = pygame.image.load("Button Icons/Quit Button.png").convert_alpha()

# Create a button class to apply to multiple buttons
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

    def draw(self):

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
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # Returns if the button is pressed
        return action



startButton = Button(100, 200, start_img, 10)
exitButton = Button(500, 200, exit_img, 10)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((202, 228, 241))

    if startButton.draw():
        print("Start Button Pressed")
    if exitButton.draw():
        running = False

    pygame.display.update()

pygame.quit()
