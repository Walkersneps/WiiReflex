import sys, pygame
pygame.init()

screenSize = width, height = 1900, 1060
black = 0, 0, 0

# Creo la finestra
screen = pygame.display.set_mode(screenSize)

# Carico lo sprite
ch = pygame.image.load("sprites/crosshair_1.png")
ch_hitbox = ch.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Recupero spostamento del mouse (sostituiremo con il wiimote) dall'ultimo controllo
    deltax, deltay = pygame.mouse.get_rel()
    
    ch_hitbox = ch_hitbox.move(deltax, deltay)

    # sfondo nero
    screen.fill(black)

    # blit() copia i pixel di ch in posizione ch_hitbox
    screen.blit(ch, ch_hitbox)

    # mostro quello che ho disegnato
    pygame.display.flip()