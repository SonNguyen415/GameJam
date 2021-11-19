from classes import SpriteObject
from settings import *


def generate_artifacts(xLoc, yLoc, idList):
    currList = [[], []]
    for id in idList:
        artifactImg = 'Artifacts/' + ARTIFACT_LIST[id] + '.png'
        descrImg = 'ArtifactDescription/' + ARTIFACT_LIST[id] + '.png'
        currArtifact = SpriteObject(xLoc, yLoc, artifactImg, 50, 'artifact')
        currDescription = SpriteObject(100, 100, descrImg, 200, 'artifact')
        currList.append[0](currArtifact)
        currList.append[1](currDescription)
    return currList