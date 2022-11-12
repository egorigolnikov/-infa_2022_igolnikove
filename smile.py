import pygame
from pygame.draw import *
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((200,200,200))
circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (200, 0, 0), (140, 150), 30)
circle(screen, (200, 0, 0), (260, 150), 30)
pygame.draw.line(screen, (0,0,0), [70, 80], [180, 130], 15)
pygame.draw.line(screen, (0,0,0), [220, 130], [340, 80], 15)
circle(screen, (0, 0, 0), (140, 150), 10)
circle(screen, (0, 0, 0), (260, 150), 10)
pygame.draw.line(screen, (0,0,0), [150, 250], [250, 250], 15)
pygame.display.update()
clock = pygame.time.Clock()
finished = False 

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()