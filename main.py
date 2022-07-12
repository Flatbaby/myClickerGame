from cmath import rect
from operator import truediv
import re
import pygame
import os
import button
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800,600


WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#image load 
btn_load = pygame.image.load('button.png').convert_alpha()
btn = pygame.transform.scale(btn_load, (100, 100))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

MONEY_FONT = pygame.font.SysFont('comicsans',40)

pygame.display.set_caption("Clicker game")

FPS = 60



start_button = button.Button(HEIGHT/2, WIDTH/2, btn)


def draw_window():
    
    WIN.fill(WHITE)
    start_button.draw(WIN)
    pygame.display.update()
    
def main():
    clock = pygame.time.Clock()
    run = True
    money = 0
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit
        if start_button.clicked == True:
            money += 1
            print("Money: " + str(money))
        draw_window()
main()