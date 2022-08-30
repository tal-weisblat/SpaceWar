

import pygame as pg 


SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)



class GameOver():

    def __init__(self):

        # settings
        img_game_over = 'images/game_over.png'
        scale  = 0.2
        
        # star-image  
        self.image = pg.image.load(img_game_over).convert_alpha()
        self.image_game_over = pg.transform.scale(self.image,(scale*int(self.image.get_width()),scale*int(self.image.get_height())))  

        # star-coordinates 
        self.x = SCREEN_WIDTH/2  - self.image_game_over.get_width()/2
        self.y = SCREEN_HEIGHT/2 - self.image_game_over.get_height()/2
        
        # star-rectangle 
        self.rect_game_over = self.image_game_over.get_rect()
        self.rect_game_over.topleft = (self.x,self.y)           


    def draw(self):
        screen.blit(self.image_game_over, self.rect_game_over.topleft)

