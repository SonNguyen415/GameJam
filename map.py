import pygame

pygame.init()


#game window
SCREEN_WIDTH =800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Game Jam')


#load images
bac_img  = pygame.image.load('1781.jpg').convert_alpha()


#creats function for drawing background
def draw_bg():
    screen.blit(bac_img, (0,0))

run =True
while run:
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()



