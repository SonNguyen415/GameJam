import pygame
from pygame import key

# white color
COLOR_WHITE = (255,255,255)
# light shade of the button
COLOR_LIGHT = (255,170,0)
# dark shade of the button
COLOR_DARK = (180,130,0)


WAIT_TIME = 5


WINDOW_LENGTH = 1000
WINDOW_HEIGHT = 600
PLAYGROUND_LENGTH = 704
PLAYGROUND_HEIGHT = 344
PLAYGROUND_X_OFFSET = 148
PLAYGROUND_Y_OFFSET = 128
WALL_HEIGHT = 20


WALK_SPEED = 5
SPRINT_SPEED = 8
MAX_STAMINA = 50
STAMINA_RECHARGE_TIME = 3
POS_TOLERANCE = 6

CHAR_WIDTH = 30
CHAR_HEIGHT = 50
ICON_SCALE = 25



BOOMERANG_SIZE = 20
BOOMERANG_SPEED = [30, 30]
BOOMERANG_TIME = 20
LOC_TOLERANCE = 1
SPEED_TOLERANCE = 5
MAX_BMR_DISTANCE = 200
MAX_BMR_TIME = 20



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

FPS = 25

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
