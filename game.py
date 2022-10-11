

from gameSettings import *

from gameDraw.drawGameOver import drawGameOver
from gameDraw.drawGame import drawGame
from gameObjects.starsAndBullets import drawStars, addStar, handle_stars_and_bullets
from gameObjects.starsAndBullets import drawBullets, handleBullets, addBullets

# change .. (put in class)
#from gameObjects.flame import updateFlame







def clickYesOrNo(yes_text, or_text, playAgain_text, mouse_clicked, pos):
    
    yesText_width  = yes_text.get_width()
    yesText_height = yes_text.get_height()
    playAgain_width  = playAgain_text.get_width()
    orText_width = or_text.get_width()
    noText_height = no_text.get_height()

    yes_rect = yes_text.get_rect()
    yes_rect.topleft = (WIN_WIDTH/2 - playAgain_width/2, WIN_HEIGHT/2 - yesText_height/2 + 50 ) 
    no_rect = no_text.get_rect()
    no_rect.topleft = (WIN_WIDTH/2 - playAgain_width/2 + yesText_width + 10 + orText_width + 10, WIN_HEIGHT/2 - noText_height/2 + 50 )

    # new-game or quite 
    if yes_rect.collidepoint(pos) & (pygame.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
        game()
    if no_rect.collidepoint(pos) & (pygame.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
        pygame.event.post(pygame.event.Event(EXIT_GAME)) 
    
    

    

def game():

    background  = Background(WIN, WIN_WIDTH, WIN_HEIGHT)
    spaceship   = Spaceship(280,490, WIN)
    flame       = Flame(WIN)   
    bulletList = []        
    starList   = []        
    hits_number   = 0
    missed_number = 0    
    game_over     = False 
    mouse_clicked = False 
    run           = True       
    clock         = pygame.time.Clock()         
                    
    while run:
        
        clock.tick(60) 
        for event in pygame.event.get():    
            
            if event.type == STAR_HIT: hits_number += 1
            if event.type == pygame.QUIT: run = False
            if event.type == EXIT_GAME: run = False 

            # missed star 
            if event.type == MISSED_STAR:
                missed_number += 1 

                # game over 
                if missed_number == MAX_STAR_MISED: 
                    GAME_OVER_SOUND.play()
                    game_over = True

            # bullet fired 
            if (event.type == pygame.KEYUP):
                if event.key == pygame.K_SPACE:
                    if (len(bulletList) < MAGAZINE_SIZE):
                        BULLET_FIRED_SOUND.play()
                        addBullets(spaceship, bulletList)          


        pos = pygame.mouse.get_pos()
        hits_number_text   = MISSED_FONT.render('Hits: ' + str(hits_number), 1,  PINK)
        missed_number_text = MISSED_FONT.render('Misses: ' + str(missed_number), 1, PINK)
        
    
        # game-over 
        if game_over: 
            drawGameOver(gameOver_text, 
                         playAgain_text, 
                         hits_number_text, 
                         missed_number_text, 
                         yes_text, or_text, 
                         no_text, background)          
            clickYesOrNo(yes_text, or_text, playAgain_text, mouse_clicked, pos)
            continue   
            
        
        addStar(starList)
        handle_stars_and_bullets(bulletList, starList)
        handleBullets(bulletList)
        spaceship.movement()         
        flame.updateFlame(flame, spaceship)
        drawGame(missed_number_text, hits_number_text, starList, background, drawStars, drawBullets, spaceship, flame, bulletList)
        
if __name__ == '__main__':
    game()


    




    
    
    
    
    
    

    



    
    
    

    

    

    
    
