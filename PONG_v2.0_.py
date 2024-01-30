import sys,pygame,random
from time import time
from pygame.locals import *
# Inicialización
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("C:\Users\aleja\Documents\Trabajos\PONG_PYGAME-20240130T142426Z-001\PONG_PYGAME\Menu.mp3")
#MENU DE INICIO DEL JUEGO
# Obtiene las dimensiones de la pantalla del usuario
ancho = 1440
alto = 800
size = (ancho, alto)
# Crea la ventana del juego en modo pantalla completa
screen = pygame.display.set_mode(size)
pygame.mixer.music.play(-1)

# Definir colores
BLANCO = (255, 255, 255)

# Cargar imagen de fondo
fondo = pygame.image.load('Fondo_Menu.png').convert()

# Definir fuente y tamaño de texto
fuente = pygame.font.Font(None, 50)

# Definir botones
boton_jugar = {
    'texto': fuente.render('PLAY', True, BLANCO),
    'rect': pygame.Rect(ancho / 2 - 100, alto / 2 - 50, 200, 50),
    'color': (255, 255, 255),
    'color_seleccionado': (128, 128, 128),
    'seleccionado': True
}
boton_salir = {
    'texto': fuente.render('EXIT', True, BLANCO),
    'rect': pygame.Rect(ancho / 2 - 100, alto / 2 + 50, 200, 50),
    'color': (255, 255, 255),
    'color_seleccionado': (128, 128, 128),
    'seleccionado': True
}

run = True
# Bucle principal del juego
while run:
    # Manejar eventos del usuario
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            pygame.mixer.music.stop(-1)
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                boton_jugar['seleccionado'] = True
                boton_salir['seleccionado'] = False
            elif evento.key == pygame.K_UP:
                boton_jugar['seleccionado'] = False
                boton_salir['seleccionado'] = True
            elif evento.key == pygame.K_RETURN:
                if boton_salir['seleccionado']:
                    ####################     COMIENZA EL JUEGO AQUI:     ######################
                    pygame.mixer.music.load("C:\Users\aleja\Documents\Trabajos\PONG_PYGAME-20240130T142426Z-001\PONG_PYGAME\Game.mp3")
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

                    # JUGADORES
                    velocidad_pelota_x = 10
                    velocidad_pelota_y = 10
                    velocidad_j1 = 10
                    velocidad_j2 = 10
                    j1_x = 108
                    j1_y = 400
                    j2_x = 1332
                    j2_y = 400
                    pelota_x = width/2
                    pelota_y = random.randint(100, 1340)

                    # Inicialización de las imagenes usadas
                    pelota = pygame.image.load("pelota.png")
                    pelota_posicion = pelota.get_rect()
                    pelota_medidas = pygame.transform.scale(pelota,(5,5))
                    pelota_posicion.midright = (pelota_x, pelota_y)
                    radio_pelota = pelota_medidas.get_width() / 2
                    j1=pygame.image.load("Jugadores.png")
                    j1_rect1 = j1.get_rect()
                    j1_medidas=pygame.transform.scale(j1,(100,220))
                    j1_rect1.midright = (j1_x, j1_y)
                    j2=pygame.image.load("Jugadores.png")
                    j2_rect2 = j2.get_rect()
                    j2_medidas2=pygame.transform.scale(j2,(100,220))
                    j2_rect2.midright = (j2_x, j2_y)

                    # MARCADOR
                    score_j1 = 0
                    score_j2 = 0

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
                        # CASO DE PUNTUACIÓN
                        #Comprobacion de que la pelota llega a la izquierda
                        if pelota_posicion.left < 0:
                            pelota_posicion.midright = (width/2, random.randint(5,700))
                            velocidad_pelota_x = -velocidad_pelota_x
                            score_j2 = score_j2 + 1
                            velocidad_pelota_x = -10
                            pelota_y = random.randint(100, 1340)
                        #Comprobacion de que la pelota llega a la derecha
                        if pelota_posicion.right > width:
                            pelota_posicion.midright = (width/2, random.randint(5,700))
                            velocidad_pelota_x = -velocidad_pelota_x
                            score_j1 = score_j1 + 1
                            velocidad_pelota_x = 10
                            pelota_y = random.randint(100, 1340)
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
                        font = pygame.font.SysFont("Pixeboy.ttf", 100)
                        score_text_j1 = font.render("SCORE " + str(score_j1), True, BLANCO)
                        screen.blit(score_text_j1, [340, 50])
                        font2 = pygame.font.SysFont("Pixeboy.ttf", 100)
                        score_text_j2 = font.render("SCORE " + str(score_j2), True, BLANCO)
                        screen.blit(score_text_j2, [760, 50])
                        pygame.display.flip()
                        # En caso de Ganar el juego se cerrará
                        if (int(score_j1) == 10) or (int(score_j2) == 10):
                            run = False
                            sys.exit()
                            pygame.QUIT()
#####################################################################################################################################################################################################
                elif boton_jugar['seleccionado']:
                    #SI QUIERES SALIR DEL JUEGO
                    pygame.quit()
                    sys.exit()
    # DIBUJAR MENU PRINCIPAL JUEGO
    # Dibujar elementos en pantalla
    screen.blit(fondo, [0, 0])
    screen.blit(boton_jugar['texto'], boton_jugar['rect'])
    screen.blit(boton_salir['texto'], boton_salir['rect'])

    # Cambiar color de fondo de botones al ser seleccionados
    if boton_jugar['seleccionado']:
        boton_jugar['color'] = boton_jugar['color_seleccionado']
    else:
        boton_jugar['color'] = (255, 0, 0)
    if boton_salir['seleccionado']:
        boton_salir['color'] = boton_salir['color_seleccionado']
    else:
        boton_salir['color'] = (255, 0, 0)

    # Dibujar botones en pantalla
    pygame.draw.rect(screen, boton_jugar['color'], boton_jugar['rect'], border_radius=5)
    pygame.draw.rect(screen, boton_salir['color'], boton_salir['rect'], border_radius=5)

    # Crear fuentes de texto
    fuente_titulo = pygame.font.Font("Pixeboy.ttf", 150)
    fuente_botones = pygame.font.Font(None, 50)

    # Crear superficie para título del juego
    titulo = fuente_titulo.render("PONG", True, (255, 255, 255))
    titulo_rect = titulo.get_rect(center=(ancho/2, 200))

    # Crear superficies para los botones
    texto_jugar = fuente_botones.render("PLAY", True, (255, 255, 255))
    texto_jugar_rect = texto_jugar.get_rect(center=boton_jugar['rect'].center)
    texto_salir = fuente_botones.render("EXIT", True, (255, 255, 255))
    texto_salir_rect = texto_salir.get_rect(center=boton_salir['rect'].center)

    # Dibujar título y texto de botones en pantalla
    screen.blit(titulo, titulo_rect)
    screen.blit(texto_jugar, texto_jugar_rect)
    screen.blit(texto_salir, texto_salir_rect)

    # Actualizar la pantalla
    pygame.display.update()

    ####################################################################################################################################################################################