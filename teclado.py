import pygame, sys
from estilos import *

pygame.init()

size = (800,500)
screen = pygame.display.set_mode(size)
clock= pygame.time.Clock()

pygame.mouse.set_visible(0)

# DEFINIR COORDENADAS CUADRADO
coord_x = 10
coord_y = 10

# VELOCIDAD
x_speed= 0
y_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # EVENTOS TECLADO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed = 0

    screen.fill(white)
    
    coord_x += x_speed
    
    pygame.draw.rect(screen,red,(coord_x,coord_y,100,100))
    
    pygame.display.flip()
    clock.tick(60)
    