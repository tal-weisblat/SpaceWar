

import pygame as pg
from sounds.functions import bullet_fired_sound
from curses import KEY_DOWN



# SCREEN 
WHITE = (255,255,255)     # screen color (rgb)     
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)
#screen.fill(WHITE)


# velocities 
VEL_SPACESHIP = 3
VEL_BULLET    = 5






class Spaceship():
    
    def __init__ (self, x, y):

        # SETTINGS  
        image_spaceship = 'images/spaceship.png'
        scale_spaceship  = 0.09

        # image
        self.image = pg.image.load(image_spaceship).convert_alpha()
        self.image_spaceship = pg.transform.scale(self.image,(scale_spaceship*int(self.image.get_width()),scale_spaceship*int(self.image.get_height())))  

        # coordinates 
        self.x = x 
        self.y = y 
        
        # rectangle 
        self.rect_spaceship = self.image_spaceship.get_rect()
        self.rect_spaceship.topleft = (self.x,self.y)     # adjusting according to coordinates 

        

    # DRAW 
    def draw(self):
        screen.blit(self.image_spaceship, self.rect_spaceship.topleft)   


    # SPACESHIP COORDINATEs for BULLET 
    def coordinates(self):
        x = self.x 
        y = self.y 
        return (x,y)


    def width(self):
        return self.image_spaceship.get_width()


    # MOVEMENT  
    def move_spaceship(self):
        
        keys = pg.key.get_pressed()        
        # RIGHT 
        if keys[pg.K_RIGHT]:
            self.x = self.x + VEL_SPACESHIP 
            self.rect_spaceship.topleft = (self.x,self.y)
        # LEFT 
        if keys[pg.K_LEFT]:
            self.x = self.x - VEL_SPACESHIP 
            self.rect_spaceship.topleft = (self.x,self.y)
        # UP 
        if keys[pg.K_DOWN]:
            self.y = self.y + VEL_SPACESHIP
            self.rect_spaceship.topleft = (self.x,self.y)   
        # DOWN
        if keys[pg.K_UP]:
            self.y = self.y - VEL_SPACESHIP
            self.rect_spaceship.topleft = (self.x,self.y)   

    


        
        
        