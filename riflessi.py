import sys, math
import pygame as pg
import random as rd
import numpy as np
import pyedflib
import wii, configurazioni, colors, coordinate, grafica
from datetime import datetime as time
from datetime import timedelta


target_raggio = 50


    

#def gioco_riflessi(screen, wm, parametri, edfwriter: pyedflib.EdfWriter):
def gioco_riflessi(screen, wm, parametri):
    tempi = []
    distanze = []

    for i in range(configurazioni.riflessi_numero_runs):
        new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)

        # Randomizzo posizione target e tempo d'attesa
        target_x = rd.randint(target_raggio, configurazioni.screen_res_x - target_raggio)
        target_y = rd.randint(target_raggio, configurazioni.screen_res_y - target_raggio)
        t_wait = timedelta(milliseconds=rd.randint(configurazioni.riflessi_max_wait, configurazioni.riflessi_max_wait))

        # Mostro cursore mentre aspetto che appaia il target
        t_start_wait = time.now()
        while (time.now() - t_start_wait) < t_wait:
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()

            screen.fill(colors.BLACK)
            grafica.draw_cursore(screen, coordinate.wii_to_screen(wii.next_coords(wm), parametri), colors.WHITE)
            pg.display.flip()

        # Adesso sono passati t_wait secondi di vuoto --> mostro anche il target
        curpos = coordinate.wii_to_screen(wii.next_coords(wm), parametri)
        distanze.append(math.sqrt(((curpos[0] - target_x)**2) + ((curpos[1] - target_y)**2)))
        t_start = time.now()
        while 1:
            for event in pg.event.get():
                    if event.type == pg.QUIT:
                        sys.exit()
            
            """
            old_x, old_y = new_x, new_y
            new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)
            delta_x = new_x - old_x
            delta_y = new_y - old_y
            """

            new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)

            #puntatore_hitbox.move_ip(delta_x, delta_y)

            screen.fill(colors.BLACK)
            pg.draw.circle(screen, colors.GREEN, (target_x, target_y), target_raggio)
            #pg.draw.circle(screen, colors.WHITE, (new_x, new_y), target_raggio)
            grafica.draw_cursore(screen, (new_x, new_y), colors.WHITE)
            pg.display.flip()

            if (target_x - target_raggio) <= new_x <= (target_x + target_raggio) and (target_y - target_raggio) <= new_y <= (target_y + target_raggio):
                tempo_riflesso = time.now() - t_start
                break
        
        t_rflx_ms = tempo_riflesso / timedelta(milliseconds=1)
        print("Tempo di riflesso " + str(i) + "-esimo: " + str(t_rflx_ms))
        tempi.append(t_rflx_ms)

    """
    # Salvo sull'edf
    edfwriter.setSignalHeader(0, {"label": "tempi di reazione", "dimension": "ms", "sample_rate": 1,
                                             "physical_max": max(tempi), "physical_min": min(tempi),
                                             "digital_max": 32767, "digital_min": -32768})
    edfwriter.writeSamples(tempi)
    edfwriter.setSignalHeader(1, {"label": "distanze alla comparsa", "dimension": "px", "sample_rate": 1,
                                             "physical_max": max(distanze), "physical_min": min(distanze),
                                             "digital_max": 32767, "digital_min": -32768})
    edfwriter.writeSamples(distanze)
    edfwriter.close()
    """

    # Salvo file
    np.save(configurazioni.riflessi_savepath, np.array([tempi, distanze]))
