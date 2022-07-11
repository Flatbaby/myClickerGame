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

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

MONEY_FONT = pygame.font.SysFont('comicsans',40)

pygame.display.set_caption("Clicker game")

FPS = 60

def draw_window():
    
    rect_dimensions = 50
    
    
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, YELLOW, (400,300,rect_dimensions,rect_dimensions))
    pygame.display.update()
    
#button class
class Button():
    def __init__(self, x, y, image):


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