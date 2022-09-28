

# packages 
import pygame 
import numpy  as np 
import random
import os

# classes
from classes import Background
from classes import Spaceship
from classes import Flame


# WINDOW 
WIN_WIDTH  = 500                                                
WIN_HEIGHT = 650  
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('SpaceWar')                    
pygame.init()
pygame.mixer.init()        # initiate sounds 


# COLORs
RED     = (255,0,0)      # bullet
YELLOW  = (255,255,0)    # gameover title 
PINK    = (255,192,203)  # yes & no
WHITE   = (255,255,255)
COLOR_1 = (128,255,0)
COLOR_2 = (204,102,0)
COLOR_3 = (255,0,127)
STAR_COLOR_LIST = [PINK,YELLOW,COLOR_1,COLOR_2,COLOR_3]


# BULLETs
BULLET_VEL    = 16    # bullet velociry 
BULLET_WIDTH  = 4     # bullet width 
BULLET_HEIGHT = 9     # bullet heaight 
MAGAZINE_SIZE = 3     # magazine size (at most 3 bullets on WIN)


# STARS
STAR_VEL    = 2            # CHNAGE : to something random 
STAR_WIDTH  = 30           # star dimensions 
STAR_HEIGHT = 30   
LIST_MAX_STARS = 4         # at most 3 stars on WIN 
MAX_STAR_MISED = 3


# SOUND
pygame.mixer.music.load(os.path.join('files/sounds', 'melody.mp3'))  
pygame.mixer.music.play()
BULLET_FIRED_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'bullet_fired.mp3'))
BLAST_SOUND        = pygame.mixer.Sound(os.path.join('files/sounds', 'blast.wav'))
GAME_OVER_SOUND    = pygame.mixer.Sound(os.path.join('files/sounds', 'game_over.wav'))


# FONT 
GAME_OVER_FONT  = pygame.font.SysFont('comicsans', 40)             
NEW_GAME_FONT   = pygame.font.SysFont('comicsans', 25)
YES_AND_NO_FONT = pygame.font.SysFont('comicsans', 25) 
MISSED_FONT     = pygame.font.SysFont('comicsans', 20)
