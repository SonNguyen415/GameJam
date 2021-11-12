import pygame
import random as rnd

pygame.init()

screen = pygame.display.set_mode((1000,600))

screen.fill((200,200,200))

class Tile():
    def __init__(self, x, y , image, scale):
        # Call the parent class (Sprite) constructor
       super().__init__()
       width = image.get_width()
       height = image.get_height()
       self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
       self.rect = self.image.get_rect()
       self.rect.topleft = (x,y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


#-----------------------------#

grid = [['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','NSWE','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B']]

ROOMS = {
        'N': ['NS', 'NS', 'NS', 'NS', 'S', 'S', 'S', 'SW', 'SE', 'SWE', 'NSW', 'NSE'],
        'W': ['WE', 'WE', 'WE', 'WE', 'E', 'E', 'E', 'SE', 'NE', 'SWE', 'NSE', 'NWE'],
        'E': ['WE', 'WE', 'WE', 'WE', 'W', 'W', 'W', 'SW', 'NW', 'SWE', 'NSW', 'NWE'],
        'S': ['NS', 'NS', 'NS', 'NS', 'N', 'N', 'N', 'NW', 'NE', 'NSE', 'NSW', 'NWE']
        }

IMAGES = {'B': ['Map Tiles/B.png'],
          'E': ['Map Tiles/E.png'],
          'N': ['Map Tiles/N.png'],
          'NE': ['Map Tiles/NE.png'],
          'NS': ['Map Tiles/NS.png'],
          'NSE': ['Map Tiles/NSE.png'],
          'NSW': ['Map Tiles/NSW.png'],
          'NSWE': ['Map Tiles/NSWE.png'],
          'NW': ['Map Tiles/NW.png'],
          'NWE': ['Map Tiles/NWE.png'],
          'S': ['Map Tiles/S.png'],
          'SE': ['Map Tiles/SE.png'],
          'SW': ['Map Tiles/SW.png'],
          'SWE': ['Map Tiles/SWE.png'],
          'W': ['Map Tiles/W.png'],
          'WE':['Map Tiles/WE.png']
          }

#-----------------------------#

def check_left(y,x):
    if x != 0:
        if grid[y][x-1].find('E') != -1:
            return True


def check_right(y,x):
    length = len(grid[x])
    if x != length-1:
        if grid[y][x+1].find('W') != -1:
            return True

def check_up(y,x):
    if y != 0:
        if grid[y-1][x].find('S') != -1:
            return True

def check_down(y,x):
    length = len(grid)
    if y != length-1:
        if grid[y+1][x].find('N') != -1:
            return True

def generate_room(direction):
    dictionaryLength = len(ROOMS[direction])-1
    return ROOMS[direction][rnd.randint(0,dictionaryLength)]

def refresh():
    screen.fill((200,200,200))
    pygame.display.flip()
    grid = [['B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B'],
            ['B','B','B','NSWE','B','B','B'],
            ['B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B'],
            ['B','B','B','B','B','B','B']]
    return grid

def display(screen):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            image = pygame.image.load(IMAGES[grid[i][j]][0])
            image = pygame.transform.scale(image, (50,50))
            screen.blit(image, (j+(j*48),i+(i*48)))

def generate():
    generateNewRoom = True
    while generateNewRoom:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'B':
                    if check_left(i,j):
                        grid[i][j] = generate_room('E')
                        count+=1
                    if check_right(i,j):
                        grid[i][j] = generate_room('W')
                        count+=1
                    if check_up(i,j):
                        grid[i][j] = generate_room('S')
                        count+=1
                    if check_down(i,j):
                        grid[i][j] = generate_room('N')
                        count+=1
        if count == 0:
            generateNewRoom = False

    for i in range(len(grid)):
        print(grid[i])

#-----------------------------#

running = True
generate()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid = refresh()
                generate()

    display(screen)

    pygame.display.update()
