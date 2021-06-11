import pygame as pg
import configurazioni

line_extra = 5

def draw_cursore(screen, posizione, colore):
    pg.draw.circle(screen, colore, posizione, configurazioni.cursore_raggio_inner)
    pg.draw.circle(screen, colore, posizione, configurazioni.cursore_raggio, configurazioni.cursore_stroke)
    pg.draw.line(screen, colore, (posizione[0] - configurazioni.cursore_raggio - line_extra, posizione[1]), (posizione[0] + configurazioni.cursore_raggio + line_extra, posizione[1]))
    pg.draw.line(screen, colore, (posizione[0], posizione[1] + configurazioni.cursore_raggio + line_extra), (posizione[0], posizione[1] - configurazioni.cursore_raggio - line_extra))