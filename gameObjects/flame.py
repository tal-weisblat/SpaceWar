

from gameSettings import *



# ----------------------------------------- FLAME -------------------------------------------
class Flame():

    def __init__(self, window):
        self.win = window
        scale = 0.07
        img = pygame.image.load(f'animationFiles/flame/flame_1.png')
        img = pygame.transform.scale(img, (img.get_width()*scale,(img.get_height()*scale)) )   # scale 
        img = pygame.transform.rotate(img,270)                                                 # rotate 
        self.flame_width  = img.get_width()
        
        self.index = 1       # for animation 
    
        self.x = 0
        self.y = 0
        self.rect = img.get_rect()
        self.rect.topleft = (self.x,self.y)      

        # animation 
        self.img_list = []      
        for i in range(1,11):
            img = pygame.image.load(f'animationFiles/flame/flame_{i}.png')
            img = pygame.transform.rotate(img,270)
            img = pygame.transform.scale(img, (img.get_width()*scale,(img.get_height()*scale)) )
            self.img_list.append(img)

    # position below spaceship
    def update_coordinates(self, x, y, spaceship_heigth, spaceship_width):
        self.x = x - (self.flame_width - spaceship_width)/2 
        self.y = y + spaceship_heigth + 1
        self.rect.topleft = (self.x,self.y)

    def update_img(self):  # animation 
        self.image = self.img_list[self.index]
        self.index += 1 
        if (self.index == 10): self.index = 1 
                    
    def draw(self):
        self.win.blit(self.image, self.rect.topleft)
