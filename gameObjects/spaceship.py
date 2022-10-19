
from gameSettings import *



# ----------------------------------------- SPACESHIP -------------------------------------------
VEL_SPACESHIP = 5
class Spaceship():
    
    def __init__ (self, GAME_WIDTH, GAME_HEIGHT, x, y, window): 
        self.win = window
        self.game_width = GAME_WIDTH
        self.game_height = GAME_HEIGHT
        image_spaceship = 'imageFiles/spaceship_1.png'
        scale_spaceship  = 0.06
        self.image = pygame.image.load(image_spaceship).convert_alpha()
        self.image_spaceship = pygame.transform.scale(self.image,(scale_spaceship*int(self.image.get_width()),scale_spaceship*int(self.image.get_height())))  
        self.x = x 
        self.y = y 
        self.rect_spaceship = self.image_spaceship.get_rect()
        self.rect_spaceship.topleft = (self.x,self.y)    

    # DRAW 
    def draw(self):
        self.win.blit(self.image_spaceship, self.rect_spaceship.topleft)   
 
    def coordinates(self): return (self.x, self.y)              # SPACESHIP COORDINATEs for BULLET 
    def width(self): return self.image_spaceship.get_width()    # WIDTH
    def height(self): return self.image_spaceship.get_height()  # HEIGHT 

    # MOVEMENT  
    def movement(self):
        keys = pygame.key.get_pressed()         
        if keys[pygame.K_RIGHT] and (self.x < self.game_width - self.image_spaceship.get_width()):   # RIGHT
            self.x = self.x + VEL_SPACESHIP        # RIGHT 
            self.rect_spaceship.topleft = (self.x,self.y)
        if keys[pygame.K_LEFT] and (self.x >0):    # LEFT 
            self.x = self.x - VEL_SPACESHIP 
            self.rect_spaceship.topleft = (self.x,self.y)
        if keys[pygame.K_DOWN] and (self.y < self.game_height - self.image_spaceship.get_height()):    # DOWN
            self.y = self.y + VEL_SPACESHIP         # DOWN
            self.rect_spaceship.topleft = (self.x,self.y)   
        if keys[pygame.K_UP] and (self.y > 0):      # UP
            self.y = self.y - VEL_SPACESHIP
            self.rect_spaceship.topleft = (self.x,self.y)   


