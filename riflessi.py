import time
import pygame as pg
import random as rd
import wii, configurazioni, colors
from datetime import datetime as time
from datetime import timedelta


target_raggio = 50


    

def gioco_riflessi(screen, wm, parametri, puntatore_sprite, puntatore_hitbox):
    showing = False 

    for i in range(configurazioni.riflessi_numero_runs):
        new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)

        # Randomizzo posizione target e tempo d'attesa
        target_x = rd.randint(target_raggio, configurazioni.screen_res_x - target_raggio)
        target_y = rd.randint(target_raggio, configurazioni.screen_res_y - target_raggio)
        t_wait = timedelta(milliseconds=rd.randint(configurazioni.riflessi_max_wait, configurazioni.riflessi_max_wait))

        # Mostro cursore mentre aspetto che appaia il target
        t_start_wait = time.now()
        while (time.now() - t_start_wait) > t_wait:
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()

            old_x, old_y = new_x, new_y
            new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)
            delta_x = new_x - old_x
            delta_y = new_y - old_y

            puntatore_hitbox.move_ip(delta_x, delta_y)

            screen.fill(colors.BLACK)
            screen.blit(puntatore_sprite, puntatore_hitbox)
            pg.display.flip()

        # Adesso sono passati t_wait secondi di vuoto --> mostro anche il target
        t_start = time.now()
        while 1:
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()
            
            pg.draw.circle(screen, colors.GREEN, (target_x, target_y), target_raggio)

            old_x, old_y = new_x, new_y
            new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)
            delta_x = new_x - old_x
            delta_y = new_y - old_y

            puntatore_hitbox.move_ip(delta_x, delta_y)

            screen.fill(colors.BLACK)
            screen.blit(puntatore_sprite, puntatore_hitbox)
            pg.display.flip()

            if (target_x - target_raggio) <= new_x <= (target_x + target_raggio) and (target_y - target_raggio) <= new_y <= (target_y + target_raggio):
                tempo_riflesso = time.now() - t_start
                break
        
        print("Tempo di riflesso " + str(i) + "-esimo: " + str(tempo_riflesso / timedelta(milliseconds=1)))

