
import pygame as pg 
import numpy as np
import time 


VEL_STAR      = 2




#WHITE = (255,255,255)     # screen color (rgb)     
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)



class Star():

    def __init__(self): 
        
        # SETTINGS 
        img_star = 'images/star.png'
        img_blast = 'images/blast.png' 
        scale_star  = 0.2
        scale_blast = 0.05


        # star-image  
        self.image = pg.image.load(img_star).convert_alpha()
        self.image_star = pg.transform.scale(self.image,(scale_star*int(self.image.get_width()),scale_star*int(self.image.get_height())))  

        # star-coordinates 
        self.x = np.random.randint(0, SCREEN_WIDTH-self.image_star.get_width())
        self.y = 0 
        
        # star-rectangle 
        self.rect_star = self.image_star.get_rect()
        self.rect_star.topleft = (self.x,self.y)           

        # --------------

        # blast image 
        self.image = pg.image.load(img_blast).convert_alpha()
        self.image_blast = pg.transform.scale(self.image,(scale_blast*int(self.image.get_width()),scale_blast*int(self.image.get_height())))  
        
        # rectangle 
        self.rect_blast = self.image_blast.get_rect()
        self.rect_blast.topleft = (self.x,self.y)      


    def initialize(self):
        self.x = np.random.randint(0, SCREEN_WIDTH-self.image_star.get_width())      
        self.y = 0


    # TEST 
    def draw(self, star_blasted, collision_time):

        self.y = self.y + VEL_STAR
        self.rect_star.topleft = (self.x,self.y) 

        time_condition = time.time() - collision_time < 1      # less than 1 second 

        if star_blasted == False:
            screen.blit(self.image_star, self.rect_star.topleft)                               
        
        if (star_blasted == True) and (time_condition == True):
            screen.blit(self.image_blast, self.rect_star.topleft) 

            
        
        # if label == 'blast':
        #     screen.blit(self.image_blast, self.rect_star.topleft)

        # if label == 'star':
        #     screen.blit(self.image_star, self.rect_star.topleft)

        




        


    # get star coordinates 
    def coordinates(self):
        return (self.x,self.y)
    
    # get star dimensions 
    def dimensions(self): 
        return (self.image_star.get_width(), self.image_star.get_height())
            
            
