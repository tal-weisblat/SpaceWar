

from gameSettings import * 


def drawGameOver(gameOver_text, playAgain_text, hits_number_text, missed_number_text, yes_text, or_text, no_text, background):
    
    gameOverText_width  = gameOver_text.get_width()
    gameOverText_height = gameOver_text.get_height()  
    playAgain_width  = playAgain_text.get_width()
    playAgain_height = playAgain_text.get_height()
    yesText_width  = yes_text.get_width()
    yesText_height = yes_text.get_height()
    orText_width = or_text.get_width()
    noText_height = no_text.get_height()

    background.draw()
    WIN.blit( gameOver_text, (WIN_WIDTH/2 - gameOverText_width/2 , WIN_HEIGHT/2 - gameOverText_height))
    WIN.blit(playAgain_text, (WIN_WIDTH/2 - playAgain_width/2, WIN_HEIGHT/2 - playAgain_height/2 + 20))
    WIN.blit( yes_text,      (WIN_WIDTH/2 - playAgain_width/2, WIN_HEIGHT/2 - yesText_height/2 + 50))            
    WIN.blit( or_text, (WIN_WIDTH/2 - playAgain_width/2 + yesText_width + 10 , WIN_HEIGHT/2 - yesText_height/2 + 50 ) )   
    WIN.blit( no_text, (WIN_WIDTH/2 - playAgain_width/2 + yesText_width + 10 + orText_width + 10, WIN_HEIGHT/2 - noText_height/2 + 50))         
    WIN.blit(hits_number_text, (0,0))
    WIN.blit(missed_number_text, (0,25))
    pygame.display.update()
      
