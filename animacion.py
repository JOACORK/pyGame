import pygame, sys
from estilos import *
import random

pygame.init()

size = (800,500)
screen = pygame.display.set_mode(size)
clock= pygame.time.Clock()

# GUARDAMOS COORDENADAS DESDE DONDE APARECEN PUNTOS
coor_list=[]
for punto in range(60):
    x = random.randint(0,size[0])
    y = random.randint(0,size[1])
    coor_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(white)
    for coord in coor_list:
        pygame.draw.circle(screen,red,(coord[0],coord[1]),2)
        coord[1] += 1
        #Hacemos que vuelvan a aparecer
        if coord[1] > 500:
            coord[1] = 0
    # CREAR PUNTOS     
    pygame.display.flip()
    clock.tick(60)