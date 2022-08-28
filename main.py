
# general 
import pygame as pg
import time 
 

# classes
from classes.background import Background
from classes.spaceship  import Spaceship
from classes.star       import Star 
from classes.bullet     import Bullet


# sounds 
from sounds.functions import blast_sound
from sounds.functions import bullet_fired_sound


SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  





# initilize all objects  
background = Background()
spaceship  = Spaceship(280,490)
star       = Star()
bullet     = Bullet(0,0,0)



clock = pg.time.Clock()    
run = True
star_blasted = False 
bullet_hit_star = False 
collision_time = 0
run_collision_condition = True 
collision_condition = True


while run:

    clock.tick(60) 
    for event in pg.event.get():    
        
        # QUIT GAME 
        if event.type == pg.QUIT:   
            run = False

        # BULLET FiRED 
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                
                bullet_fired_sound()
                star_blasted = False
                bullet_hit_star = False 
                
                # initialize bullet (according to spaceship)
                x,y = spaceship.coordinates_for_bullet()
                spaceship_width = spaceship.get_spaceship_width()
                bullet = Bullet(x,y,spaceship_width)
                

    background.draw()
    spaceship.move_spaceship()    
    spaceship.draw()


    # COLLISION variables
    x_star, y_star     = star.get_coordinates()                 # STAR 
    star_width, star_height = star.get_dimensions()
    x_bullet, y_bullet = bullet.get_coordinates()               # BULLET 
    bullet_width, bullet_height = bullet.get_dimensions()


    # CONDITION (for collision)
    if  (x_star < x_bullet + bullet_width) and\
        (x_bullet + bullet_width < x_star + star_width) and\
        (y_bullet < y_star + star_height)  and\
        (collision_condition): 
        
        blast_sound()  
        collision_condition  = False 
        star_blasted         = True
        bullet_hit_star = True
        collision_time = time.time()

        # initialize bullet
        x,y = spaceship.coordinates_for_bullet()
        spaceship_width = spaceship.get_spaceship_width()
        bullet.initialize(x,y,spaceship_width) 

    
    
    # DRAW BULLET 
    time_condition = time.time() < collision_time + 1
    if star_blasted == False:  
        star.draw('star') 
        print (1)
        if y_star > SCREEN_HEIGHT:
            collision_condition = True
            star.initialize()
            
    elif (star_blasted == True) and (time_condition):        
        star.draw('blast')
        print (2)

    elif (star_blasted == True) and (not time_condition):
        collision_condition = True 
        star_blasted        = False
        star.initialize()
        print(3) 

    # DRAW BULLET 
    bullet.draw(bullet_hit_star)
     
    



    pg.display.update()
    

    



    
    
    

    

    

    
    
