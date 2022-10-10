

from gameSettings import * 



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
             
              


        