


# TODO 
# add : different shapes for stars (rectangles, circles, elipses etc.)

 
# use pymunk library for physics simulations ? 
# - you can add more features to your game
# - you can add 'dynamic stars' change their position on screen while bumping up with other static-objects 
# - 





# packages  
from os import sysconf
import pygame as pygame
import numpy  as np 
import random



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


<<<<<<< HEAD
# initilize all objects  
background = Background()
spaceship  = Spaceship(280,490)
gameOver   = GameOver()
flame      = Flame()
star       = Star()

=======
# COLORs
RED     = (255,0,0)      # bullet
YELLOW  = (255,255,0)    # gameover title 
PINK    = (255,192,203)  # yes & no
WHITE = (255,255,255)
COLOR_1 = (128,255,0)
COLOR_2 = (204,102,0)
COLOR_3 = (255,0,127)
STAR_COLOR_LIST = [PINK,YELLOW,COLOR_1,COLOR_2,COLOR_3]


>>>>>>> changeBullets


# BULLETs
bullet_list   = []    # the one that's going to contain all bullets
BULLET_VEL    = 16    # bullet velociry 
BULLET_WIDTH  = 4     # bullet width 
BULLET_HEIGHT = 9    # bullet heaight 
BULLET_MAX    = 2     # magazine size (at most 3 bullets on WIN)


# STARs
star_list   = []           # contain all stars present on WIN 
STAR_VEL    = 2            # CHNAGE : to something random 
STAR_WIDTH  = 30           # star dimensions 
STAR_HEIGHT = 30   
LIST_MAX_STARS = 4            # at most 3 stars on WIN 
MAX_STAR_MISED = 5

<<<<<<< HEAD
run = True                             # 
is_star_blasted = False                # true or false  
bullet_hit_star = False                # used for eliminating bullet from screen once collision took place  
bullet_star_collision_time = 0         # the exact bullet-star-collision-time 
bullet_did_not_hit_star_before = True         # bullet & star status before hitting (one another)
game_over_sound = 0                    # controll the numebr of times gameover_sound() called 
bullet_fired = False                   # True only when bullet fired and on the screen 
mouse_clicked = False                  # for YES & NO buttons 






# background music 
pg.mixer.init()
pg.mixer.music.load('sounds/files/melody.mp3')
pg.mixer.music.play()
=======


# EVENTS 
GAME_OVER = pygame.USEREVENT + 1
EXIT_GAME = pygame.USEREVENT + 2 
STAR_HIT  = pygame.USEREVENT + 3  
MISSED_STAR = pygame.USEREVENT + 4 
>>>>>>> changeBullets

# FONT 
GAME_OVER_FONT   = pygame.font.SysFont('comicsans', 40)             
NEW_GAME_FONT    = pygame.font.SysFont('comicsans', 25)
YES_AND_NO_FONT  = pygame.font.SysFont('comicsans', 25) 
MISSED_FONT = pygame.font.SysFont('comicsans', 20)

<<<<<<< HEAD



SCREEN_WIDTH  = 500       # screen shape  
SCREEN_HEIGHT = 650  
pg.display.set_caption('SpaceWar')                            # title 
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))     # game window (width & height)
=======
# RENDER: text, collor  
gameOver_text    = GAME_OVER_FONT.render('Game over',1, YELLOW)      
playAgain_text   = NEW_GAME_FONT.render('Play again ?',1, PINK)
or_text          = YES_AND_NO_FONT.render('or',1,PINK)
yes_text         = YES_AND_NO_FONT.render('Yes',1, PINK)
no_text          = YES_AND_NO_FONT.render('No',1, PINK) 



>>>>>>> changeBullets





<<<<<<< HEAD
# TEST : changing bullet settings 
MAX_BULLETS = 3                      # maximal number of bullets on screen 
bullets     = []                     # bullet magazine 
RED = (255,0,0)                      # the color of future to be bullet 
bullet_test = pg.Rect(100,100,5,10)  # 
=======
>>>>>>> changeBullets




<<<<<<< HEAD
while run:
=======


# DRAW BULLETS 
def draw_bullets(bullet_list):
    for bullet in bullet_list:
        pygame.draw.rect(WIN, RED, bullet)


# HANDLE BULLETS 
def handle_bullets(bullet_list): 
>>>>>>> changeBullets
    
    for bullet in bullet_list: 
        # movement on WIN   
        bullet.y -= BULLET_VEL                  
        # reached top WIN
        if bullet.y < 0: bullet_list.remove(bullet)    

<<<<<<< HEAD
        # BULLET FIRED 
        if (event.type == pg.KEYUP):
            if event.key == pg.K_SPACE and not bullet_fired :
                
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
    if star.rect.colliderect(bullet.rect) and bullet_did_not_hit_star_before:
    
        blast_sound()  
        bullet_did_not_hit_star_before  = False 
        is_star_blasted                 = True
        bullet_hit_star                 = True
        bullet_star_collision_time      = t.time()

        # initialize bullet
        x,y = spaceship.coordinates()
        bullet.initialize(x, y, spaceship.width()) 


    
    time_condition = t.time() < bullet_star_collision_time + 1
=======

# DRAW STARS          
def draw_stars(star_list):    
    
    for starSettings in star_list:
        star  = starSettings[0]
        color = starSettings[1]
        pygame.draw.rect(WIN, color, star)


# ADD NEW STARs
def add_new_stars(star_list):
    if len(star_list) < LIST_MAX_STARS :
         
        x = np.random.randint(0, WIN_WIDTH - STAR_WIDTH)      
        star  = pygame.Rect(x, 0, STAR_WIDTH, STAR_HEIGHT)   # shape $ position    : add more shapes ?
        color = random.choice(STAR_COLOR_LIST)               # color 
        velocity = random.choice([1.5, 2, 2.5, 3])           # velocity : uniquely determined for each star 
        star_list.append((star,color,velocity)) 


# COLLISION 
def handle_stars_and_bullets(bullet_list, star_list): 
>>>>>>> changeBullets
    
    for starSettings in star_list:
        
        star     = starSettings[0]    # star itself 
        velocity = starSettings[2]    # star velocity 
        star.y += velocity

        # FIX : 
        if star.y > WIN_HEIGHT:             
            
            pygame.event.post(pygame.event.Event(MISSED_STAR))   # posing : for counting missed-stars 
            star_list.remove(starSettings)                     # remove star from list 

<<<<<<< HEAD
    # FIRST LAYER 
    background.draw()
    #pg.draw.rect(screen, RED, bullet_test)
=======


            

        # COLLISION : stars & bullets 
        for bullet in bullet_list: 
            if star.colliderect(bullet): 
                
                blast_sound()
                bullet_list.remove(bullet)                         # remove star  
                star_list.remove(starSettings)                     # remove bullet       
                pygame.event.post(pygame.event.Event(STAR_HIT))    # posing : for star-hits counting purposes 
            


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
>>>>>>> changeBullets
    
    






<<<<<<< HEAD
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
        star.turn_off()                                                # BUG: doesnt function ... 
        
        if (pg.mouse.get_pressed()[0] == 0): mouse_clicked = False     
        pg.display.update()
=======


def main():

    
    hits_number   = 0
    missed_number = 0    
    

    starsSetting_list   = []
    game_over = False 
    mouse_clicked = False 
    clock = pygame.time.Clock()         
    run = True                          

    while run:
        
        clock.tick(60) 
        for event in pygame.event.get():    
            
            # hit star 
            if event.type == STAR_HIT:
                hits_number += 1
                hits_number_text = MISSED_FONT.render('Hits : ' + str(hits_number), 1, PINK)

            # missed star 
            if event.type == MISSED_STAR:
                missed_number += 1 
                missed_number_text = MISSED_FONT.render('Missed: ' + str(missed_number), 1, PINK)

                # game over 
                if missed_number == MAX_STAR_MISED: 
                    gameOver_sound()
                    game_over = True


            # quit game 
            if event.type == pygame.QUIT: run = False
                
            # exit game 
            if event.type == EXIT_GAME: run = False 

            # bullet fired 
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
            WIN.blit(hits_number_text, (0,0))
            WIN.blit(missed_number_text, (0,25))
            pygame.display.update()
            continue   
            

        # BACKGROUND
        background.draw()

        # HITS-NUMBER  
        hits_number_text = MISSED_FONT.render('Hits: ' + str(hits_number), 1,  PINK)
        WIN.blit(hits_number_text, (0,0))    

        # MISSED-NUMBER
        missed_number_text = MISSED_FONT.render('Misses: ' + str(missed_number), 1, PINK)
        WIN.blit(missed_number_text, (0,25))

        # STARS
        add_new_stars(starsSetting_list)
        handle_stars_and_bullets(bullet_list, starsSetting_list)
        draw_stars(starsSetting_list)      

        # BULLETS
        handle_bullets(bullet_list)
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

>>>>>>> changeBullets
        
        pygame.display.update()

<<<<<<< HEAD
    # initialize star
    elif (is_star_blasted == False) & (y_star > SCREEN_HEIGHT): 
        bullet_did_not_hit_star_before = True
        star.initialize()

    elif (is_star_blasted == True) & (not time_condition):
        bullet_did_not_hit_star_before = True 
        is_star_blasted        = False
        star.initialize()
=======

    
            
            

if __name__ == '__main__':
    main()
>>>>>>> changeBullets


    


<<<<<<< HEAD
    pg.display.update()
=======


    
    
    
    
    
>>>>>>> changeBullets
    

    



    
    
    

    

    

    
    
