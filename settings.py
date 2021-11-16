import pygame

# white color
COLOR_WHITE = (255,255,255)
# light shade of the button
COLOR_LIGHT = (255,170,0)
# dark shade of the button
COLOR_DARK = (180,130,0)

WINDOW_LENGTH = 1000
WINDOW_HEIGHT = 600

PLAYGROUND_LENGTH = 704
PLAYGROUND_HEIGHT = 344


CHAR_WIDTH = 120
CHAR_HEIGHT = 200

WAIT_TIME = 10

BOOMERANG_SIZE = 20
BOOMERANG_SPEED = [30, 30]
BOOMERANG_TIME = 50
LOC_TOLERANCE = 1
SPEED_TOLERANCE = 1
DECCELERATION = 100
TIME_TOLERANCE = 5



DOWN_IMG = []
UP_IMG = []
LEFT_IMG = []
RIGHT_IMG = []

UP_IMG.append(pygame.image.load('Character Sprites/Up/1.png'))
UP_IMG.append(pygame.image.load('Character Sprites/Up/2.png'))
UP_IMG.append(pygame.image.load('Character Sprites/Up/3.png'))

RIGHT_IMG.append(pygame.image.load('Character Sprites/Right/1.png'))
RIGHT_IMG.append(pygame.image.load('Character Sprites/Right/2.png'))
RIGHT_IMG.append(pygame.image.load('Character Sprites/Right/3.png'))

DOWN_IMG.append(pygame.image.load('Character Sprites/Down/1.png'))
DOWN_IMG.append(pygame.image.load('Character Sprites/Down/2.png'))
DOWN_IMG.append(pygame.image.load('Character Sprites/Down/3.png'))

LEFT_IMG.append(pygame.image.load('Character Sprites/Left/1.png'))
LEFT_IMG.append(pygame.image.load('Character Sprites/Left/2.png'))
LEFT_IMG.append(pygame.image.load('Character Sprites/Left/3.png'))

PLAYER_IMG = [UP_IMG, RIGHT_IMG, DOWN_IMG, LEFT_IMG]



UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3