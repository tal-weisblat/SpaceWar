

import pygame as pg 



def bulletFired_sound():
    
    #time.sleep(0.8)   # delay 
    pg.mixer.init()
    sound = pg.mixer.Sound('sounds/files/test_sound.mp3')  
    sound.play()


def blast_sound():

    pg.mixer.init()
    sound = pg.mixer.Sound('sounds/files/blast.wav')  
    sound.play()


def gameOver_sound():

    pg.mixer.init()
    sound = pg.mixer.Sound('sounds/files/game_over.wav')  
    sound.play()
