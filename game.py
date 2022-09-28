

from gameSettings import *



# OBJECTS  
background  = Background()
spaceship   = Spaceship(280,490)
flame       = Flame()    # flame beneath spaceship
bullet_list = []         # list of all bullets 
star_list   = []         # list of all star presented on screen 


# EVENTS 
EXIT_GAME   = pygame.USEREVENT + 1
STAR_HIT    = pygame.USEREVENT + 2  
MISSED_STAR = pygame.USEREVENT + 3 


# RENDER: text, collor  
gameOver_text    = GAME_OVER_FONT.render('Game over',1, YELLOW)      
playAgain_text   = NEW_GAME_FONT.render('Play again ?',1, PINK)
or_text          = YES_AND_NO_FONT.render('or',1,PINK)
yes_text         = YES_AND_NO_FONT.render('Yes',1, PINK)
no_text          = YES_AND_NO_FONT.render('No',1, PINK) 




# DRAW BULLETS 
def draw_bullets(bullet_list):
    for bullet in bullet_list:
        pygame.draw.rect(WIN, RED, bullet)

# HANDLE BULLETS 
def handle_bullets(bullet_list): 
    for bullet in bullet_list:    
        bullet.y -= BULLET_VEL                         # movement on WIN                 
        if bullet.y < 0: bullet_list.remove(bullet)    # reached top WIN


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
    
    for starSettings in star_list:
        star     = starSettings[0]    # star itself 
        velocity = starSettings[2]    # star velocity 
        star.y += velocity
        
        # star reached bottom
        if star.y > WIN_HEIGHT:             
            pygame.event.post(pygame.event.Event(MISSED_STAR))  # posing : for counting missed-stars 
            star_list.remove(starSettings)                      # remove star from list 

        # COLLISION : stars & bullets 
        for bullet in bullet_list: 
            if star.colliderect(bullet): 
                BLAST_SOUND.play()
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
        game()
    if no_rect.collidepoint(pos) & (pygame.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
        pygame.event.post(pygame.event.Event(EXIT_GAME)) 
      

    
def game():

    hits_number   = 0
    missed_number = 0    
    game_over     = False 
    mouse_clicked = False 
    run           = True          
    clock         = pygame.time.Clock()         
    starsSetting_list = []
                    
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
                    GAME_OVER_SOUND.play()
                    game_over = True


            # quit game 
            if event.type == pygame.QUIT: run = False
                
            # exit game 
            if event.type == EXIT_GAME: run = False 

            # bullet fired 
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_SPACE:
                    if (len(bullet_list) < MAGAZINE_SIZE):

                        BULLET_FIRED_SOUND.play()
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

        pygame.display.update()


    
if __name__ == '__main__':
    game()


    




    
    
    
    
    
    

    



    
    
    

    

    

    
    
