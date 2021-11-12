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



# white color
COLOR_WHITE = (255,255,255)
# light shade of the button
COLOR_LIGHT = (255,170,0)
# dark shade of the button
COLOR_DARK = (180,130,0)

# get width and height for later reference
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
button_width = 140
button_height = 40


# set font
smallfont = pygame.font.SysFont('Corbel', 40)

creditNames = ("Oliver"
                "Fred"
                "Son"
                "Warren")

# renders text
quitText = smallfont.render('Quit' , True , COLOR_WHITE)
creditText = smallfont.render('Credits', True, COLOR_WHITE)
credits = smallfont.render(creditNames, True, COLOR_WHITE)
playText = smallfont.render('Play', True, COLOR_WHITE)

currentScreen = "Main Menu"


def make_menu(mouse, myScreen):
    if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2-20 <= mouse[1] <= HEIGHT/2+20:
        pygame.draw.rect(myScreen,COLOR_LIGHT,[(WIDTH/2-70),(HEIGHT/2-20),140,40])
        myScreen.blit(creditText , (WIDTH/2-50,HEIGHT/2-10))
    else:
        pygame.draw.rect(myScreen,COLOR_DARK,[(WIDTH/2-70),(HEIGHT/2-20),140,40])
        myScreen.blit(creditText , (WIDTH/2-50,HEIGHT/2-10))

        # Quit button
    if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2+40 <= mouse[1] <= HEIGHT/2+80:
        pygame.draw.rect(myScreen,COLOR_LIGHT,[(WIDTH/2-70),(HEIGHT/2+40),140,40])
        myScreen.blit(quitText , (WIDTH/2-32.5,HEIGHT/2+50))
    else:
        pygame.draw.rect(myScreen,COLOR_DARK,[(WIDTH/2-70),(HEIGHT/2+40),140,40])
        myScreen.blit(quitText , (WIDTH/2-32.5,HEIGHT/2+50))

        # Play Button
    if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2-80 <= mouse[1] <= HEIGHT/2-40:
        pygame.draw.rect(myScreen,COLOR_LIGHT,[(WIDTH/2-70),(HEIGHT/2-80),140,40])
        myScreen.blit(playText , (WIDTH/2-32.5,HEIGHT/2-70))
    else:
        pygame.draw.rect(myScreen,COLOR_DARK,[(WIDTH/2-70),(HEIGHT/2-80),140,40])
        myScreen.blit(playText , (WIDTH/2-32.5,HEIGHT/2-70))


def change_menu(mouse, myScreen):
    if WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2-20 <= mouse[1] <= HEIGHT/2+20:
        myScreen.fill((100,60,25))
        return "Credits"
    elif WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2+40 <= mouse[1] <= HEIGHT/2+80:
        pygame.quit()
        return "Quit"
    elif WIDTH/2-70 <= mouse[0] <= WIDTH/2+70 and HEIGHT/2-80 <= mouse[1] <= HEIGHT/2+80:
        return "Play"
