import pygame as pg
import pygame_menu as pgmenu
import numpy as np
import colors, wii
import configurazioni as cfg
import calibrazione, riflessi

wm = wii.persistente()

def fun_connessione_wiimote(persistente):
    pg.display.set_caption('WiiReflex - Connessione...')
    print("Connetto tramite oggetto...")
    persistente.connect()
    pg.display.set_caption('WiiReflex - Menu Principale')


def fun_calibrazione(screen, pers):
    if pers.tele is not None:
        pg.display.set_caption('WiiReflex - Calibrazione')
        print("## Calibrazione")
        pers.parametri = calibrazione.esegui_calibrazione(screen, pers.tele)
        print(pers.parametri)
        print("    eseguita!\n")
    else:
        print("Calibrazione annullata perchè WiiMote non connesso.")
    pg.display.set_caption('WiiReflex - Menu Principale')


def fun_load_params(persistente):
    persistente.parametri = calibrazione.leggi_parametri()
    print("Letti parametri:")
    print(persistente.parametri)


def fun_save_params(persistente):
    calibrazione.salva_parametri(persistente.parametri)
    print("Parametri salvati")


def fun_test(persistente):
    print("Parametri sono: ")
    print(persistente.parametri)
    print("\nwm è: ")
    print(type(persistente.tele))



print("#########################")
print("-o-o-o- WiiReflex -o-o-o-")
print("#########################\n")

print("### Caricamento...")

print("Inizializzazione PyGame")
pg.init()
screen = pg.display.set_mode((cfg.screen_res_x, cfg.screen_res_y))

print("  - creo menu")
menu = pgmenu.Menu("Menu Principale", cfg.screen_res_x / 3, cfg.screen_res_y / 2, theme=pgmenu.themes.THEME_SOLARIZED, mouse_motion_selection=True)
menu.add.button("Connetti WiiMote", fun_connessione_wiimote, wm)
menu.add.button("Calibrazione", fun_calibrazione, screen, wm)
menu.add.button("Carica Ultima Calibrazione", fun_load_params, wm)
menu.add.button("Salva Calibrazione", fun_save_params, wm)
menu.add.button("Verifiche Tecniche", fun_test, wm)

pg.display.set_caption('WiiReflex - Menu Principale')
menu.mainloop(screen)