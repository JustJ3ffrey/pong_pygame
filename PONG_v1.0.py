import sys,pygame,random
from time import time
from pygame.locals import *
# Inicialización
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("E:\PONG_PYGAME\Menu.mp3")
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

# Bucle principal del juego
while True:
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
                    pygame.mixer.music.load("E:\PONG_PYGAME\Game.mp3")
                    # Juego (PONG)
                    # PANTALLA
                    size=(1440, 800)
                    screen = pygame.display.set_mode(size)
                    ##############################################################################################################################################################
                elif boton_jugar['seleccionado']:
                    #SI QUIERES SALIR DEL JUEGO
                    pygame.quit()
                    pygame.mixer.music.stop(-1)
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