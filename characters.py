import pygame

MOVEMENT_SPEED = 3
SPRINT_SPEED = 6
MAX_STAMINA = 30

WHITE = (255, 255, 255)



class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Set our transparent color
        self.image.set_colorkey(WHITE)

        # Some character data
        self.__health = 100
        self.__recharge = 3
        self.__xLoc = xLoc
        self.__yLoc = yLoc
        self.__movementSpeed = MOVEMENT_SPEED
        self.__stamina = MAX_STAMINA
        self.__bmrTime = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.__yLoc += self.__movementSpeed
        elif key[pygame.K_UP]:
            self.__yLoc -= self.__movementSpeed
        if key[pygame.K_RIGHT]:
            self.__xLoc += self.__movementSpeed
        elif key[pygame.K_LEFT]:
            self.__xLoc -= self.__movementSpeed
        if key[pygame.K_e]:
            self.interact()
        if key[pygame.K_LSHIFT]:
            if(self.__stamina >= 3):
                self.__movementSpeed = SPRINT_SPEED
                self.__stamina -= 3
            else:
                self.__movementSpeed = MOVEMENT_SPEED
        else:
            self.restore_stamina()

    def interact(self):
        print("Interacting")

    def restore_stamina(self):
        if(self.__stamina < MAX_STAMINA):
            self.__stamina += 1

    def draw(self, surface):
        # blit yourself at your current position
        surface.blit(self.image, (self.__xLoc, self.__yLoc))

    def wounded(self, damage):
        self.__health -= damage
        if(self.__health == 0):
            pygame.quit()

    # def throw_boomerang(self, boomerang):
        # Boomerang = instance of boomerang
        # Boomerang.spawn_boomerang()
