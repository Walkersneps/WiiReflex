import pygame as pg
import cwiid
import colors, wii, coordinate
import configurazioni as cfg
import calibrazione, riflessi

print("#########################")
print("-o-o-o- WiiReflex -o-o-o-")
print("#########################\n")

print("### Caricamento...")

print("Inizializzazione PyGame")
pg.init()
screen = pg.display.set_mode((cfg.screen_res_x, cfg.screen_res_y))

print("     - carico fonts...")
font = pg.font.Font('freesansbold.ttf', 32)
print("     - renderizzo testi...")
testi = ["Connetti WiiMote",
         "Calibrazione",
         "Carica parametri",
         "Salva Parametri",
         "Test Riflessi",
         "Test Santa"]
scritte = []
for i in range(len(testi)):
    scritte.append(font.render(testi[i], True, colors.WHITE))


def draw_bottoni(screen):
    btn_size = (cfg.screen_res_x / 3, 50)
    for i in range(cfg.menu_nbtn):
        btn_pos = (cfg.screen_res_x / 3, int( (i + 1/2) * ((cfg.screen_res_y - cfg.menu_offset) / cfg.menu_nbtn)))
        pg.draw.rect(screen, colors.GRAY, [btn_pos[0], btn_pos[1], btn_size[0], btn_size[1]])
        screen.blit(scritte[i], (btn_pos[0] + 30, btn_pos[1]))




"""
print("Connessione WiiMote...")
wm = cwiid.Wiimote()
print("Connessione effettuata!")
wm.rpt_mode = cwiid.RPT_IR
wm.led = 5
wii.rumble_alert(wm)
"""



pg.display.set_caption('WiiReflex - Menu Principale')
while 1:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                

    screen.fill(colors.BLACK)
    draw_bottoni(screen)
    pg.display.flip()





"""
print("## Calibrazione")
pg.display.set_caption('CALIBRAZIONE')
parametri = calibrazione.esegui_calibrazione(screen, wm)
print(parametri)
print("    eseguita!\n")

print("## Caricamento Assets PyGame")
#puntatore_sprite = pg.image.load('sprites/MIRINO_BIANCO.PNG')
#puntatore_hitbox = puntatore_sprite.get_rect()
pg.display.set_caption('WiiReflex')
print("    fatto!")

#new_x, new_y = coordinate.wii_to_screen(wii.next_coords(wm), parametri)


riflessi.gioco_riflessi(screen, wm, parametri)
"""

"""
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
    screen.blit(puntatore_sprite, puntatore_hitbox)
    pg.display.flip()

"""