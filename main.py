from cmath import rect
from operator import truediv
import re
import pygame
import os
import button
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1024,800


WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#image load 
btn_load = pygame.image.load('button.png').convert_alpha()
btn = pygame.transform.scale(btn_load, (90, 90))

MONEY = 0
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

MONEY_FONT = pygame.font.SysFont('comicsans',40)

pygame.display.set_caption("Clicker game")

FPS = 60



start_button = button.Button(470, 360,btn)


def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
    

def draw_window():
    
    WIN.fill(WHITE)
    start_button.draw(WIN)

    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    run = True
    
    mong = 1
    coins = 1
    
    
    
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit

            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos >= (380,0):
                    if mopos <= (560,0):
                        coins += mong
                        print(coins)
       
          
        draw_window()
main()