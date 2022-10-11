

from gameSettings import * 


# --------------------------------------- BULLETS --------------------------------------------
def draw_bullets(bullet_list):
    for bullet in bullet_list:
        pygame.draw.rect(WIN, RED, bullet)


def handle_bullets(bullet_list): 
    for bullet in bullet_list:    
        bullet.y -= BULLET_VEL                         
        if bullet.y < 0: bullet_list.remove(bullet)    



# ---------------------------------------- STARS ---------------------------------------------
def draw_stars(star_list):    
    for starSettings in star_list:
        star  = starSettings[0]
        color = starSettings[1]
        pygame.draw.rect(WIN, color, star)

def add_new_stars(star_list):
    if len(star_list) < LIST_MAX_STARS :
        x = np.random.randint(0, WIN_WIDTH - STAR_WIDTH)      
        star  = pygame.Rect(x, 0, STAR_WIDTH, STAR_HEIGHT)  
        color = random.choice(STAR_COLOR_LIST)              
        velocity = random.choice([1.5, 2, 2.5, 3])          
        star_list.append((star,color,velocity)) 



# ------------------------------------- STARS & BULLETS ---------------------------------------
def handle_stars_and_bullets(bullet_list, star_list): 
    
    for starSettings in star_list:
        star     = starSettings[0]    
        velocity = starSettings[2]    
        star.y += velocity
        
        # star reached bottom
        if star.y > WIN_HEIGHT:             
            pygame.event.post(pygame.event.Event(MISSED_STAR))  
            star_list.remove(starSettings)                      

        # COLLISION : stars & bullets 
        for bullet in bullet_list: 
            if star.colliderect(bullet): 
                BLAST_SOUND.play()
                bullet_list.remove(bullet)                         
                star_list.remove(starSettings)                     
                pygame.event.post(pygame.event.Event(STAR_HIT))    
            
