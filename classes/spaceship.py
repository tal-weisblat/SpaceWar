

import pygame as pg
from sounds.functions import bulletFired_sound
from curses import KEY_DOWN



# SCREEN 
WHITE = (255,255,255)     # screen color (rgb)     
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)


VEL_SPACESHIP = 4







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

        self.turnOff = False 

    # DRAW 
    def draw(self):
        if (not self.turnOff):
            screen.blit(self.image_spaceship, self.rect_spaceship.topleft)   


    # SPACESHIP COORDINATEs for BULLET 
    def coordinates(self):
        x = self.x 
        y = self.y 
        return (x,y)


    def width(self):
        return self.image_spaceship.get_width()

    def height(self):
        return self.image_spaceship.get_height()


    # MOVEMENT  
    def movement(self):
        
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



    def turn_off(self):
        self.turnOff = True 
    


        
        
        