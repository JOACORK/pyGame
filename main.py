from time import sleep
import pygame , sys
import estilos as est



size = (800,500)
print(size[0]-1)
# Crear ventana
screen = pygame.display.set_mode(size)

# Controlar fps
clock = pygame.time.Clock()

#coodenadas
cord_x = 400
cord_y = 200
#Velocidad a la que se mueve animación
speed_x = 3
speed_y = 3

while True:
    pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # --------------- LOGICA ---------------
    # Invertimos velocidad al llegar a los límites de la ventana        
    if (cord_x > size[0]-75 or cord_x < 0):
        speed_x *= -1
    if (cord_y > size[1]-75 or cord_y < 0):
        speed_y *= -1
        
    # animación objeto    
    cord_x += speed_x
    cord_y += speed_y
    
    # --------------- FIN LOGICA ---------------
    # Color de fondo
    screen.fill(est.white)
    # --------------- ZONA DE DIBUJO ---------------
    for x in range(100,700,100):
        pygame.draw.rect(screen,est.green,(x,230,50,50))
        pygame.draw.rect(screen,est.black,(x,230,50,50))
        
    # Animación
    pygame.draw.rect(screen,est.red,(cord_x,cord_y,80,80))
    
        
    #  --------------- FIN ZONA DE DIBUJO ---------------
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(80)