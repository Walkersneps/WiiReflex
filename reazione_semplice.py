import pygame
from pygame.locals import*
import sys
import datetime
import random as rd
import configurazioni

pygame.init()
img = pygame.image.load('sprites/warning.jpg')

black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
w = configurazioni.screen_res_x
h = configurazioni.screen_res_y

#grafico età e funzione interpolazione
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

y = [18, 28, 38, 48, 58, 68, 78, 88]
x = [296, 371, 456, 553, 661, 781, 912, 1055]

f = interp1d(x, y)
f2 = interp1d(x, y, kind='quadratic')

xnew = np.linspace(296, 1055, num= 50, endpoint=True)

#istante random in cui compare l'immagine
t_wait = datetime.timedelta(seconds=rd.randint(2, 7))

font = pygame.font.Font('freesansbold.ttf', 32)



#screen = pygame.display.set_mode((w, h))



def gioco_reazione_semplice(screen):
    screen.fill(black)
    interrotto = False
    readyToExit = False

    t_start = datetime.datetime.now()
    while (datetime.datetime.now() - t_start) < t_wait: 
        screen.fill(black)
        pygame.display.flip()


    t_start = datetime.datetime.now()
    while 1:
        screen.fill(black)
        if not interrotto:
            screen.blit(img,(400,250))
        else:
            screen.blit(text, textRect)
        pygame.display.flip()
        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    if readyToExit:
                        return

                    tempo_riflesso = datetime.datetime.now() - t_start
                    tempo_riflesso_ms= int(tempo_riflesso / datetime.timedelta(milliseconds=1))

                    if tempo_riflesso_ms < 296:
                        text = font.render("Velocissimo! La tua età di reazione è 18 anni", True ,green, blue)
                        textRect = text.get_rect()
                        textRect.center = (w // 2, h // 2)
                        interrotto = True
                        readyToExit = True
                    elif tempo_riflesso_ms > 1055:
                        text = font.render("La tua età di reazione è superiore ai 90 anni!", True ,green, blue)
                        textRect = text.get_rect()
                        textRect.center = (w // 2, h // 2)
                        interrotto = True
                        readyToExit = True
                    elif tempo_riflesso_ms >= 296 and tempo_riflesso_ms <= 1055 :
                        età_riflesso = int(f(tempo_riflesso_ms))
                        testo = "la tua età di reazione è {} anni! ({} ms)".format(età_riflesso, tempo_riflesso_ms)
                        text = font.render(testo, True ,green, blue)
                        textRect = text.get_rect()
                        textRect.center = (w // 2, h // 2)
                        interrotto = True
                        readyToExit = True
                    


#text = font.render("il tuo tempo di rezione è : {} ms   La tua età cerebrale è: {} ",tempo_riflesso_ms, str(età_riflesso)), True,green, blue)






                


                
        

