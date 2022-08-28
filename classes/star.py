
import pygame as pg 
import numpy as np
import time 


VEL_STAR      = 1




WHITE = (255,255,255)     # screen color (rgb)     
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



    # DRAW 
    def draw(self, bullet_collided_star, bullet_collided_star_time):

        # falling star 
        if (self.y < SCREEN_HEIGHT) and (bullet_collided_star == False):             
            self.y = self.y + VEL_STAR
            self.rect_star.topleft = (self.x,self.y)
            screen.blit(self.image_star, self.rect_star.topleft)
            
            return bullet_collided_star


        # COLLISION 
        elif (self.y < SCREEN_HEIGHT) and (bullet_collided_star == True):
            
            # BLAST for 2-SECONDS
            if (time.time()<bullet_collided_star_time +2):
                self.y = self.y + VEL_STAR
                self.rect_star.topleft = (self.x,self.y) 
                screen.blit(self.image_blast, self.rect_star.topleft)

                bullet_collided_star = True                 
                return bullet_collided_star
            
            else: 
                # NEW STAR
                self.x = np.random.randint(0, SCREEN_WIDTH-self.image_star.get_width())      
                self.y = 0
                self.rect_star.topleft = (self.x,self.y) 
                screen.blit(self.image_star, self.rect_star.topleft)   

                
                
                bullet_collided_star = False                 
                return bullet_collided_star
            
            
        
        else:
            # NEW STAR
            self.x = np.random.randint(0, SCREEN_WIDTH-self.image_star.get_width())      
            self.y = 0
            self.rect_star.topleft = (self.x,self.y) 
            screen.blit(self.image_star, self.rect_star.topleft)   

            bullet_collided_star = False                 
            return bullet_collided_star

        


    # get star coordinates 
    def get_coordinates(self):
        return (self.x,self.y)
    
    # get star dimensions 
    def get_dimensions(self): 
        return (self.image_star.get_width(), self.image_star.get_height())
            
            
