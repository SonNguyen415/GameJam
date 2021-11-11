import pygame
import sys

#initialize pygame
pygame.init()

# Generate Window
screen = pygame.display.set_mode((500, 500))

# Title and Icon
pygame.display.set_caption("Jelly Jammers")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)




# white color
color = (255,255,255)
# light shade of the button
color_light = (255,170,0)
# dark shade of the button
color_dark = (180,130,0)

# get width and height for later reference
width = screen.get_width()
height = screen.get_height()
button_width = 140
button_height = 40


# set font
smallfont = pygame.font.SysFont('Corbel', 40)

credit_names = ("Oliver"
                "Fred"
                "Son"
                "Warren")

# renders text
quit_text = smallfont.render('Quit' , True , color)
credit_text = smallfont.render('Credits', True, color)
credits = smallfont.render(credit_names, True, color)
play_text = smallfont.render('Play', True, color)

current_screen = "Main Menu"

# Game Loop
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
                screen.fill((100,60,25))
                current_screen = "Credits"
            elif width/2-70 <= mouse[0] <= width/2+70 and height/2+40 <= mouse[1] <= height/2+80:
                pygame.quit()
            elif width/2-70 <= mouse[0] <= width/2+70 and height/2-80 <= mouse[1] <= height/2+80:
                screen.fill((100,60,25))


    screen.fill((100,60,25))

    mouse = pygame.mouse.get_pos()

    if current_screen == "Main Menu":
        # Credit button
        if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
            pygame.draw.rect(screen,color_light,[(width/2-70),(height/2-20),140,40])
            screen.blit(credit_text , (width/2-50,height/2-10))
        else:
            pygame.draw.rect(screen,color_dark,[(width/2-70),(height/2-20),140,40])
            screen.blit(credit_text , (width/2-50,height/2-10))



            # Quit button
        if width/2-70 <= mouse[0] <= width/2+70 and height/2+40 <= mouse[1] <= height/2+80:
            pygame.draw.rect(screen,color_light,[(width/2-70),(height/2+40),140,40])
            screen.blit(quit_text , (width/2-32.5,height/2+50))
        else:
            pygame.draw.rect(screen,color_dark,[(width/2-70),(height/2+40),140,40])
            screen.blit(quit_text , (width/2-32.5,height/2+50))




            # Play Button
        if width/2-70 <= mouse[0] <= width/2+70 and height/2-80 <= mouse[1] <= height/2-40:
            pygame.draw.rect(screen,color_light,[(width/2-70),(height/2-80),140,40])
            screen.blit(play_text , (width/2-32.5,height/2-70))
        else:
            pygame.draw.rect(screen,color_dark,[(width/2-70),(height/2-80),140,40])
            screen.blit(play_text , (width/2-32.5,height/2-70))



    elif current_screen == "Credits":
        screen.blit(credits , (width/2,height/2))

    # updates the frames of the game
    pygame.display.update()
