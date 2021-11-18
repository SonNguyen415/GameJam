import pygame
import random as rnd
import time
from classes import Door
from menu import *
from settings import *
#-----------------------------#

playerPosition = [2,2]

grid = [['B','B','B','B','B',],
         ['B','B','B','B','B',],
         ['B','B','NSWE','B','B',],
         ['B','B','B','B','B',],
         ['B','B','B','B','B',]]

playerGrid = [['B','B','B','B','B',],
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







def initiate_doors(spriteList):
    for i in playerGrid[playerPosition[0]][playerPosition[1]]:
        if i == 'N':
            north = Door(500,100, DOOR_IMG, 'N')
            north.draw(screen)
        elif i == 'S':
            south = Door(500,500, DOOR_IMG, 'S')
            south.rotate(180)
            south.draw(screen)
        elif i == 'W':
            west = Door(100,300, DOOR_IMG, 'W')
            west.rotate(90)
            west.draw(screen)
        elif i == 'E':
            east = Door(900,300, DOOR_IMG, 'E')
            east.rotate(270)
            east.draw(screen)

def display(screen):
    for i in range(len(playerGrid)):
        for j in range(len(playerGrid[i])):
            image = pygame.image.load(IMAGES[playerGrid[i][j]][0])
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, ((0+(j*19)) , (505+(i*19))))
    pygame.draw.circle(screen, (255,0,0), (10+((playerPosition[0])*19), 515+((playerPosition[1])*19)), 3)

def updateMap(spriteList):
    pGrid = playerGrid[playerPosition[0]][playerPosition[1]]
    if pGrid == 'B':
        pGrid = grid[playerPosition[0]][playerPosition[1]]
    initiate_doors(spriteList)







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
            if grid[i][j] != 'B' and grid[i][j] != 'NSWE':
                gridStats[tile].append(ENEMIES[rnd.randint(0,len(ENEMIES)-1)])
            else:
                gridStats[tile].append([])

def fix():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not bool(grid[i][j]):
                grid[i][j] = 'B'

def refresh(screen):
    screen.fill((0,0,0))
    pygame.display.update()
