import pygame as pg
import pygame_menu as pgmenu
import numpy as np
#import pyedflib
import colors, wii
import configurazioni as cfg
import calibrazione, riflessi, paziente

wm = wii.persistente()
#edfw = pyedflib.EdfWriter('dati_paziente.edf', 2)

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


def fun_riflessi1(screen, persistente):
    #riflessi.gioco_riflessi(screen, persistente.tele, persistente.parametri, edfw)
    riflessi.gioco_riflessi(screen, persistente.tele, persistente.parametri)


def open_link(*args) -> None:
    link: 'pygame_menu.widgets.MenuLink' = args[-1]
    link.open()

def open_link_andPaziente(*args) -> None:
    link: 'pygame_menu.widgets.MenuLink' = args[-1]
    #paz: 'paziente.persona' = args[-2]

    """
    edfw.setEquipment("WiiReflex")
    edfw.setGender(paz.sesso)
    edfw.setPatientName(paz.nome)
    """

    link.open()



print("#########################")
print("-o-o-o- WiiReflex -o-o-o-")
print("#########################\n")

print("### Caricamento...")

print("Inizializzazione PyGame")
pg.init()
screen = pg.display.set_mode((cfg.screen_res_x, cfg.screen_res_y))

print("  - creo menu")
mainmenu = pgmenu.Menu("Menu Principale", cfg.screen_res_x / 3, cfg.screen_res_y / 2, theme=pgmenu.themes.THEME_SOLARIZED, mouse_motion_selection=True)
menu_paziente = pgmenu.Menu("Dati Paziente", cfg.screen_res_x / 1.5, cfg.screen_res_y / 1.5, theme=pgmenu.themes.THEME_SOLARIZED, mouse_motion_selection=True)
menu_giochi = pgmenu.Menu("Scelta Test", cfg.screen_res_x / 2, cfg.screen_res_y / 2, theme=pgmenu.themes.THEME_SOLARIZED, mouse_motion_selection=True)

link_toPaziente = mainmenu.add.menu_link(menu_paziente)
link_toGiochi = menu_paziente.add.menu_link(menu_giochi)

mainmenu.add.button("Connetti WiiMote", fun_connessione_wiimote, wm)
mainmenu.add.button("Calibrazione", fun_calibrazione, screen, wm)
mainmenu.add.button("Test Riflessi", open_link, "lala", link_toPaziente)
mainmenu.add.button("Carica Ultima Calibrazione", fun_load_params, wm)
mainmenu.add.button("Salva Calibrazione", fun_save_params, wm)
#menu.add.button("Verifiche Tecniche", fun_test, wm)



pzt = paziente.persona()
menu_paziente.add.text_input("Nome e Cognome: ", input_underline='_', onreturn=pzt.salva_nome)
#menu_paziente.add.text_input("Cognome: ", input_underline='_', onreturn=pzt.salva_cognome)
menu_paziente.add.text_input("Età: ", input_underline='_', input_type=pgmenu.locals.INPUT_INT, onreturn=pzt.salva_eta)
menu_paziente.add.dropselect("Sesso: ", [("N/S", 0), ("F", 1), ("M", 2)], onchange=pzt.salva_sesso)
#menu_paziente.add.button("Vai!", open_link, pzt, link_toGiochi)
menu_paziente.add.button("Vai!", open_link, "lalal", link_toGiochi)

menu_giochi.add.button("Riflesso Semplice", fun_riflessi1, screen, wm)

pg.display.set_caption('WiiReflex - Menu Principale')
mainmenu.mainloop(screen)