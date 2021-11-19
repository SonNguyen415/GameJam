from classes import SpriteObject
from settings import *

def artifact_x(currID):
    xMod = (currID - 1) % 3 
    return 100+xMod*50


def artifact_y(currID):
    yMod = (currID - 1) /  3 
    return 100+yMod*50


def make_id_list():
    idList = []
    return idList


def generate_artifacts(idList):
    currList = [[], []]
    for id,i in enumerate(idList):
        xLoc = artifact_x(i)
        yLoc = artifact_y(i)
        artifactImg = 'Artifacts/' + ARTIFACT_LIST[id] + '.png'
        descrImg = 'ArtifactDescription/' + ARTIFACT_LIST[id] + '.png'
        currArtifact = SpriteObject(xLoc, yLoc, artifactImg, 50, 'artifact')
        currDescription = SpriteObject(100, 100, descrImg, 200, 'artifact')
        currList.append[0](currArtifact)
        currList.append[1](currDescription)
    return currList