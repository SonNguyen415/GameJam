import pygame
import pygame.font
from settings import *
from dungeon_generation import *
import time
import math
import random

pygame.font.init()










class Playground():
    def __init__(self):
        self.image = pygame.image.load("Backgrounds/Base Room.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (WINDOW_LENGTH, WINDOW_HEIGHT))

        self.spriteList = []
        self.currArtifactNames = []
        self.currArtifacts = [[], []]
        self.numArtifacts = 0

    def draw(self, surface):
        surface.blit(self.image, (0, 0))

    def initiate_doors(self):
        for i in playerGrid[playerPosition[1]][playerPosition[0]]:
            if i == 'N':
                north = SpriteObject(470,40, 'Objects/Door.png', 50, 'door', 'N')
                self.spriteList.append(north)
                north.draw(screen)
            elif i == 'S':
                south = SpriteObject(470,502, 'Objects/Door.png', 50, 'door', 'S')
                self.spriteList.append(south)
                south.rotate(180)
                south.draw(screen)
            elif i == 'W':
                west = SpriteObject(104,264, 'Objects/Door.png', 50, 'door', 'W')
                self.spriteList.append(west)
                west.rotate(90)
                west.draw(screen)
            elif i == 'E':
                east = SpriteObject(838,264, 'Objects/Door.png', 50, 'door', 'E')
                self.spriteList.append(east)
                east.rotate(270)
                'yes'
                east.draw(screen)



    def get_current_artifacts(self):
        idList = []
        ctr = 0
        prevID = random.randint(0, len(artifactList) - 1)
        while ctr < self.numArtifacts:
            currID = random.randint(0, len(artifactList) - 1)
            if currID != prevID:
                idList.append(currID)
                prevID = currID
        for id in idList:
            myArtifact = artifactList.pop[id]
            self.currArtifactNames.append(myArtifact)


    def artifact_x(currID):
        xMod = (currID - 1) % 3
        return 100+xMod*50


    def artifact_y(currID):
        yMod = (currID - 1) /  3
        return 100+yMod*50


    def append_artifacts(self):
        for artifact, i in enumerate(self.currArtifactNames):
            xLoc = self.artifact_x(i)
            yLoc = self.artifact_y(i)
            artifactImg = 'Artifacts/' + artifact + '.png'
            descrImg = 'Artifact Descriptions/' + artifact + '.png'
            artifactObj = SpriteObject(xLoc, yLoc, artifactImg, 50, 'artifact')
            artifactDescr = SpriteObject(200, 200, descrImg, 300, 'description')
            self.currArtifacts.append(artifactObj)
            self.artifactDescr.appen(artifactDescr)
            self.spriteList.append(artifactObj)


    def generate_artifacts(self):
        self.get_current_artifacts()
        self.append_artifacts()


    def generate_sprites(self):

        return

    def updateMap(self):
        while len(self.spriteList) > 1:
            self.spriteList.pop(1)
        if playerGrid[playerPosition[1]][playerPosition[0]] == 'B':
            playerGrid[playerPosition[1]][playerPosition[0]] = grid[playerPosition[1]][playerPosition[0]]

        self.initiate_doors()
        self.generate_sprites()




class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, iconImg, imageSize, objType, rotation = 'C'):
         # Call the parent class (Sprite) constructor
        super().__init__()
        self.type = objType

        self.xLoc = xLoc
        self.yLoc = yLoc

        self.unlocked = False
        self.rot = rotation

        self.image = pygame.image.load(iconImg)

        self.image = pygame.transform.scale(self.image, (imageSize, imageSize))
        self.rect = self.image.get_rect(topleft=(self.xLoc, self.yLoc))

    def draw(self, surface):
        surface.blit(self.image, (self.xLoc, self.yLoc))

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

    def draw(self, surface):
        surface.blit(self.image, (self.xLoc, self.yLoc))


    def change_position(self):
        if self.rot == 'N':
            playerPosition[1] -= 1
        elif self.rot == 'S':
            playerPosition[1] += 1
        elif self.rot == 'W':
            playerPosition[0] -= 1
        elif self.rot == 'E':
            playerPosition[0] += 1


        # Temporarily, the Artifact generation code will be placed here










class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc, charImg, objID):
         # Call the parent class (Sprite) constructor
        super().__init__()

        self.id = objID

        self.xLoc = xLoc
        self.yLoc = yLoc
        self.orientation = DOWN

        # Load the image
        self.sprites = charImg
        self.currSprite = 0
        self.image = self.sprites[DOWN][self.currSprite]

        self.image = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))

        self.rect = self.image.get_rect(topleft=(self.xLoc, self.yLoc))


        # Set our transparent color
        self.image.set_colorkey(COLOR_WHITE)


        # Some character data
        self.health = 10
        self.dead = False
        self.canMoveUp = True
        self.canMoveDown = True
        self.canMoveLeft = True
        self.canMoveRight = True
        self.movementSpeed = WALK_SPEED
        self.slappable = False

    def draw(self, surface):
        # blit yourself at your current position
        if(self.dead):
            return
        if(self.orientation == UP):
            self.image = self.sprites[UP][self.currSprite]
        if(self.orientation == DOWN):
            self.image = self.sprites[DOWN][self.currSprite]
        if(self.orientation == LEFT):
            self.image = self.sprites[LEFT][self.currSprite]
        if(self.orientation == RIGHT):
            self.image = self.sprites[RIGHT][self.currSprite]
        self.image = pygame.transform.scale(self.image, (CHAR_WIDTH, CHAR_HEIGHT))
        surface.blit(self.image, (self.xLoc, self.yLoc))

    def wounded(self, damage):
        self.health -= damage
        if(self.health == 0):
            self.dead = True


    def increment_sprite(self):
        if(self.currSprite < 2):
            self.currSprite += 1
        else:
            self.currSprite = 0

    def update_rect(self):
        if(self.dead):
            return
        self.rect.update(self.xLoc, self.yLoc, CHAR_WIDTH, CHAR_HEIGHT)


    def collision_enforcement(self, eachSprite):
        if(-POS_TOLERANCE < eachSprite.rect.top - self.rect.bottom  <= 0):
            self.canMoveDown = False
        if(-POS_TOLERANCE < self.rect.top - eachSprite.rect.bottom <= -POS_TOLERANCE/2):
            self.canMoveUp = False
        if(-POS_TOLERANCE < self.rect.left - eachSprite.rect.right < POS_TOLERANCE):
            self.canMoveLeft = False
        if(-POS_TOLERANCE < eachSprite.rect.left - self.rect.right < POS_TOLERANCE):
            self.canMoveRight = False




    def check_collision(self, playArea):
        self.canMoveLeft = True
        self.canMoveRight = True
        self.canMoveDown = True
        self.canMoveUp = True
        for eachSprite in playArea.spriteList:
            if(eachSprite.type == self.type):
                pass
            else:
                if(self.rect.colliderect(eachSprite.rect)):
                    self.collision_enforcement(eachSprite)
                    if eachSprite.type == "door" and self.type == "player" and eachSprite.unlocked:

                        playArea.updateMap()
                        eachSprite.change_position()


                        self.xLoc = WINDOW_LENGTH/2
                        self.yLoc = PLAYGROUND_HEIGHT
                        time.sleep(0.1)
                        return
                    if(eachSprite.type == "player" and self.type == "npc"):
                        self.slappable = True



class Player(Character, object):
    def __init__(self, xLoc, yLoc, charImg, objID):
        Character.__init__(self, xLoc, yLoc, charImg, objID)

        self.type = "player"
        self.__staminaRecharge = 0
        self.__stamina = MAX_STAMINA
        self.speaking = False



    def slapped(self):
        self.wounded(1)

    def move(self):
        if(self.dead):
            return
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and self.yLoc+CHAR_HEIGHT <= PLAYGROUND_HEIGHT+PLAYGROUND_Y_OFFSET and self.canMoveDown:
            self.yLoc += self.movementSpeed
            self.orientation = DOWN
            self.increment_sprite()
        elif key[pygame.K_UP] and PLAYGROUND_Y_OFFSET <= self.yLoc+CHAR_HEIGHT-10 and self.canMoveUp:
            self.yLoc -= self.movementSpeed
            self.orientation = UP
            self.increment_sprite()
        if key[pygame.K_RIGHT] and self.xLoc+CHAR_WIDTH <= PLAYGROUND_LENGTH+PLAYGROUND_X_OFFSET and self.canMoveRight:
            self.xLoc += self.movementSpeed
            self.orientation = RIGHT
            self.increment_sprite()
        elif key[pygame.K_LEFT] and PLAYGROUND_X_OFFSET <= self.xLoc and self.canMoveLeft:
            self.xLoc -= self.movementSpeed
            self.orientation = LEFT
            self.increment_sprite()
        if key[pygame.K_LSHIFT]:
            if(self.__stamina >= 3):
                self.movementSpeed = SPRINT_SPEED
                self.__stamina -= 3
            else:
                self.movementSpeed = WALK_SPEED
        elif (self.__staminaRecharge < STAMINA_RECHARGE_TIME):
            self.__staminaRecharge += 1
        else:
            self.__staminaRecharge = 0
            self.restore_stamina()




    def restore_stamina(self):
        if(self.__stamina < MAX_STAMINA):
            self.__stamina += 5

    def get_stamina_ratio(self):
        if MAX_STAMINA > 0:
            return self.__stamina / MAX_STAMINA
        return 0

    def spawn_boomerang(self, surface):
        bmrX = self.xLoc + CHAR_WIDTH/2
        bmrY = self.yLoc + CHAR_HEIGHT/2
        bmr = Boomerang(bmrX, bmrY)
        bmr.draw(surface)
        return bmr



    def generate_text(self, surface):
        font = pygame.font.SysFont('Arial', 10)
        textsurface  = font.render('Press e to view artifact', False, COLOR_WHITE).convert_alpha()
        surface.blit(textsurface, (self.xLoc,self.yLoc))





class Enemy (Character, object):
    def __init__(self, xLoc, yLoc, charImg, objID):
        Character.__init__(self, xLoc, yLoc, charImg, objID)

        self.type = "npc"
        self.sightLength = 300
        self.__movementSpeed = WALK_SPEED + 1
        self.agro = False
        self.fiveSec = True
        self.coolDown = False

    def sense(self, pxLoc, pyLoc):
        if self.health < 10:
            self.agro = True
        #find distance of npc to player
        distance = math.sqrt(((self.xLoc-pxLoc)**2)+((self.yLoc-pyLoc)**2))
        #find the range of sight
        leftRange = (self.orientation*45)-45
        rightRange = (self.orientation*45)+45
        #find the angle from npc to character
        angle = math.degrees(math.atan2(pyLoc + (CHAR_WIDTH/2) - self.yLoc, pxLoc + (CHAR_HEIGHT/2) - self.xLoc))
        #if distance is less than sight length
        if (distance<self.sightLength):
            #if angle is between
            if (angle>leftRange and angle<rightRange):
                self.agro = True


    def move_towards_player(self, x, y):
        if self.dead:
            return
        distX = x - self.xLoc
        distY = y - self.yLoc
        dist = math.sqrt((distX*distX)+(distY*distY))

        if distX < 0 and self.canMoveLeft:
            self.xLoc += (distX/dist) * self.movementSpeed
            self.increment_sprite()

        if distX > 0 and self.canMoveRight:
            self.xLoc += (distX / dist) * self.movementSpeed
            self.increment_sprite()
        if distY < 0 and self.canMoveUp:
            self.yLoc += (distY/dist) * self.movementSpeed
            self.increment_sprite()

        if distY > 0 and self.canMoveDown:
            self.yLoc += (distY / dist) * self.movementSpeed
            self.increment_sprite()


        if abs(distX) > abs(distY):
            if distX<0:
                self.orientation = LEFT
            else:
                self.orientation = RIGHT
        else:
            if(distY<0):
                self.orientation = UP
            else:
                self.orientation = DOWN

    def whacked(self):
        self.wounded(BMR_DMG)

    def slaps(self, player):
        if not self.coolDown:
            if self.slappable:
                player.slapped()
                self.slappable = False
                self.coolDown = True

    def random_movement(self, k):
        if k == 1 and self.yLoc + CHAR_HEIGHT <= PLAYGROUND_HEIGHT-PLAYGROUND_Y_OFFSET and self.canMoveDown:
            #Move down
            self.orientation = DOWN
            self.yLoc += self.__movementSpeed
            self.increment_sprite()

        elif k == 2 and PLAYGROUND_Y_OFFSET <= self.yLoc and self.canMoveUp:
            #Move up
            self.orientation = UP
            self.yLoc -= self.__movementSpeed
            self.increment_sprite()

        elif k == 3 and self.xLoc + CHAR_WIDTH <= PLAYGROUND_LENGTH+PLAYGROUND_X_OFFSET and self.canMoveRight:
            #Move right
            self.orientation = RIGHT
            self.xLoc += self.__movementSpeed
            self.increment_sprite()

        elif k == 4 and PLAYGROUND_X_OFFSET <= self.xLoc and self.canMoveLeft:
            #Move left
            self.orientation = LEFT
            self.xLoc -= self.__movementSpeed
            self.increment_sprite()




class Boomerang(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        self.xLoc = xLoc
        self.yLoc = yLoc

        self.image = pygame.image.load("Objects/icon.png")
        self.image = pygame.transform.scale(self.image, (BOOMERANG_SIZE, BOOMERANG_SIZE))

        self.rect = self.image.get_rect(topleft=(self.xLoc, self.yLoc))

        self.returning = False
        self.direction = []
        self.currSpeed = 0
        self.accel = 0


        self.tick = 0
        self.fire = True

    def draw(self, surface):
        surface.blit(self.image, (self.xLoc, self.yLoc))


    def check_collision(self):
        if(self.xLoc > PLAYGROUND_LENGTH+WALL_HEIGHT/2 or self.xLoc < PLAYGROUND_HEIGHT+WALL_HEIGHT/2 or
            self.yLoc > PLAYGROUND_HEIGHT+WALL_HEIGHT/2 or self.yLoc < PLAYGROUND_HEIGHT+WALL_HEIGHT/2):
            return True
        return False

    def check_at_set_point(self, xSetPoint, ySetPoint):
        if ((xSetPoint - LOC_TOLERANCE <= self.xLoc <= xSetPoint + LOC_TOLERANCE and
        ySetPoint - LOC_TOLERANCE <= self.yLoc  <= ySetPoint + LOC_TOLERANCE) or
        (-SPEED_TOLERANCE <= self.currSpeed/2 <= SPEED_TOLERANCE)):
            return True
        return False


    def check_finish(self, bmrTime, surface, myPlayer):
        if (bmrTime >= BOOMERANG_TIME or
        (self.returning == True and self.get_distance(myPlayer.xLoc, myPlayer.yLoc) < 40)):

            time.sleep(0.01)
            return True
        return False


    def find_a(self, xSetPoint, ySetPoint, myPlayer):
        x = xSetPoint - (myPlayer.xLoc + CHAR_WIDTH/2) + 3
        y = ySetPoint - (myPlayer.yLoc + CHAR_HEIGHT/2) + 3
        length = (x**2 + y**2)**0.5
        if length > MAX_BMR_DISTANCE:
            x = x/length * MAX_BMR_DISTANCE
            y = y/length * MAX_BMR_DISTANCE
        aX = -x/(BOOMERANG_TIME/2)**2
        aY = -y/(BOOMERANG_TIME/2)**2
        return (aX**2 + aY**2)**0.5

    def find_normalized_dir(self, xLoc, yLoc):
        x = self.xLoc - xLoc
        y = self.yLoc - yLoc
        length = (x**2 + y**2)**0.5
        if length != 0:
            return [x/length, y/length]
        return [0,0]

    def find_normalized_dir_player(self, xLoc, yLoc):
        return self.find_normalized_dir(xLoc + CHAR_WIDTH/2 - 3, yLoc + CHAR_HEIGHT/2 - 3)

    def get_distance(self, xLoc, yLoc):
        x = self.xLoc - xLoc
        y = self.yLoc - yLoc
        return (x**2 + y**2)**0.5


    def move_boomerang(self, surface, xSetPoint, ySetPoint, player, spriteList):
        self.currSpeed = min(self.currSpeed + self.accel, BOOMERANG_MAX_SPEED)
        if not self.returning:
            if(self.check_at_set_point(xSetPoint, ySetPoint)):
                self.returning = True

            self.xLoc += self.direction[0] * self.currSpeed
            self.yLoc += self.direction[1] * self.currSpeed
            if self.xLoc < 120 or self.xLoc > 870:
                if self.xLoc < 120:
                    self.xLoc = 120
                else:
                    self.xLoc = 870
                self.returning = True
                self.currSpeed = 0
            if self.yLoc < 100 or self.yLoc > 490:
                if self.yLoc < 100:
                    self.yLoc = 100
                else:
                    self.yLoc = 490
                self.returning = True
                self.currSpeed = 0
        else:
            direction = self.find_normalized_dir_player(player.xLoc, player.yLoc)
            self.xLoc -= direction[0] * self.currSpeed
            self.yLoc -= direction[1] * self.currSpeed
        self.rect = self.image.get_rect(topleft=(self.xLoc, self.yLoc))
        self.draw(surface)
        for sprite in spriteList:
            if self.rect.colliderect(sprite.rect):
                if sprite.type == "npc":
                    if not self.returning:
                        self.returning = True
                        self.currSpeed = 0
                        sprite.whacked()
                    else:
                        sprite.whacked()

                elif sprite.type != "player":
                    if not self.returning:
                        self.returning = True
                        self.currSpeed = 0



    def spawn_boomerang(self, x, y, myPlayer):
        self.returning = False
        self.accel = 2*self.find_a(x, y, myPlayer)
        self.currSpeed = -self.accel*BOOMERANG_TIME/2
        self.direction = self.find_normalized_dir(x, y)
