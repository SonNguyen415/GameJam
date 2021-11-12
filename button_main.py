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
bg = pygame.image.load("Background.png")

startButton = button.Button(100, 200, start_img, 10)
exitButton = button.Button(500, 200, exit_img, 10)



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

    pygame.display.update()

pygame.quit()
