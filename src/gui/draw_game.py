

from game_settings import * 
from src.gui.draw_game import * 

# ------------------------------------------------- GAME -------------------------------------------------------
def drawGame(missed_number_text, hits_number_text, starList, background, drawStars, drawBullets, spaceship, flame, bulletList):
    
    WIN.fill(WHITE)
    background.draw()
    drawGameTable()
    WIN.blit(missed_number_text, (0,25))
    WIN.blit(hits_number_text, (0,0))    
    drawStars(starList)      
    drawBullets(bulletList)
    spaceship.draw()             
    flame.draw()
    pygame.display.update()


# ------------------------------------------------- GAME-OVER ----------------------------------------------------
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
    WIN.blit( gameOver_text, (GAME_WIDTH/2 - gameOverText_width/2 , GAME_HEIGHT/2 - gameOverText_height))
    WIN.blit(playAgain_text, (GAME_WIDTH/2 - playAgain_width/2, GAME_HEIGHT/2 - playAgain_height/2 + 20))
    WIN.blit( yes_text,      (GAME_WIDTH/2 - playAgain_width/2, GAME_HEIGHT/2 - yesText_height/2 + 50))            
    WIN.blit( or_text, (GAME_WIDTH/2 - playAgain_width/2 + yesText_width + 10 , GAME_HEIGHT/2 - yesText_height/2 + 50 ) )   
    WIN.blit( no_text, (GAME_WIDTH/2 - playAgain_width/2 + yesText_width + 10 + orText_width + 10, GAME_HEIGHT/2 - noText_height/2 + 50))         
    WIN.blit(hits_number_text, (0,0))
    WIN.blit(missed_number_text, (0,25))
    pygame.display.update()
      

# ------------------------------------------------- TABLE ----------------------------------------------------
def drawGameTable():
    
    table = getResults()   # from database 
    table_title = STATISTICS.render('Recent 10 games (time/score):', 1, BLACK)
    table_title_x = GAME_WIDTH + TABLE_GAP
    table_title_y = 15*TABLE_GAP
    underline_x_1 = table_title_x
    underline_x_2 = table_title_x + table_title.get_width()
    underline_y   = table_title_y + table_title.get_height()
    WIN.blit(table_title, (table_title_x, table_title_y))
    pygame.draw.line(WIN, BLACK, (underline_x_1, underline_y), (underline_x_2, underline_y))

    count = table_title_y/TABLE_GAP
    ten_recent_table_results = list(reversed(table))[0:10]
    for line in ten_recent_table_results: 
        table_line = STATISTICS.render( str(line[0]) + ':   ' + str(line[1]) , 1, BLACK)
        WIN.blit(table_line, (GAME_WIDTH + TABLE_GAP, 2*TABLE_GAP + TABLE_GAP*count)) 
        count += 1
