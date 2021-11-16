import pygame
import random as rnd
import time

pygame.init()

screen = pygame.display.set_mode((1000,600))

screen.fill((0,0,0))

#-----------------------------#

grid = [['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','NSWE','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B']]

gridStats ={
            '(0, 0)':[],
            '(0, 1)':[],
            '(0, 2)':[],
            '(0, 3)':[],
            '(0, 4)':[],
            '(1, 0)':[],
            '(1, 1)':[],
            '(1, 2)':[],
            '(1, 3)':[],
            '(1, 4)':[],
            '(2, 0)':[],
            '(2, 1)':[],
            '(2, 2)':[],
            '(2, 3)':[],
            '(2, 4)':[],
            '(3, 0)':[],
            '(3, 1)':[],
            '(3, 2)':[],
            '(3, 3)':[],
            '(3, 4)':[],
            '(4, 0)':[],
            '(4, 1)':[],
            '(4, 2)':[],
            '(4, 3)':[],
            '(4, 4)':[]
            }

grid2 = [['B','B','B'],
         ['B','NSWE','B'],
         ['B','B','B']]

grid3 = [['B','B','B','B','B',],
         ['B','B','B','B','B',],
         ['B','B','NSWE','B','B',],
         ['B','B','B','B','B',],
         ['B','B','B','B','B',]]

grid = grid3

grid4 = [['B','B','B','B'],
         ['B','NSWE','B','B'],
         ['B','B','B','B']]

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

ENEMIES = [[0,0,0],
           [1,0,0],
           [2,0,0],
           [3,0,0],
           [2,1,0],
           [0,3,0],
           [0,0,1],
           [2,0,1],
           [1,3,0],
           [3,1,0],
           [0,0,2],
           [0,2,1],
           [3,2,0],
           [0,2,0],
           [5,0,0],
           [3,2,1],
           [3,2,2]]

#-----------------------------#

def check_left(y,x):
    if x != 0:
        if 'B' not in str(grid[y][x-1]):
            if 'E' in str(grid[y][x-1]):
                return True

def check_right(y,x):
    length = len(grid[y])-1
    if x != length:
        if 'B' not in str(grid[y][x+1]):
            if 'W' in str(grid[y][x+1]):
                return True

def check_up(y,x):
    if y != 0:
        if 'B' not in str(grid[y-1][x]):
            if 'S' in str(grid[y-1][x]):
                return True

def check_down(y,x):
    length = len(grid)-1
    if y != length:
        if 'B' not in str(grid[y+1][x]):
            if 'N' in str(grid[y+1][x]):
                return True

#-------------------#

def check_walls_left(y,x):
    if x != 0:
        if 'B' not in str(grid[y][x-1]):
            if 'E' not in str(grid[y][x-1]):
                return True

def check_walls_right(y,x):
    length = len(grid[y])
    if x != length-1:
        if 'B' not in str(grid[y][x+1]):
            if 'W' not in str(grid[y][x+1]):
                return True

def check_walls_up(y,x):
    if y != 0:
        if 'B' not in str(grid[y-1][x]):
            if 'S' not in str(grid[y-1][x]):
                return True

def check_walls_down(y,x):
    length = len(grid)
    if y != length-1:
        if 'B' not in str(grid[y+1][x]):
            if 'N' not in str(grid[y+1][x]):
                return True


#-------------------#

def generate_room(directions,directionsWalls):
    branchCount = 3

    if len(directions) != 0:
        if len(directions) > 1:
            startList = ROOMS[directions[0]]
            similarities = []

            for i in range(len(directions)-1):
                for l in range(len(startList)):
                    for j in range(len(ROOMS[directions[i+1]])):
                        if startList[l] == ROOMS[directions[i+1]][j]:
                            similarities.append(startList[l])
                startList = similarities
                similarities = []

        else:
            startList = ROOMS[directions[0]]

        newList = []
        for t in range(len(startList)):
            bool = True
            for n in range(len(directionsWalls)):
                if startList[t].find(str(directionsWalls[n])) != -1:
                    bool = False
            if bool == True:
                newList.append(startList[t])


        length = len(newList)
        if length != 0:
            answer = newList[rnd.randint(0,length-1)]

            """
            repeat = True
            while repeat:
                answer = newList[rnd.randint(0,length-1)]
                if branchCount > 0:
                    branchCount -= 1
                    repeat = False
                elif branchCount == 0:
                    if len(directions):
                        if len(answer) == 1:
                            repeat == False
            """

        return answer

    else:
        return 'B'

def reset(answer):
    screen.fill((0,0,0))
    pygame.display.flip()

    grid =  [['B','B','B','B','B',],
             ['B','B','B','B','B',],
             ['B','B','NSWE','B','B',],
             ['B','B','B','B','B',],
             ['B','B','B','B','B',]]

    gridStats ={
                '(0, 0)':[],
                '(0, 1)':[],
                '(0, 2)':[],
                '(0, 3)':[],
                '(0, 4)':[],
                '(1, 0)':[],
                '(1, 1)':[],
                '(1, 2)':[],
                '(1, 3)':[],
                '(1, 4)':[],
                '(2, 0)':[],
                '(2, 1)':[],
                '(2, 2)':[],
                '(2, 3)':[],
                '(2, 4)':[],
                '(3, 0)':[],
                '(3, 1)':[],
                '(3, 2)':[],
                '(3, 3)':[],
                '(3, 4)':[],
                '(4, 0)':[],
                '(4, 1)':[],
                '(4, 2)':[],
                '(4, 3)':[],
                '(4, 4)':[]
                }
    if answer == 'grid':
        return grid
    elif answer == 'stats':
        return gridStats


def display(screen):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            image = pygame.image.load(IMAGES[grid[i][j]][0])
            image = pygame.transform.scale(image, (50,50))
            screen.blit(image, ((j+(j*48)) , (i+(i*48))))

def checkForDoors(i,j):
    directions = []
    if check_left(i,j):
        directions.append('E')
    if check_right(i,j):
        directions.append('W')
    if check_up(i,j):
        directions.append('S')
    if check_down(i,j):
        directions.append('N')
    return directions

def checkForWalls(i,j):
    directions = []
    if i == 0:
        directions.append('N')
    if i == len(grid)-1:
        directions.append('S')
    if j == 0:
        directions.append('W')
    if j == len(grid[i])-1:
        directions.append('E')

    if check_walls_left(i,j):
        directions.append('W')
    if check_walls_right(i,j):
        directions.append('E')
    if check_walls_up(i,j):
        directions.append('N')
    if check_walls_down(i,j):
        directions.append('S')
    return directions

def checkIteration():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'B':
                doors = checkForDoors(i,j)
                if len(doors) > 0:
                    return True
    return False

def generate():
    while checkIteration() == True:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'B':
                    doors = checkForDoors(i,j)
                    walls = checkForWalls(i,j)
                    grid[i][j] = generate_room(doors,walls)

def generateStats():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tile = '({}, {})'.format(i,j)
            print(tile)
            print(grid[i][j])
            if grid[i][j] != 'B' and grid[i][j] != 'NSWE':
                gridStats[tile].append(ENEMIES[rnd.randint(0,len(ENEMIES)-1)])
            else:
                gridStats[tile].append([])
            print(gridStats[tile])
            print("")

def fix():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not bool(grid[i][j]):
                grid[i][j] = 'B'

def refresh(screen):
    screen.fill((0,0,0))
    pygame.display.update()


#-----------------------------#

generate()
generateStats()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_r:
                grid = reset('grid')
                gridStats = reset('stats')
                generate()
                generateStats()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if gridStats[pos] == [0,0,0]:
                    print("The Room is Empty")
                elif gridStats[pos] == []:
                    print("There is no Room Here")
                else:
                    print("The Room Contains Grunts:{}, Ranged:{}, Tanks{}"
                    .format(gridStats[pos][0][0],gridStats[pos][0][1],gridStats[pos][0][2]))

    fix()
    display(screen)
    pygame.draw.circle(screen, (255,0,0), (122,123), 10)

    pos = pygame.mouse.get_pos()
    pos = str((pos[0]//49, pos[1]//49))


    pygame.display.update()
