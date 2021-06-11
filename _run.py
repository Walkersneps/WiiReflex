import pygame as pg
import cwiid
import esegui_calibrazione
import configurazioni
import time
import colors


print("Connetto...")
wm = cwiid.Wiimote()
print("Connessione effettuata")
wm.rpt_mode = cwiid.RPT_IR
wm.led = 3
time.sleep(1)
wm.led = 5



pg.init()
screen = pg.display.set_mode((configurazioni.screen_res_x, configurazioni.screen_res_y))

"""
while 1:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
    screen.fill(colors.GREEN)
    pg.display.flip()
"""

parametri = esegui_calibrazione.esegui_calibrazione(screen, wm)
print(parametri)