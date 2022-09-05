

import pygame as pg 


SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('TicTacToe')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)



class GameOver():

    def __init__(self):

        # # GAMEOVER 
        img_gameOver   = 'images/game_over_play_again.png'
        scale_gameOver = 1
        self.image = pg.image.load(img_gameOver).convert_alpha()
        self.image_gameOver = pg.transform.scale(self.image,(scale_gameOver*int(self.image.get_width()),scale_gameOver*int(self.image.get_height())))  
        self.x_gameOver = SCREEN_WIDTH/2  - self.image_gameOver.get_width()/2
        self.y_gameOver = SCREEN_HEIGHT/2 - self.image_gameOver.get_height()/2
        self.rect_gameOver = self.image_gameOver.get_rect()
        self.rect_gameOver.topleft = (self.x_gameOver,self.y_gameOver)      
        width = self.image_gameOver.get_width()

        # YES 
        img_yes   = 'images/yes_circle.gif'
        scale_yes = 0.1
        self.image = pg.image.load(img_yes).convert_alpha()
        self.image_yes = pg.transform.scale(self.image,(scale_yes*int(self.image.get_width()),scale_yes*int(self.image.get_height())))  
        self.x_yes = self.x_gameOver   + (2/7)*self.image_gameOver.get_width()
        self.y_yes = self.y_gameOver + self.image_gameOver.get_height() + 10 
        self.rect_yes = self.image_yes.get_rect()
        self.rect_yes.topleft = (self.x_yes,self.y_yes)      
        

        # NO
        img_no   = 'images/no_circle.gif'
        scale_no = 0.1
        self.image = pg.image.load(img_no).convert_alpha()
        self.image_no = pg.transform.scale(self.image,(scale_no*int(self.image.get_width()),scale_no*int(self.image.get_height())))  
        self.x_no = self.x_gameOver + (4/7)*self.image_gameOver.get_width()
        self.y_no = self.y_gameOver + self.image_gameOver.get_height() + 10 
        self.rect_no = self.image_no.get_rect()
        self.rect_no.topleft = (self.x_no,self.y_no)      



    # NO - EXIT GAME 
    def exit_game(self, pos, mouse_clicked):
        
        # run : true or false 
        if self.rect_no.collidepoint(pos) & (pg.mouse.get_pressed()[0] == 1) & (mouse_clicked == False):    
            return False  
        else:  
            return True   


    # YES - NEW GAME 
    def new_game(self, pos, mouse_clicked):
        
        if self.rect_yes.collidepoint(pos) & (pg.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
            print ('YES') 
            mouse_clicked = True 
            return mouse_clicked
    
            
            

    def draw(self):
        screen.blit(self.image_gameOver, self.rect_gameOver.topleft)
        #screen.blit(self.image_playAgain, self.rect_playAgain.topleft)
        screen.blit(self.image_yes, self.rect_yes.topleft)
        screen.blit(self.image_no, self.rect_no.topleft)

        