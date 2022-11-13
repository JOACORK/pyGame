import pygame, sys
from style import *

pygame.init()

screen_size = (800,500)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
print(pygame.display.get_surface().get_size())
game_over = False

# ----- Definir constantes
player_width= 15
player_hight= 90
distance_x_players = 50




# Posición X
player1_x_coord = distance_x_players
player2_x_coord = screen_size[0] - distance_x_players

# Posición Y
player1_y_coord = screen_size[1]/2-(player_hight/2)
player2_y_coord = screen_size[1]/2-(player_hight/2)

# Velocidad Players
player1_speed = 0
player2_speed = 0

# Coordenadas pelota
ball_x = screen_size[0]/2
ball_y = screen_size[1]/2
# Velocidad pelota
ball_speed_x = 3
ball_speed_y = 3


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               game_over=True

        
        # Animaciones
        if event.type == pygame.KEYDOWN:
            print(event)
            # jugador 1
            if event.key == pygame.K_w:
                player1_speed = -3
            if event.key == pygame.K_s:
                player1_speed = +3
                
            # jugador 2
            if event.key == pygame.K_UP:
                player2_speed = -3
            if event.key == pygame.K_DOWN:
                player2_speed = +3  
                print(player2_speed)      
        
        if event.type == pygame.KEYUP:
             # jugador 1
            if event.key == pygame.K_w:
                player1_speed = 0
            if event.key == pygame.K_s:
                player1_speed = 0
            # jugador 2
            if event.key == pygame.K_UP:
                player2_speed = 0
            if event.key == pygame.K_DOWN:
                player2_speed = 0         
     
    # --------------- LOGICA ---------------
    # Rebote pelota
    if ball_y > 493 or ball_y < 7:
        ball_speed_y *= -1
    
    #Revisa si la pelota sale por lado derecho
    if ball_x > 800:
        ball_x= screen_size[0]/2
        ball_y= screen_size[1]/2  
        ball_speed_x= 3
        ball_speed_y = 3
        ball_speed_x *= -1
        ball_speed_y *= -1
        
    if ball_x < 0:
        ball_x= screen_size[0]/2
        ball_y= screen_size[1]/2  
        ball_speed_x= 3
        ball_speed_y = 3
        ball_speed_x *= -1
        ball_speed_y *= -1
    

    
    #  Modificar coordenadas, movimiento objetos
    # Jugadores
    player1_y_coord += player1_speed
    player2_y_coord += player2_speed
    
    # Limites jugadores
    if player1_y_coord >screen_size[1]-player_hight or player1_y_coord < 0:
        player1_speed = 0
    if player2_y_coord >screen_size[1]-player_hight or player1_y_coord < 0:
        player2_speed = 0
        
    # Pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # --------------- FIN LOGICA ---------------
    
    
    screen.fill(black)
    # ------------- DIUJO
    # Rectangulo
    player1 = pygame.draw.rect(screen,white,(player1_x_coord,player1_y_coord, player_width, player_hight))
    player2 = pygame.draw.rect(screen,white,(player2_x_coord,player2_y_coord, player_width, player_hight))

    ball = pygame.draw.circle(screen, red,(ball_x,ball_y),7)
    # ------------- DIUJO
    
    # Colisión
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1    
        
        
        
    
    pygame.display.flip()    
    # Seteamos fps
    clock.tick(60)


pygame.quit()