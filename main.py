

# TODO 



# CREATE functionality for NEW-GAME option  
# 3 bullets at once (but no more)
# more than 1 star at screen (different paces ? zigzaging ?)
# reshape spaceship image 
# how to reduce/increase the sounds of shooting etc. ? 
# bug : once star is blasted it's possible to fire at will 
# various BUGs along the code (look for them)

# imporive falling-star ANIMATION (add better stream of pictures)







# general 
from telnetlib import GA
import pygame as pg
import time as t 
 

# classes
from classes.background import Background
from classes.spaceship  import Spaceship
from classes.star       import Star 
from classes.bullet     import Bullet
from classes.game_over  import GameOver
from classes.flame      import Flame


# sounds 
from sounds.functions import blast_sound
from sounds.functions import bullet_fired_sound
from sounds.functions import gameOver_sound


SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  





# initilize all objects  
background = Background()
spaceship  = Spaceship(280,490)
gameOver   = GameOver()
flame      = Flame()
star       = Star()

bullet     = Bullet(0,0,0)




clock = pg.time.Clock() 

run = True                             # 
is_star_blasted = False                # true or false  
bullet_hit_star = False                # used for eliminating bullet from screen once collision took place  
bullet_star_collision_time = 0         # the exact bullet-star-collision-time 
bullet_did_not_hit_star = True         # bullet & star status before hitting (one another)
game_over_sound = 0                    # controll the numebr of times gameover_sound() called 
bullet_fired = False                   # True only when bullet fired and on the screen 
mouse_clicked = False                  # for YES & NO buttons 


# background music 
pg.mixer.init()
pg.mixer.music.load('sounds/files/melody.mp3')
pg.mixer.music.play()


while run:
    
    clock.tick(60) 
    for event in pg.event.get():    
        
        # QUIT GAME 
        if event.type == pg.QUIT: run = False

        # BULLET FIRED 
        if (event.type == pg.KEYUP):
            if event.key == pg.K_SPACE:

                if not bullet_fired: 
                
                    bullet_fired  = True
                    bullet_fired_sound()
                    
                    if t.time() > bullet_star_collision_time + 1: 
                        is_star_blasted = False
                        
                    bullet_hit_star = False 
                    game_over_sound = 0          # control game-over sound 
                    
                    # initialize bullet 
                    x,y = spaceship.coordinates()
                    bullet.initialize(x,y,spaceship.width())
                    


    # COLLISION variables
    x_star, y_star              = star.coordinates()                 # STAR 
    star_width, star_height     = star.dimensions()
    x_bullet, y_bullet          = bullet.coordinates()               # BULLET 
    bullet_width, bullet_height = bullet.dimensions()

    
    # condition : 1 bullet at a time 
    if (y_bullet < 2) or is_star_blasted:  
        bullet_fired = False 


    # shorter collision version 
    if star.rect_star.colliderect(bullet.rect_bullet) and bullet_did_not_hit_star:
        print ('HIT')
        blast_sound()  
        bullet_did_not_hit_star    = False 
        is_star_blasted            = True
        bullet_hit_star            = True
        bullet_star_collision_time = t.time()

        # initialize bullet
        x,y = spaceship.coordinates()
        bullet.initialize(x, y, spaceship.width()) 


    # CONDITION (for collision)
    # if  (x_star < x_bullet + bullet_width) &\
    #     (x_bullet + bullet_width < x_star + star_width) &\
    #     (y_bullet < y_star + star_height)  &\
    #     (bullet_did_not_hit_star): 
        
    #     blast_sound()  
    #     bullet_did_not_hit_star    = False 
    #     is_star_blasted            = True
    #     bullet_hit_star            = True
    #     bullet_star_collision_time = t.time()

    #     # initialize bullet
    #     x,y = spaceship.coordinates()
    #     bullet.initialize(x, y, spaceship.width()) 

    time_condition = t.time() < bullet_star_collision_time + 1
    

# -------- move this block to the buttom ------------

    # FIRST LAYER 
    background.draw()
    
    # FLAME 
    x,y = spaceship.coordinates()
    height = spaceship.height()
    width  = spaceship.width()
    flame.update_coordinates(x,y, height, width)
    flame.update_img()
    flame.draw()
    
# -------- move this block to the buttom ------------




    # GAME-OVER 
    if (y_star > SCREEN_HEIGHT) and (is_star_blasted == False) and (run == True): 

        if game_over_sound == 0:                                       # sound (played once)
            gameOver_sound()
            game_over_sound = 1 
        
        gameOver.draw()                                                # draw   
        pos = pg.mouse.get_pos()                                       # cursor position 
        run = gameOver.exit_game(pos,mouse_clicked)                    # EXIT GAME  
        mouse_clicked = gameOver.new_game(pos,mouse_clicked)           # BUG: no functionality ... 

        # TURN-OFF 
        flame.turn_off()                                               
        spaceship.turn_off()
        star.turn_off()          # BUG: doesnt function ... 
        

        
        
        if (pg.mouse.get_pressed()[0] == 0): mouse_clicked = False     # 
        pg.display.update()
        

    # initialize star
    elif (is_star_blasted == False) & (y_star > SCREEN_HEIGHT): 
        bullet_did_not_hit_star = True
        star.initialize()

    elif (is_star_blasted == True) & (not time_condition):
        bullet_did_not_hit_star = True 
        is_star_blasted        = False
        star.initialize()


    

    #spaceship.movement()               # moving spaceship on screen 
    spaceship.draw()                   # draw spaceship
    bullet.draw(bullet_hit_star)       # draw bullet 
    bullet.update_move()               # movement on screen
    star.update_image()                # for animation 
    star.draw(is_star_blasted, bullet_star_collision_time)  

    
    pg.display.update()
    

    



    
    
    

    

    

    
    
