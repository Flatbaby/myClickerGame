from cmath import rect
from operator import truediv
import re
import pygame
import os
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800,600



global MONEY

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#image load 
btn = pygame.image.load('button.png').convert_alpha()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

MONEY_FONT = pygame.font.SysFont('comicsans',40)

pygame.display.set_caption("Clicker game")

FPS = 60

#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(HEIGHT/2, WIDTH/2, btn)


def draw_window():
    
    WIN.fill(WHITE)
    start_button.draw()
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit
        draw_window()
main()