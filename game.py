import sys
import numpy as np
from numpy import pi
import pygame, pygame.gfxdraw
pygame.init()



def f_to_pixels(xs, ys, altezza, colore) -> np.ndarray:
    w = xs.size
    out = np.empty((w, altezza, 3), dtype = np.int16)
    for x in range(0, w):
        colonna = np.empty((altezza, 3))
        for y in range(0, altezza):
            if ys[x] == y:
                pixel = np.array(colore)
            else:
                pixel = np.array([255, 255, 255])
            colonna[y] = pixel
        out[x] = colonna
    return out



#screenSize = width, height = 5, 8
screenSize = width, height = 1900, 1060
black = 0, 0, 0

# Creo la finestra
screen = pygame.display.set_mode(screenSize)

# Carico lo sprite
ch = pygame.image.load("sprites/crosshair_1.png")
ch_hitbox = ch.get_rect()

newx, newy = pygame.mouse.get_pos()


# Calcolo pixel per il seno
xs = np.linspace(0, 4*pi, width)
hor_pxs = np.linspace(0, width - 1, width).astype(int)
sinpxls = ((((height-1)/2) * np.sin(xs))+((height-1)/2)).astype(int)
pxls = f_to_pixels(xs, sinpxls, height, (255, 0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Recupero spostamento del mouse (sostituiremo con il wiimote) dall'ultimo controllo
    #deltax, deltay = pygame.mouse.get_rel()

    # Recupero posizione del mouse
    oldx, oldy = newx, newy
    newx, newy = pygame.mouse.get_pos()
    deltax = newx - oldx
    deltay = newy - oldy
    
    ch_hitbox = ch_hitbox.move(deltax, deltay)

    # sfondo nero
    screen.fill(black)

    # blit() copia i pixel di ch in posizione ch_hitbox
    screen.blit(ch, ch_hitbox)

    # Disegno curva di Bezier
    pygame.gfxdraw.bezier(screen, [(0, 0), (100, 120), (500, 635),(1800, 100), (1900, 1000)], 4, (255, 0, 0))

    #print("\neccoje")
    #print(pygame.surfarray.array3d(screen))
    # tre assi:
    #   asse 1: dimensione width --> colonna
    #   asse 2: dimensione heigth --> riga
    #   asse 3: dimensione 3 --> RGB

    # Disegno curva sinusoidale
    sine_surface = pygame.surfarray.make_surface(pxls)
    screen.blit(sine_surface, (0, 0))

    # mostro quello che ho disegnato
    pygame.display.flip()




