import pygame, sys
from estilos import *
import random

pygame.init()

size = (800,500)
screen = pygame.display.set_mode(size)
clock= pygame.time.Clock()

pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    mouse_pos = pygame.mouse.get_pos()
    x_pos = mouse_pos[0]
    y_pos = mouse_pos[1]
    screen.fill(white)
    
    pygame.draw.rect(screen,red,(x_pos,y_pos,100,100))
    
    pygame.display.flip()
    