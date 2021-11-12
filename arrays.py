import random as rnd
from re import search

ROOMS = {
        'N': ['NS', 'NS', 'NS', 'NS', 'S', 'S', 'S', 'SW', 'SE', 'SWE', 'NSW', 'NSE'],
        'W': ['WE', 'WE', 'WE', 'WE', 'E', 'E', 'E', 'SE', 'NE', 'SWE', 'NSE', 'NWE'],
        'E': ['WE', 'WE', 'WE', 'WE', 'W', 'W', 'W', 'SW', 'NW', 'SWE', 'NSW', 'NWE'],
        'S': ['NS', 'NS', 'NS', 'NS', 'N', 'N', 'N', 'NW', 'NE', 'NSE', 'NSW', 'NWE']
        }


directions = ['E', 'S']
directionsWalls = ['S', 'W']
startList = ROOMS[directions[0]]
similarities = []

for i in range(len(directions)-1):
    for l in range(len(startList)):
        for j in range(len(ROOMS[directions[i+1]])):
            if startList[l] == ROOMS[directions[i+1]][j]:
                similarities.append(startList[l])
    startList = similarities
    similarities = []
    print(startList)

newList = []
for t in range(len(startList)):
    bool = True
    for n in range(len(directionsWalls)):
        if startList[t].find(str(directionsWalls[n])) != -1:
            bool = False
    if bool == True:
        newList.append(startList[t])

print(newList)
