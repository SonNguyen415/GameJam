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
back_img = pygame.image.load("Button Icons/Back Button.png").convert_alpha()
bg = pygame.image.load("Backgrounds/Background.png")
bg_credits = pygame.image.load("Backgrounds/Background Credits.png")

width = screen.get_width()
height = screen.get_height()
startButtonWidth = start_img.get_width()
exitButtonWidth = exit_img.get_width()
creditButtonWidth = credit_img.get_width()
backButtonWidth = back_img.get_width()
backButtonHeight = back_img.get_height()

startButton = button.Button(((width/2) - (startButtonWidth*4/2)), 100, start_img, 4)
exitButton = button.Button(((width/2) - (exitButtonWidth*4/2)), 400, exit_img, 4)
creditButton = button.Button(((width/2) - (creditButtonWidth*4/2)), 250, credit_img, 4)
backButton = button.Button(50, ((height/2) - (backButtonHeight*3/2)), back_img, 3)

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

    screen.blit(bg, (0,0))

    if startButton.draw(screen):
        sound.play()
    if exitButton.draw(screen):
        pygame.quit()
    if creditButton.draw(screen):
        changeScreen = "Credit"

    pygame.display.update()

    return changeScreen

#----------------------------------------------#

def credit_menu():
    changeScreen = "Credit"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg_credits, (0,0))

    if backButton.draw(screen):
        changeScreen = "Main"

    pygame.display.update()

    return changeScreen

#----------------------------------------------#
currentScreen = "Main"

running = True
while running:
    if currentScreen == "Main":
        currentScreen = main_menu()
    elif currentScreen == "Credit":
        currentScreen = credit_menu()
