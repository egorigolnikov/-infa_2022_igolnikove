import pygame
from pygame.draw import *
from random import randint
pygame.init()
FPS = 0.5
screen = pygame.display.set_mode((1200, 900)) 
# создаём массив цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global b, k
b, k, z = (0, 0, 0)


def new_ball():
    # рисуем круг
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def tap():
    # проверяем, попали ли в круг
    global z
    if((((x-x1)**2 + (y-y1)**2)**0.5) < r):
        z = 1


def score():
    # выводим счёт
    g = pygame.font.SysFont("comicsansms", 35)
    value = g.render("Ваш счёт: " + str(k), True, GREEN)
    screen.blit(value, [100, 110])


pygame.display.update()
clock = pygame.time.Clock()
finished = False
        
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1 = event.pos[0]  
            y1 = event.pos[1]
            tap()

    k = k + z
    z = 0
    score()
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
