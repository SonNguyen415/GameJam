import pygame
import sys
import button

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
credit_img = pygame.image.load("Button Icons/Credit Button.png").convert_alpha()
bg = pygame.image.load("Background.png")

width = screen.get_width()
height = screen.get_height()
startButtonWidth = start_img.get_width()
exitButtonWidth = exit_img.get_width()
creditButtonWidth = credit_img.get_width()

startButton = button.Button(((width/2) - (startButtonWidth*10/2)), 100, start_img, 10)
exitButton = button.Button(((width/2) - (exitButtonWidth*10/2)), 400, exit_img, 10)
creditButton = button.Button(((width/2) - (creditButtonWidth*10/2)), 250, credit_img, 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.blit(bg, (0,0))
    #screen.fill((202, 228, 241))

    if startButton.draw(screen):
        print("Start Button Pressed")
    if exitButton.draw(screen):
        running = False
    if creditButton.draw(screen):
        print("Credit Button Pressed")

    pygame.display.update()

pygame.quit()
