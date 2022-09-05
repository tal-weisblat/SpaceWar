

import pygame as pg



WHITE = (255,255,255)     # screen color (rgb)     
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)
screen.fill(WHITE)







class Bullet():

    def __init__(self, x, y, spaceship_width):

        # settings
        image_bullet         = 'images/bullet.png'
        scale_bullet         = 0.045
        self.bullet_velocity = 13

        # image   
        self.image = pg.image.load(image_bullet).convert_alpha()
        self.image_bullet = pg.transform.scale(self.image,(scale_bullet*int(self.image.get_width()),scale_bullet*int(self.image.get_height())))  

        # coordinates
        self.x = x + (spaceship_width/2) - (self.image_bullet.get_width()/2)
        self.y = y - (self.image_bullet.get_height())

        # rectangle 
        self.rect_bullet = self.image_bullet.get_rect()
        self.rect_bullet.topleft = (self.x,self.y)     
        
    
    def initialize(self, x, y, spaceship_width):
        self.x = x + (spaceship_width/2) - (self.image_bullet.get_width()/2)
        self.y = y - (self.image_bullet.get_height())


    # UPDATE 
    def update_move(self):
        self.y = self.y - self.bullet_velocity  
        self.rect_bullet.topleft = (self.x,self.y)   


    # DRAW 
    def draw(self, bullet_hit_star):

        if (self.y > 0) and (bullet_hit_star == False): 
            
            #self.y = self.y - self.bullet_velocity  
            #self.rect_bullet.topleft = (self.x,self.y)   
            screen.blit(self.image_bullet, self.rect_bullet.topleft)
            
        
        
        


    # get coordinates 
    def coordinates(self):
        return(self.x,self.y)
    
    # get bullet dimensions 
    def dimensions(self):
        return (self.image_bullet.get_width(), self.image_bullet.get_height())
    





       