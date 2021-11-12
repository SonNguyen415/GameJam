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
width = screen.get_width()
height = screen.get_height()
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
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
        pygame.draw.rect(myScreen,COLOR_LIGHT,[(width/2-70),(height/2-20),140,40])
        myScreen.blit(creditText , (width/2-50,height/2-10))
    else:
        pygame.draw.rect(myScreen,COLOR_DARK,[(width/2-70),(height/2-20),140,40])
        myScreen.blit(creditText , (width/2-50,height/2-10))

        # Quit button
    if width/2-70 <= mouse[0] <= width/2+70 and height/2+40 <= mouse[1] <= height/2+80:
        pygame.draw.rect(myScreen,COLOR_LIGHT,[(width/2-70),(height/2+40),140,40])
        myScreen.blit(quitText , (width/2-32.5,height/2+50))
    else:
        pygame.draw.rect(myScreen,COLOR_DARK,[(width/2-70),(height/2+40),140,40])
        myScreen.blit(quitText , (width/2-32.5,height/2+50))

        # Play Button
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-80 <= mouse[1] <= height/2-40:
        pygame.draw.rect(myScreen,COLOR_LIGHT,[(width/2-70),(height/2-80),140,40])
        myScreen.blit(playText , (width/2-32.5,height/2-70))
    else:
        pygame.draw.rect(myScreen,COLOR_DARK,[(width/2-70),(height/2-80),140,40])
        myScreen.blit(playText , (width/2-32.5,height/2-70))


def change_menu(mouse, myScreen):
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
        myScreen.fill((100,60,25))
        return "Credits"
    elif width/2-70 <= mouse[0] <= width/2+70 and height/2+40 <= mouse[1] <= height/2+80:
        pygame.quit()
        return "Quit"
    elif width/2-70 <= mouse[0] <= width/2+70 and height/2-80 <= mouse[1] <= height/2+80:
        return "Play"
