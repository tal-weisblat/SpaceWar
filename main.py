
# general 
import pygame as pg
import time 
 

# classes
from classes.background import Background
from classes.spaceship  import Spaceship
from classes.star       import Star 
from classes.bullet     import Bullet
from classes.blast      import Blast

# sounds 
from sounds.functions import blast_sound
from sounds.functions import bullet_fired_sound








# initilize all objects  
background = Background()
spaceship  = Spaceship(280,490)
star       = Star()
bullet     = Bullet(0,0,0)



clock = pg.time.Clock()    
run = True
bullet_collided_star_draw_star = False 
bullet_collided_star_draw_bullet = False 
collision_time = 0
run_collision_condition = True 



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
                bullet_collided_star_draw_star = False
                bullet_collided_star_draw_bullet = False 
                
                # initialize bullet (according to spaceship)
                x,y = spaceship.coordinates_for_bullet()
                spaceship_width = spaceship.get_spaceship_width()
                bullet = Bullet(x,y,spaceship_width)
                


    background.draw()


    # COLLISION variables
    x_star, y_star     = star.get_coordinates()                 # STAR 
    star_width, star_height = star.get_dimensions()
    x_bullet, y_bullet = bullet.get_coordinates()               # BULLET 
    bullet_width, bullet_height = bullet.get_dimensions()


    # initialie (for condition)
    if y_star == 0: 
        collision_condition = True 

    # CONDITION (for collision)
    if  (x_star < x_bullet + bullet_width) and\
        (x_bullet + bullet_width < x_star + star_width) and\
        (y_bullet < y_star + star_height)  and\
        (collision_condition): 
        
        blast_sound()  
        collision_condition  = False 
        bullet_collided_star_draw_star = True
        bullet_collided_star_draw_bullet = True
        collision_time = time.time()

        # initialize bullet
        x,y = spaceship.coordinates_for_bullet()
        spaceship_width = spaceship.get_spaceship_width()
        bullet = Bullet(x,y,spaceship_width) 

    
    spaceship.move_spaceship()    
    spaceship.draw()


     
    bullet_collided_star_draw_star = star.draw(bullet_collided_star_draw_star, collision_time)
    
    bullet.draw(bullet_collided_star_draw_bullet)




    pg.display.update()
    

    



    
    
    

    # when it happens (both image and sound take place)   ....

    # STEP : find the blast condition in terms of the above star & bullet coordinates 
    # STEP : use CONDITION stimulate blast-scene (both visual and sound)
    # REMARK : the visual-blast should take place at the exact collision's coordinates 

    

    

    
    
