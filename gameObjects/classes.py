

import pygame 




# ----------------------------------------- SPACESHIP -------------------------------------------
VEL_SPACESHIP = 5
class Spaceship():
    
    def __init__ (self, x, y, window): 
        self.win = window
        image_spaceship = 'imageFiles/spaceship_1.png'
        scale_spaceship  = 0.06
        self.image = pygame.image.load(image_spaceship).convert_alpha()
        self.image_spaceship = pygame.transform.scale(self.image,(scale_spaceship*int(self.image.get_width()),scale_spaceship*int(self.image.get_height())))  
        self.x = x 
        self.y = y 
        self.rect_spaceship = self.image_spaceship.get_rect()
        self.rect_spaceship.topleft = (self.x,self.y)    

    # DRAW 
    def draw(self):
        self.win.blit(self.image_spaceship, self.rect_spaceship.topleft)   
 
    def coordinates(self): return (self.x, self.y)              # SPACESHIP COORDINATEs for BULLET 
    def width(self): return self.image_spaceship.get_width()    # WIDTH
    def height(self): return self.image_spaceship.get_height()  # HEIGHT 

    # MOVEMENT  
    def movement(self):
        keys = pygame.key.get_pressed()         
        if keys[pygame.K_RIGHT]:   # RIGHT
            self.x = self.x + VEL_SPACESHIP 
            self.rect_spaceship.topleft = (self.x,self.y)
        if keys[pygame.K_LEFT]:    # LEFT 
            self.x = self.x - VEL_SPACESHIP 
            self.rect_spaceship.topleft = (self.x,self.y)
        if keys[pygame.K_DOWN]:    # UP 
            self.y = self.y + VEL_SPACESHIP
            self.rect_spaceship.topleft = (self.x,self.y)   
        if keys[pygame.K_UP]:      # DOWN
            self.y = self.y - VEL_SPACESHIP
            self.rect_spaceship.topleft = (self.x,self.y)   



# ----------------------------------------- FLAME -------------------------------------------
class Flame():

    def __init__(self, window):
        self.win = window
        scale = 0.07
        img = pygame.image.load(f'animationFiles/flame/flame_1.png')
        img = pygame.transform.scale(img, (img.get_width()*scale,(img.get_height()*scale)) )   # scale 
        img = pygame.transform.rotate(img,270)                                                 # rotate 
        self.flame_width  = img.get_width()
        
        # for animation 
        self.index = 1       
        
        # rectangle 
        self.x = 0
        self.y = 0
        self.rect = img.get_rect()
        self.rect.topleft = (self.x,self.y)      

        # ANIMATION :list of all images 
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

    # ANIMATION
    def update_img(self):
        self.image = self.img_list[self.index]
        self.index += 1 
        if (self.index == 10): self.index = 1 
            
    # DRAW         
    def draw(self):
        self.win.blit(self.image, self.rect.topleft)
    



# ----------------------------------------- BACKGROUND -------------------------------------------
class Background():
    
    def __init__ (self, window, win_width, win_height):
        self.win = window
        self.win_width = win_width
        self.win_height = win_height
        image = pygame.image.load('imageFiles/background.jpg')
        self.background_image = pygame.transform.scale(image, (self.win_width, self.win_height))      
        self.y = 0
        
    def draw(self):
        self.y = self.y + 1
        self.win.blit(self.background_image, (0, self.y))
        self.win.blit(self.background_image, (0, self.y -  self.win_height))
        if self.y ==  self.win_height: self.y = 0
             
              


        