import pygame
import time
import button
from settings import WINDOW_HEIGHT, WINDOW_LENGTH


#initialize pygame
pygame.init()

# Generate Window
screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))

# Title and Icon
pygame.display.set_caption("Jelly Jammers")
icon = pygame.image.load('Objects/icon.png')
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
creditButton = button.Button(((WIDTH/2) - (creditButtonWidth*4/2)), 250, CREDIT_IMG, 4)
exitButton = button.Button(((WIDTH/2) - (exitButtonWidth*4/2)), 400, EXIT_IMG, 4)
backButton = button.Button(50, ((HEIGHT/2) - (backButtonHeight*3/2)), BACK_IMG, 3)


resumeButton = button.Button(50, 100, 'Button Icons/Resume.png', 4)
exitButton = button.Button(50, 200, 'Button Icons/Exit.png', 4)


sound = pygame.mixer.Sound('sound.mp3')

#----------------------------------------------#

def main_menu(currScreen):
    screen.blit(BACKGROUND, (0,0))

    if startButton.draw(screen):
        sound.play()
        time.sleep(0.1)
        return "Play"
    if exitButton.draw(screen):
        pygame.quit()
    if creditButton.draw(screen):
        currScreen = "Credits"

    pygame.display.update()

    return currScreen

#----------------------------------------------#

def credit_menu(currScreen):
    currScreen = "Credits"

    screen.blit(BG_CREDITS, (0,0))

    if backButton.draw(screen):
        currScreen = "Main"

    pygame.display.update()

    return currScreen



def pause_menu(pauseMenu):
    pauseMenu.draw()
    if resumeButton.draw(screen):
        return
    elif exitButton.draw(screen):
        pygame.quit()
    pause_menu()

