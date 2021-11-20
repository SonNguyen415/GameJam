import pygame
from pygame import key

# white color
COLOR_WHITE = (255,255,255)
# light shade of the button
COLOR_LIGHT = (255,170,0)
# dark shade of the button
COLOR_DARK = (180,130,0)

COLOR_STAMINA = (0, 203, 255)

WAIT_TIME = 1


WINDOW_LENGTH = 1000
WINDOW_HEIGHT = 600
PLAYGROUND_LENGTH = 688
PLAYGROUND_HEIGHT = 416
PLAYGROUND_X_OFFSET = 148
PLAYGROUND_Y_OFFSET = 90
WALL_HEIGHT = 20


WALK_SPEED = 4
SPRINT_SPEED = 6
MAX_STAMINA = 100
STAMINA_RECHARGE_TIME = 3
POS_TOLERANCE = 6

CHAR_WIDTH = 30
CHAR_HEIGHT = 50


BOOMERANG_SIZE = 20
BOOMERANG_MAX_SPEED = 50
BOOMERANG_TIME = 20
LOC_TOLERANCE = 1
SPEED_TOLERANCE = 5
MAX_BMR_DISTANCE = 400
MAX_BMR_TIME = 20
BMR_DMG = 2



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




NPC_DOWN = []
NPC_UP = []
NPC_LEFT = []
NPC_RIGHT = []

NPC_DOWN.append(pygame.image.load('NPC Sprites/Down/guard1.png'))
NPC_DOWN.append(pygame.image.load('NPC Sprites/Down/guard2.png'))
NPC_DOWN.append(pygame.image.load('NPC Sprites/Down/guard3.png'))


NPC_UP.append(pygame.image.load('NPC Sprites/Up/guard1.png'))
NPC_UP.append(pygame.image.load('NPC Sprites/Up/guard2.png'))
NPC_UP.append(pygame.image.load('NPC Sprites/Up/guard3.png'))

NPC_RIGHT.append(pygame.image.load('NPC Sprites/Right/guard1.png'))
NPC_RIGHT.append(pygame.image.load('NPC Sprites/Right/guard2.png'))
NPC_RIGHT.append(pygame.image.load('NPC Sprites/Right/guard3.png'))

NPC_LEFT.append(pygame.image.load('NPC Sprites/Left/guard1.png'))
NPC_LEFT.append(pygame.image.load('NPC Sprites/Left/guard2.png'))
NPC_LEFT.append(pygame.image.load('NPC Sprites/Left/guard3.png'))

NPC_IMG = [NPC_UP, NPC_RIGHT, NPC_DOWN, NPC_LEFT]



DOOR_IMG = pygame.image.load('Objects/Door.png')

ROCK_IMG = 'Obstacles/Rock1.png'

FPS = 25

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


artifactList = ['BearSword', 'Croc', 'DreamCatcher', 'Drum', 'Mask', 'NavajoPot']
MAX_ARTY_PER_ROOM = 1
ARTY_PROB = 0.2
