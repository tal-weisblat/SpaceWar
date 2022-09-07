


# TODO 
# APPLY NEW bullets list throughout the code 
# ERASE the old bullet approach 



# packages  
import pygame as pygame
import numpy  as np 
import time   as t 
 
# classes
from classes.background import Background
from classes.spaceship  import Spaceship
from classes.star       import Star 
from classes.game_over  import GameOver
from classes.flame      import Flame
 
# sounds 
from sounds.functions import blast_sound
from sounds.functions import bullet_fired_sound


# initilize objects  
background = Background()
spaceship  = Spaceship(280,490)
gameOver   = GameOver()
flame      = Flame()
star       = Star()


# MUSIC (background)
pygame.mixer.init()
pygame.mixer.music.load('sounds/files/melody.mp3')
pygame.mixer.music.play()

# WINDOW
SCREEN_WIDTH  = 500                                                # WINDOW shape  
SCREEN_HEIGHT = 650  
WINDOW = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)
pygame.display.set_caption('SpaceWar')                             # title 


# BULLETs
bullet_list   = []    # the one that's going to contain all bullets
BULLET_VEL    = 15    # bullet velociry 
BULLET_WIDTH  = 5     # bullet width 
BULLET_HEIGHT = 10    # bullet heaight 
BULLET_MAX    = 2     # magazine size (at most 3 bullets on WINDOW)
RED = (255,0,0)       # bullet color 



# STARs
star_list   = []           # contain all stars present on WINDOW 
STAR_VEL    = 3            # CHNAGE : to something random 
STAR_WIDTH  = 40           # star dimensions 
STAR_HEIGHT = 50   
STAR_MAX    = 2            # at most 3 stars on WINDOW 
YELLOW      = (255,255,0)  # stars color 







# EVENTS 
STAR_HIT  = pygame.USEREVENT + 1 
STAR_INIT = pygame.USEREVENT + 2  






# DRAW BULLETS 
def draw_bullets(bullet_list):
    for bullet in bullet_list:
        pygame.draw.rect(WINDOW, RED, bullet)


# HANDLE BULLETS 
def handle_bullets(bullet_list, star_list): 
    
    for bullet in bullet_list: 
        # movement on WINDOW   
        bullet.y -= BULLET_VEL                  
        # reached top WINDOW
        if bullet.y < 0: bullet_list.remove(bullet)    


# DRAW STARS          
def draw_stars(star_list):    
    
    for star in star_list:
        pygame.draw.rect(WINDOW, YELLOW, star)


# ADD NEW STARs
def add_new_stars(star_list):
    
    if len(star_list) < STAR_MAX :
        x = np.random.randint(0, SCREEN_WIDTH - STAR_WIDTH) 
        star = pygame.Rect(x, 0, STAR_WIDTH, STAR_HEIGHT)       
        star_list.append(star) 


# COLLISION 
def handle_stars_and_bullets(bullet_list, star_list): 
    
    for star in star_list:

        star.y += STAR_VEL

        # star reached buttom 
        if star.y > SCREEN_HEIGHT: star_list.remove(star)
            
        # star & bullet collided 
        for bullet in bullet_list: 
            if star.colliderect(bullet): 
                
                blast_sound()
                pygame.event.post(pygame.event.Event(STAR_HIT))         # posting event 
                bullet_list.remove(bullet)                              # remove bullet (from list) 
                star_list.remove(star)                                  # remove star   (from list)
            


            

        

        


def main():

    mouse_clicked = False 
    #star.initialize()
    stage = 'non'    
    collision_time = t.time() - 1 
    clock = pygame.time.Clock()         # conroll number of looping per second
    run = True                          

    while run:
        
        clock.tick(60) 
        for event in pygame.event.get():    
            
            # STAR-HIT 
            if event.type == STAR_HIT: print ('star HIT')
            
            # QUIT-GAME 
            if event.type == pygame.QUIT: run = False
                

            # BULLET-FIRED 
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_SPACE:
                    if (len(bullet_list) < BULLET_MAX):

                        bullet_fired_sound()
                        x,y = spaceship.coordinates()
                        z   = spaceship.width()
                        bullet = pygame.Rect(x + z/2 - BULLET_WIDTH/2, y, BULLET_WIDTH, BULLET_HEIGHT)  
                        bullet_list.append(bullet)                               # add bullet to list 


        # FIRST LAYER 
        background.draw()

        # STARS
        add_new_stars(star_list)
        handle_stars_and_bullets(bullet_list, star_list)
        draw_stars(star_list)      

        # BULLETS
        handle_bullets(bullet_list, star_list)
        draw_bullets(bullet_list)
        

        # SPACESHIP
        spaceship.movement()               # moving spaceship on WINDOW 
        spaceship.draw()                   # draw spaceship

        # FLAME 
        x,y = spaceship.coordinates()
        height = spaceship.height()
        width  = spaceship.width()
        flame.update_coordinates(x,y, height, width)
        flame.update_img()
        flame.draw()


        
        pygame.display.update()




        # star_y_coordinate = star.y_coordinate()
        # if (t.time() > collision_time + 0.7) and stage == '1': 
        #     stage = '2'
        #     star.status = 'not blasted'
        
        # elif (t.time() > collision_time + 0.7) and stage == '2':
        #     stage = 'non'
        #     star.initialize()

        # elif (star_y_coordinate > SCREEN_HEIGHT) and (star.status == 'not blasted'):
            
        #     pos = pygame.mouse.get_pos()                        # mouse position 
        #     if gameOver.new_game(pos,mouse_clicked)  : main()   # NEW-GAME 
        #     if gameOver.exit_game(pos,mouse_clicked) : break    # EXIT-GAME 
        #     if (pygame.mouse.get_pressed()[0] == 0): mouse_clicked = False
        #     gameOver.draw()    
            


        
            

            
            
            

if __name__ == '__main__':
    main()


    




    
    
    
    
    
    

    



    
    
    

    

    

    
    
