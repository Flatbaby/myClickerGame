import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
        
    def draw(self, surface):
 
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        
    

    

            