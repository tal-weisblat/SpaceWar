
import pygame as pg




WHITE = (255,255,255)     # screen color (rgb)     
SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)



class Background():

    def __init__ (self):
        self.background_image = pg.image.load("images/space.jpg")
    
    def draw(self):
        screen.blit(self.background_image, (0, 0))

