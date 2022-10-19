
from gameSettings import * 



def clickYesOrNo(yes_text, or_text, playAgain_text, mouse_clicked, pos):
    
    yesText_width  = yes_text.get_width()
    yesText_height = yes_text.get_height()
    playAgain_width  = playAgain_text.get_width()
    orText_width = or_text.get_width()
    noText_height = no_text.get_height()

    yes_rect = yes_text.get_rect()
    yes_rect.topleft = (GAME_WIDTH/2 - playAgain_width/2, GAME_HEIGHT/2 - yesText_height/2 + 50 ) 
    no_rect = no_text.get_rect()
    no_rect.topleft = (GAME_WIDTH/2 - playAgain_width/2 + yesText_width + 10 + orText_width + 10, GAME_HEIGHT/2 - noText_height/2 + 50 )

    # new-game/quite 
    if yes_rect.collidepoint(pos) & (pygame.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
        pygame.event.post(pygame.event.Event(NEW_GAME))
    if no_rect.collidepoint(pos) & (pygame.mouse.get_pressed()[0] == 1) & (mouse_clicked == False) :
        pygame.event.post(pygame.event.Event(EXIT_GAME)) 
    
