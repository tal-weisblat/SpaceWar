import pygame as pg 

SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)



class Flame():

    def __init__(self):

        scale = 0.07
        img = pg.image.load('flames/flame_1.png')
        img = pg.transform.scale(img, (img.get_width()*scale,(img.get_height()*scale)) )   # scale 
        img = pg.transform.rotate(img,270)                                                 # rotate 
        self.flame_width  = img.get_width()
        
        # for animation 
        self.index = 1       
        
        # rectangle 
        self.x = 0
        self.y = 0
        self.rect = img.get_rect()
        self.rect.topleft = (self.x,self.y)      

        # ANIMATION :list of all images 
        self.img_list = []      
        for i in range(1,11):
            img = pg.image.load(f'flames/flame_{i}.png')
            img = pg.transform.rotate(img,270)
            img = pg.transform.scale(img, (img.get_width()*scale,(img.get_height()*scale)) )
            self.img_list.append(img)

        
        
    # BELOW SPACESHIP
    def update_coordinates(self, x, y, spaceship_heigth, spaceship_width):
        self.x = x - (self.flame_width - spaceship_width)/2 
        self.y = y + spaceship_heigth + 1
        self.rect.topleft = (self.x,self.y)

    # ANIMATION
    def update_img(self):
        self.image = self.img_list[self.index]
        self.index += 1 
        if (self.index == 10): self.index = 1 
            
    # DRAW         
    def draw(self):
        screen.blit(self.image, self.rect.topleft)

