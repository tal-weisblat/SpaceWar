

import pygame as pg 



def bullet_fired_sound():
    
    #time.sleep(0.8)   # delay 
    #pg.init()
    pg.mixer.init()
    sound = pg.mixer.Sound('sounds/files/test_sound.mp3')  
    sound.play()


def blast_sound():

    #pg.init()
    pg.mixer.init()
    sound = pg.mixer.Sound('sounds/files/blast.wav')  
    sound.play()
