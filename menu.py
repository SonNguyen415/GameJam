import pygame
import sys
import button
from characters import draw_speech_bubble


#initialize pygame
pygame.init()

# Generate Window
screen = pygame.display.set_mode((1000, 600))

# Title and Icon
pygame.display.set_caption("Jelly Jammers")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Title and Icon
pygame.display.set_caption("Jelly Jammers")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Set image path as variables for later use
START_IMG = pygame.image.load("Button Icons/Play Button.png").convert_alpha()
EXIT_IMG = pygame.image.load("Button Icons/Quit Button.png").convert_alpha()
CREDIT_IMG = pygame.image.load("Button Icons/Credit Button.png").convert_alpha()
BACK_IMG = pygame.image.load("Button Icons/Back Button.png").convert_alpha()
BACKGROUND = pygame.image.load("Backgrounds/Background.png")
BG_CREDITS = pygame.image.load("Backgrounds/Background Credits.png")

WIDTH = screen.get_width()
HEIGHT = screen.get_height()
startButtonWidth = START_IMG.get_width()
exitButtonWidth = EXIT_IMG.get_width()
creditButtonWidth = CREDIT_IMG.get_width()
backButtonWidth = BACK_IMG.get_width()
backButtonHeight = BACK_IMG.get_height()


startButton = button.Button(((WIDTH/2) - (startButtonWidth*4/2)), 100, START_IMG, 4)
exitButton = button.Button(((WIDTH/2) - (exitButtonWidth*4/2)), 400, EXIT_IMG, 4)
creditButton = button.Button(((WIDTH/2) - (creditButtonWidth*4/2)), 250, CREDIT_IMG, 4)
backButton = button.Button(50, ((HEIGHT/2) - (backButtonHeight*3/2)), BACK_IMG, 3)

sound = pygame.mixer.Sound('sound.mp3')

#----------------------------------------------#

def main_menu():
    changeScreen = "Main"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    screen.blit(BACKGROUND, (0,0))

    if startButton.draw(screen):
        sound.play()
        return "Play"
    if exitButton.draw(screen):
        pygame.quit()
    if creditButton.draw(screen):
        changeScreen = "Credits"

    pygame.display.update()

    return changeScreen

#----------------------------------------------#

def credit_menu():
    changeScreen = "Credits"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    screen.blit(BG_CREDITS, (0,0))

    if backButton.draw(screen):
        changeScreen = "Main"

    pygame.display.update()

    return changeScreen

