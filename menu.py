import pygame
import time
import button
from settings import WINDOW_HEIGHT, WINDOW_LENGTH


#initialize pygame
pygame.init()

# Generate Windows
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


victoryImage = pygame.image.load('Backgrounds/Victory.png')
VICTORY = pygame.transform.scale(victoryImage, (WINDOW_LENGTH, WINDOW_HEIGHT))
defeatImage = pygame.image.load('Backgrounds/Gameover.png')
DEFEAT = pygame.transform.scale(defeatImage, (WINDOW_LENGTH, WINDOW_HEIGHT))



WIDTH = screen.get_width()
HEIGHT = screen.get_height()
startButtonWidth = START_IMG.get_width()
quitButtonWidth = EXIT_IMG.get_width()
creditButtonWidth = CREDIT_IMG.get_width()
backButtonWidth = BACK_IMG.get_width()
backButtonHeight = BACK_IMG.get_height()


startButton = button.Button(((WIDTH/2) - (startButtonWidth*2)), 100, START_IMG, 4)
creditButton = button.Button(((WIDTH/2) - (creditButtonWidth*2)), 250, CREDIT_IMG, 4)
quitButton = button.Button(((WIDTH/2) - (quitButtonWidth*2)), 400, EXIT_IMG, 4)
backButton = button.Button(50, ((HEIGHT/2) - (backButtonHeight*3/2)), BACK_IMG, 3)


RES_BUTTON = pygame.image.load("Button Icons/Resume.png").convert_alpha()
EXIT_BUTTON = pygame.image.load("Button Icons/Exit.png").convert_alpha()

resumeWidth = RES_BUTTON.get_width()
exitWidth = EXIT_BUTTON.get_width()


#----------------------------------------------#





def main_menu(currScreen):

    screen.blit(BACKGROUND, (0,0))

    if startButton.draw(screen):
        time.sleep(0.1)
        return "Play"
    if quitButton.draw(screen):
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


def victory_screen():
    screen.blit(VICTORY, (0, 0))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()


def defeat_screen():
    screen.blit(DEFEAT, (0, 0))
    pygame.display.update()
    time.sleep(2)
    return "Main"


def pause_menu():
    resumeButton = button.Button(WINDOW_LENGTH/2-resumeWidth/2, WINDOW_HEIGHT/2 - 50, RES_BUTTON, 1)
    exitButton = button.Button(WINDOW_LENGTH/2-exitWidth/2, WINDOW_HEIGHT/2, EXIT_BUTTON, 1)
    if resumeButton.draw(screen):
        return True
    elif exitButton.draw(screen):
        return "Main"
    else:
        return False
