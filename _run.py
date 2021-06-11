import pygame as pg
import cwiid
import esegui_calibrazione
import configurazioni
import time
import colors, wii, coordinate

print("-o-o-o- WiiReflex -o-o-o-")

print("Connessione WiiMote...")
wm = cwiid.Wiimote()
print("Connessione effettuata!")
wm.rpt_mode = cwiid.RPT_IR
wm.led = 5
wii.rumble_alert(wm)


print("Inizializzazione PyGame")
pg.init()
screen = pg.display.set_mode((configurazioni.screen_res_x, configurazioni.screen_res_y))

print("## Calibrazione")
pg.display.set_caption('CALIBRAZIONE')
parametri = esegui_calibrazione.esegui_calibrazione(screen, wm)
print(parametri)
print("    eseguita!\n")

print("## Caricamento Assets PyGame")
#sprite_puntatore = pg.image.load('sprites/puntatore.png')
sprite_puntatore = pg.image.load('sprites/crosshair_1.png')
puntatore_hitbox = sprite_puntatore.get_rect()
pg.display.set_caption('WiiReflex')
print("    fatto!")

new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)

while 1:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
    
    old_x, old_y = new_x, new_y
    new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)
    delta_x = new_x - old_x
    delta_y = new_y - old_y

    puntatore_hitbox.move_ip(delta_x, delta_y)

    screen.fill(colors.BLACK)
    screen.blit(sprite_puntatore, puntatore_hitbox)
    pg.display.flip()

