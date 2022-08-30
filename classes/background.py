
import pygame as pg




WHITE = (255,255,255)     # screen color (rgb)     
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)



class Background():

    def __init__ (self):
        
        image = pg.image.load("images/background.jpg")
        # rescaling image according to screen
        self.background_image = pg.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))      

        self.y = 0
        
    
    def draw(self):

        self.y = self.y + 1

        screen.blit(self.background_image, (0, self.y))
        screen.blit(self.background_image, (0, self.y -  SCREEN_HEIGHT))

        if self.y ==  SCREEN_HEIGHT:
            self.y = 0 
              

