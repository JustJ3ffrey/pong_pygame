# Juego 2 (PONG)

# PANTALLA

import random, sys, pygame
import os
os.system("cls")
pygame.init()

pygame.mixer.music.load("E:\PONG_PYGAME\Game.mp3")
# Juego (PONG)
# PANTALLA
size=(1440, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('PONG')
pygame.mixer.music.play(-1)
width, height = 1440, 800
# COLORES
BLANCO = [255, 255, 255]
NEGRO = [0, 0, 0]
font=pygame.font.SysFont("Pixeboy.ttf",40)
pygame.display.set_caption("PONG")

# JUGADORES
velocidad_pelota_x = 7
velocidad_pelota_y = 7
velocidad_j1 = 10
velocidad_j2 = 10
j1_x = 108
j1_y = 400
j2_x = 1332
j2_y = 400
pelota_x = width/2
pelota_y = random.randint(0,750)

pelota = pygame.image.load("pelota.png")
pelota_posicion = pelota.get_rect()
pelota_medidas = pygame.transform.scale(pelota,(5,5))
pelota_posicion.midright = (pelota_x, pelota_y)
ball_radio = pelota_medidas.get_width() / 2
j1=pygame.image.load("Jugadores.png")
j1_rect1 = j1.get_rect()
raqueta_medidas=pygame.transform.scale(j1,(100,220))
j1_rect1.midright = (j1_x, j1_y)
j2=pygame.image.load("Jugadores.png")
j2_rect2 = j2.get_rect()
j2_medidas2=pygame.transform.scale(j2,(100,220))
j2_rect2.midright = (j2_x, j2_y)

# MARCADOR
score_j1 = 0
score_j2 = 0

run = True
while run:
#Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    pygame.time.delay(10)
#Capturamos los eventos que se han producido
for event in pygame.event.get():
#Si el evento es salir de la ventana, terminamos
    if event.type == pygame.QUIT:
        run=False
#Movimiento de los jugadores
keys = pygame.key.get_pressed()
if keys[pygame.K_UP] and j1_rect1.top> velocidad_j1 + 30:
    j1_rect1.top -= velocidad_j1
if keys[pygame.K_DOWN] and j1_rect1.bottom<height - velocidad_j1:
    j1_rect1.bottom += velocidad_j1
if keys[pygame.K_w] and j2_rect2.top>0:
    j2_rect2.top -= velocidad_j2
if keys[pygame.K_s] and j2_rect2.bottom<height:
    j2_rect2.bottom += velocidad_j2
#Colision de la raqueta y la pelota
if j1_rect1.colliderect(pelota_posicion):
    velocidad_pelota_x = -velocidad_pelota_x
if j2_rect2.colliderect(pelota_posicion):
    velocidad_pelota_x=-velocidad_pelota_x
# PONER PUNTUACION CUANDO MARQUEN
#Comprobacion de que la pelota llega a la izquierda
if pelota_posicion.left < 0:
    pelota_posicion.midright = (width/2, random.randint(0,700))
    velocidad_pelota_x = -velocidad_pelota_x
    score_j2 = score_j2 + 1
    velocidad_pelota_x = 20
#Comprobacion de que la pelota llega a la derecha
if pelota_posicion.right > width:
    pelota_posicion.midright = (width/2, random.randint(0,700))
    velocidad_pelota_x = -velocidad_pelota_x
    score_j1 = score_j1 + 1
    velocidad_pelota_x=20
#Movimiento de la pelota
pelota_posicion = pelota_posicion.move(velocidad_pelota_x, velocidad_pelota_y)
if pelota_posicion.left < 0 or pelota_posicion.right > width:
    velocidad_pelota_x = -velocidad_pelota_x
if pelota_posicion.top < 50 or pelota_posicion.bottom > height:
    velocidad_pelota_y = -velocidad_pelota_y
#Pinto el fondo de negro, dibujo la pelota y actualizo la pantalla
screen.fill(NEGRO)
screen.blit(pelota, pelota_posicion)
screen.blit(j1, j1_rect1)
screen.blit(j2, j2_rect2)
#Puntuacion
font = pygame.font.SysFont(None, 100)
score_text = font.render("Score " + str(score_j1), True, BLANCO)
screen.blit(score_text, [10, 10])
pygame.display.flip()
font2 = pygame.font.SysFont(None, 100)
score_text2 = font.render("Score " + str(score_j2), True, BLANCO)
screen.blit(score_text2, [1200, 10])
pygame.display.flip()
# En caso de Ganar el juego se cerrará
if (score_j1 == 5 or score_j2 == 5) == pygame.QUIT:
    run = False
    pygame.quit()
    pygame.mixer.music.stop(-1)
    sys.exit()