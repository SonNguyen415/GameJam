import pygame

MOVEMENT_SPEED = 3
SPRINT_SPEED = 6
MAX_STAMINA = 30

WHITE = (255, 255, 255)

def draw_speech_bubble(screen, text, text_colour, bg_colour, pos, size):

    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, text_colour)
    text_rect = text_surface.get_rect(midbottom=pos)

    # background
    bg_rect = text_rect.copy()
    bg_rect.inflate_ip(10, 10)

    # Frame
    frame_rect = bg_rect.copy()
    frame_rect.inflate_ip(4, 4)

    pg.draw.rect(screen, text_colour, frame_rect)
    pg.draw.rect(screen, bg_colour, bg_rect)
    screen.blit(text_surface, text_rect)



class Character(pygame.sprite.Sprite):
    def __init__(self, xLoc, yLoc):
         # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the image
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
    
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
        


