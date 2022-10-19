

from gameSettings import * 



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

drawGameTable()

