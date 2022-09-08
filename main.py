


# TODO 






# packages  
from os import sysconf
import pygame as pygame
import numpy  as np 
import time   as t 


pygame.init()
 
# classes
from classes.background import Background
from classes.spaceship  import Spaceship
from classes.game_over  import GameOver
from classes.flame      import Flame
 
# sounds 
from sounds.functions import blast_sound
from sounds.functions import bulletFired_sound
from sounds.functions import gameOver_sound


# initilize objects  
background = Background()
spaceship  = Spaceship(280,490)
gameOver   = GameOver()
flame      = Flame()


# MUSIC (background)
pygame.mixer.init()
pygame.mixer.music.load('sounds/files/melody.mp3')
pygame.mixer.music.play()

# WIN
WIN_WIDTH  = 500                                                
WIN_HEIGHT = 650  
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('SpaceWar')                    


# COLORs
RED     = (255,0,0)      # bullet
YELLOW  = (255,255,0)    # stars & game-over 
PINK    = (255,192,203)  # yes & no


# BULLETs
bullet_list   = []    # the one that's going to contain all bullets
BULLET_VEL    = 15    # bullet velociry 
BULLET_WIDTH  = 5     # bullet width 
BULLET_HEIGHT = 10    # bullet heaight 
BULLET_MAX    = 2     # magazine size (at most 3 bullets on WIN)




# STARs
star_list   = []           # contain all stars present on WIN 
STAR_VEL    = 3            # CHNAGE : to something random 
STAR_WIDTH  = 40           # star dimensions 
STAR_HEIGHT = 50   
STAR_MAX    = 2            # at most 3 stars on WIN 



# EVENTS 
GAME_OVER = pygame.USEREVENT + 1
EXIT_GAME = pygame.USEREVENT + 2 

# FONT 
GAME_OVER_FONT  = pygame.font.SysFont('comicsans', 40)             
NEW_GAME_FONT   = pygame.font.SysFont('comicsans', 25)
YES_AND_NO_FONT = pygame.font.SysFont('comicsans', 25)             

# RENDER: text, collor  
gameOver_text   = GAME_OVER_FONT.render('Game over',1, YELLOW)      
playAgain_text  = NEW_GAME_FONT.render('Play again ?',1, PINK)
or_text         = YES_AND_NO_FONT.render('or',1,PINK)
yes_text        = YES_AND_NO_FONT.render('Yes',1, PINK)
no_text         = YES_AND_NO_FONT.render('No',1, PINK) 






# DRAW BULLETS 
def draw_bullets(bullet_list):
    for bullet in bullet_list:
        pygame.draw.rect(WIN, RED, bullet)


# HANDLE BULLETS 
def handle_bullets(bullet_list, star_list): 
    
    for bullet in bullet_list: 
        # movement on WIN   
        bullet.y -= BULLET_VEL                  
        # reached top WIN
        if bullet.y < 0: bullet_list.remove(bullet)    


# DRAW STARS          
def draw_stars(star_list):    
    
    for star in star_list:
        pygame.draw.rect(WIN, YELLOW, star)


# ADD NEW STARs
def add_new_stars(star_list):
    
    if len(star_list) < STAR_MAX :
        x = np.random.randint(0, WIN_WIDTH - STAR_WIDTH) 
        star = pygame.Rect(x, 0, STAR_WIDTH, STAR_HEIGHT)       
        star_list.append(star) 


# COLLISION 
def handle_stars_and_bullets(bullet_list, star_list): 
    
    for star in star_list:

        star.y += STAR_VEL

        # star reached buttom - game over 
        if star.y > WIN_HEIGHT:             
            pygame.event.post(pygame.event.Event(GAME_OVER))         # posting GAME_OVER event  

        # star & bullet collided 
        for bullet in bullet_list: 
            if star.colliderect(bullet): 
                
                blast_sound()
                bullet_list.remove(bullet)                              # remove bullet (from list) 
                star_list.remove(star)                                  # remove star   (from list)
            


def finalWindow_draw(gameOver_text, playAgain_text, yes_text, or_text, no_text, pos, mouse_clicked):
    gameOverText_width  = gameOver_text.get_width()
    gameOverText_height = gameOver_text.get_height()  
    playAgain_width  = playAgain_text.get_width()
    playAgain_height = playAgain_text.get_height()
    yesText_width  = yes_text.get_width()
    yesText_height = yes_text.get_height()
    orText_width = or_text.get_width()
    noText_height = no_text.get_height()


    # DRAW 
    WIN.blit( gameOver_text, (WIN_WIDTH/2 - gameOverText_width/2 , WIN_HEIGHT/2 - gameOverText_height))
    WIN.blit(playAgain_text, (WIN_WIDTH/2 - playAgain_width/2, WIN_HEIGHT/2 - playAgain_height/2 + 20))
    WIN.blit( yes_text,      (WIN_WIDTH/2 - playAgain_width/2, WIN_HEIGHT/2 - yesText_height/2 + 50))            
    WIN.blit( or_text, (WIN_WIDTH/2 - playAgain_width/2 + yesText_width + 10 , WIN_HEIGHT/2 - yesText_height/2 + 50 ) )   
    WIN.blit( no_text, (WIN_WIDTH/2 - playAgain_width/2 + yesText_width + 10 + orText_width + 10, WIN_HEIGHT/2 - noText_height/2 + 50))         

    # RECT
    yes_rect = yes_text.get_rect()
    yes_rect.topleft = (WIN_WIDTH/2 - playAgain_width/2, WIN_HEIGHT/2 - yesText_height/2 + 50 ) 
    no_rect = no_text.get_rect()
    no_rect.topleft = (WIN_WIDTH/2 - playAgain_width/2 + yesText_width + 10 + orText_width + 10, WIN_HEIGHT/2 - noText_height/2 + 50 )

    # mouse cursor position 
    pos = pygame.mouse.get_pos()
    
    # taking action 
    if yes_rect.collidepoint(pos) & (pygame.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
        main()
    if no_rect.collidepoint(pos) & (pygame.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
        pygame.event.post(pygame.event.Event(EXIT_GAME)) 
        print ('need to break')    
    
    



def main():

    star_list   = []
    game_over = False 
    mouse_clicked = False 
    clock = pygame.time.Clock()         
    run = True                          

    while run:
        
        clock.tick(60) 
        for event in pygame.event.get():    
            
            
            # GAME-OVER 
            if event.type == GAME_OVER : 
                gameOver_sound()
                game_over = True
                
            # QUIT-GAME 
            if event.type == pygame.QUIT: run = False
                
            # EXIT_GAME 
            if event.type == EXIT_GAME: run = False 

            # BULLET-FIRED 
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_SPACE:
                    if (len(bullet_list) < BULLET_MAX):

                        bulletFired_sound()
                        x,y = spaceship.coordinates()
                        z   = spaceship.width()
                        bullet = pygame.Rect(x + z/2 - BULLET_WIDTH/2, y, BULLET_WIDTH, BULLET_HEIGHT)  
                        bullet_list.append(bullet)                         


         
        # GAME-OVER 
        if game_over: 
            background.draw()
            pos = pygame.mouse.get_pos()
            finalWindow_draw(gameOver_text, playAgain_text, yes_text, or_text, no_text, pos, mouse_clicked)
            pygame.display.update()
            continue   
            

        # BACKGROUND
        background.draw()

        # STARS
        add_new_stars(star_list)
        handle_stars_and_bullets(bullet_list, star_list)
        draw_stars(star_list)      

        # BULLETS
        handle_bullets(bullet_list, star_list)
        draw_bullets(bullet_list)
        
        # SPACESHIP
        spaceship.movement()         
        spaceship.draw()             

        # FLAME 
        x,y = spaceship.coordinates()
        height = spaceship.height()
        width  = spaceship.width()
        flame.update_coordinates(x,y, height, width)
        flame.update_img()
        flame.draw()

        
        pygame.display.update()


    
            
            

if __name__ == '__main__':
    main()


    




    
    
    
    
    
    

    



    
    
    

    

    

    
    
