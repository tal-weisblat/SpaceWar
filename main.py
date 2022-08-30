

# TODO 

# 3 bullets at once (but no more)
# spaceship back-flame (animated)
# more than 1 star at screen 
# reshape spaceship image 
# option for 'new game' at the final-screen 







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


# sounds 
from sounds.functions import blast_sound
from sounds.functions import bullet_fired_sound
from sounds.functions import gameover_sound


SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  





# initilize all objects  
background = Background()
spaceship  = Spaceship(280,490)
star       = Star()
bullet     = Bullet(0,0,0)
gameover   = GameOver()



clock = pg.time.Clock()    
run = True
game_over = False 
star_blasted = False 
bullet_hit_star = False 
collision_time = 0
run_collision_condition = True 
collision_condition = True
game_over_sound = 0     # controll the numebr of times gameover_sound() called 

bullet_fired = False 



while run:

    clock.tick(60) 
    for event in pg.event.get():    
        
        # QUIT GAME 
        if event.type == pg.QUIT:   
            run = False

        # BULLET FIRED 
        
        if (event.type == pg.KEYUP):
            if event.key == pg.K_SPACE:

                if not bullet_fired: 
                
                    bullet_fired      = True 


                    bullet_fired_sound()
                    
                    if t.time() > collision_time + 1: 
                        star_blasted = False
                        
                    bullet_hit_star = False 
                    game_over_sound = 0       # control game-over sound 
                    
                    # initialize bullet 
                    x,y = spaceship.coordinates()
                    bullet.initialize(x,y,spaceship.width())
                    


    

    # COLLISION variables
    x_star, y_star              = star.coordinates()                 # STAR 
    star_width, star_height     = star.dimensions()
    x_bullet, y_bullet          = bullet.coordinates()               # BULLET 
    bullet_width, bullet_height = bullet.dimensions()

    
    # condition : 1 bullet at a time 
    if (y_bullet < 2) or star_blasted:  
        bullet_fired = False 


    # CONDITION (for collision)
    if  (x_star < x_bullet + bullet_width) &\
        (x_bullet + bullet_width < x_star + star_width) &\
        (y_bullet < y_star + star_height)  &\
        (collision_condition): 
        
        blast_sound()  
        collision_condition = False 
        star_blasted        = True
        bullet_hit_star     = True
        collision_time      = t.time()

        # initialize bullet
        x,y = spaceship.coordinates()
        bullet.initialize(x, y, spaceship.width()) 

    
    # FIRST LAYER 
    background.draw()


    # GAME-OVER : add option for new game  
    if (y_star == SCREEN_HEIGHT) and (star_blasted == False): 

        
        # sound 
        if game_over_sound == 0:
            gameover_sound()
            game_over_sound = 1 
        
        gameover.draw()
        pg.display.update()
        continue

        
    spaceship.move_spaceship()    
    spaceship.draw()
    bullet.draw(bullet_hit_star)
    star.draw(star_blasted, collision_time)

    
    # initialize star
    time_condition = t.time() < collision_time + 1
    if (star_blasted == False) & (y_star > SCREEN_HEIGHT): 
        collision_condition = True
        star.initialize()

    elif (star_blasted == True) & (not time_condition):
        collision_condition = True 
        star_blasted        = False
        star.initialize()


    
    pg.display.update()
    

    



    
    
    

    

    

    
    
