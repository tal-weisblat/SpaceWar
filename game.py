

from gameSettings import *

from gameGUI.drawGameOver import drawGameOver
from gameGUI.drawGame import drawGame
from gameGUI.clickYesOrNo import clickYesOrNo

from gameObjects.starsAndBullets import drawStars, addStar, handle_stars_and_bullets
from gameObjects.starsAndBullets import drawBullets, handleBullets, addBullets





def game():

    background  = Background(WIN, WIN_WIDTH, WIN_HEIGHT)
    spaceship   = Spaceship(280,490, WIN)
    flame       = Flame(WIN)   
    bulletList = []        
    starList   = []        
    hits_number   = 0
    missed_number = 0    
    game_over     = False 
    new_game      = False 
    mouse_clicked = False 
    run           = True       
    clock         = pygame.time.Clock()         
                    
    while run:
        
        clock.tick(60) 
        for event in pygame.event.get():    
            
            if event.type == pygame.QUIT: run = False
            if event.type == STAR_HIT: hits_number += 1
            if event.type == EXIT_GAME: run = False 
            if event.type == NEW_GAME:
                new_game = True
                break

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
        
    
        # new-game 
        if new_game:
            game()
            new_game = False 
            break

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


    




    
    
    
    
    
    

    



    
    
    

    

    

    
    
