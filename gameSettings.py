


import pygame 
import numpy  as np 
import random
import os


from gameObjects.background import Background
from gameObjects.spaceship import Spaceship
from gameObjects.flame import Flame


# from gameDraw.drawGameOver import drawGameOver
# from gameDraw.drawGame import drawGame
# from gameObjects.starsAndBullets import drawStars, addStar, handle_stars_and_bullets
# from gameObjects.starsAndBullets import drawBullets, handleBullets, addBullets



# WINDOW 
WIN_WIDTH  = 500                                                
WIN_HEIGHT = 650  
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('SpaceWar')                    
pygame.init()
pygame.mixer.init()        


# COLORs
RED     = (255,0,0)      
YELLOW  = (255,255,0)    
PINK    = (255,192,203)  
WHITE   = (255,255,255)
COLOR_1 = (128,255,0)
COLOR_2 = (204,102,0)
COLOR_3 = (255,0,127)
STAR_COLOR_LIST = [PINK,YELLOW,COLOR_1,COLOR_2,COLOR_3]


# BULLETs
BULLET_VEL    = 16   
BULLET_WIDTH  = 4    
BULLET_HEIGHT = 9    
MAGAZINE_SIZE = 3    


# STARS
STAR_VEL    = 2           
STAR_WIDTH  = 30          
STAR_HEIGHT = 30   
LIST_MAX_STARS = 4        
MAX_STAR_MISED = 3


# SOUND
pygame.mixer.music.load(os.path.join('soundFiles', 'music.mp3'))  
pygame.mixer.music.play()
BULLET_FIRED_SOUND = pygame.mixer.Sound(os.path.join('soundFiles', 'shooting.wav'))
BLAST_SOUND        = pygame.mixer.Sound(os.path.join('soundFiles', 'blast.wav'))
GAME_OVER_SOUND    = pygame.mixer.Sound(os.path.join('soundFiles', 'gameOver.wav'))


# FONT 
GAME_OVER_FONT  = pygame.font.SysFont('comicsans', 40)             
NEW_GAME_FONT   = pygame.font.SysFont('comicsans', 25)
YES_AND_NO_FONT = pygame.font.SysFont('comicsans', 25) 
MISSED_FONT     = pygame.font.SysFont('comicsans', 20)


# TEXTS
gameOver_text    = GAME_OVER_FONT.render('Game over',1, YELLOW)      
playAgain_text   = NEW_GAME_FONT.render('Play again ?',1, PINK)
or_text          = YES_AND_NO_FONT.render('or',1,PINK)
yes_text         = YES_AND_NO_FONT.render('Yes',1, PINK)
no_text          = YES_AND_NO_FONT.render('No',1, PINK) 



# EVENTS 
EXIT_GAME   = pygame.USEREVENT + 1
STAR_HIT    = pygame.USEREVENT + 2  
MISSED_STAR = pygame.USEREVENT + 3 
NEW_GAME    = pygame.USEREVENT + 4 
