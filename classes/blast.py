
import pygame as pg




# SCREEN 
WHITE = (255,255,255)     # screen color (rgb)     
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)



class Blast():

    def __init__(self,x,y): 

        # settings  
        image_collision = 'images/blast.png' 
        scale = 0.05

        # image 
        self.image = pg.image.load(image_collision).convert_alpha()
        self.image_blast = pg.transform.scale(self.image,(scale*int(self.image.get_width()),scale*int(self.image.get_height())))  

        # coordinates  - need to change ... 
        self.x = x
        self.y = y 

        # rectangle 
        self.rect_blast = self.image_blast.get_rect()
        self.rect_blast.topleft = (self.x,self.y)      


    def draw(self): 
        screen.blit(self.image_blast, self.rect_blast.topleft)   

     



