
import pygame as pg 
import numpy as np
import time 





<<<<<<< HEAD
=======



>>>>>>> changeBullets
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)





class Star():

    def __init__(self): 
        
        # SETTINGS 
        img_star  = 'images/falling_star/falling_star_1.png'
        img_blast = 'images/blast.png' 
        scale_star       = 0.17
        scale_blast      = 0.05
        self.velocity    = 2
        self.turnOff     = False

        # STAR  
        self.image = pg.image.load(img_star).convert_alpha()
        self.image_star = pg.transform.scale(self.image,(scale_star*int(self.image.get_width()),scale_star*int(self.image.get_height())))  
        self.x = np.random.randint(0, SCREEN_WIDTH-self.image_star.get_width())
        self.y = 0 
        self.rect = self.image_star.get_rect()
        self.rect.topleft = (self.x,self.y)          


        self.status = 'not blasted'

        # ANIMATION
        self.index = 0
        self.image_list = []      
        for i in range(1,11):
            img = pg.image.load(f'images/falling_star/falling_star_{i}.png')
            img = pg.transform.rotate(img,90)
            img = pg.transform.scale(img, (img.get_width()*scale_star,(img.get_height()*scale_star)) )
            self.image_list.append(img) 

        # BLAST 
        self.image = pg.image.load(img_blast).convert_alpha()
        self.image_blast = pg.transform.scale(self.image,(scale_blast*int(self.image.get_width()),scale_blast*int(self.image.get_height())))  
        self.rect_blast = self.image_blast.get_rect()
        self.rect_blast.topleft = (self.x,self.y)      

         


    # ANIMATION
    def update_image(self):
        self.image = self.image_list[self.index]
        self.index += 1 
        if (self.index == 5): self.index = 0
    

   
        
    # NEW DRAW METHOD 
    def draw_star(self):
        
        self.y += self.velocity
        rect    = self.rect_star
        rect.topleft = (self.x,self.y) 
        
        if self.status == 'blasted':
            screen.blit(self.image_blast, self.rect_star.topleft) 

        else: 
            image = self.image_list[self.index]
            screen.blit(image, rect.topleft)                               


    # INIT 
    def initialize(self):
        self.x = np.random.randint(0, SCREEN_WIDTH-self.image_star.get_width())      
        self.y = 0
        self.velocity = np.random.randint(2,5)


    # DRAW  
    def draw(self, star_blasted, collision_time):

        if (not self.turnOff): 
            self.y = self.y + self.velocity
            self.rect.topleft = (self.x,self.y) 
            time_condition = time.time() - collision_time < 1      # less than 1 second 

            # STAR 
            if star_blasted == False:                
                image = self.image_list[self.index]                                
                screen.blit(image, self.rect.topleft)                               
            
            # BLAST 
            if (star_blasted == True) and (time_condition == True):      
                screen.blit(self.image_blast, self.rect.topleft) 


    
    # COORDINATES 
    def y_coordinate(self):
        return self.y
    
    # DIMENSIONS
    def dimensions(self): 
        return (self.image_star.get_width(), self.image_star.get_height())

    


    def turn_off(self):
        self.turnOff = True

            
            
