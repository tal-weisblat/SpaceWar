

from gameSettings import * 


def drawGame(missed_number_text, hits_number_text, starList, background, drawStars, drawBullets, spaceship, flame, bulletList):
    background.draw()
    WIN.blit(missed_number_text, (0,25))
    WIN.blit(hits_number_text, (0,0))    
    drawStars(starList)      
    drawBullets(bulletList)
    spaceship.draw()             
    flame.draw()
    pygame.display.update()
