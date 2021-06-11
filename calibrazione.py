import numpy as np
from scipy.linalg import solve

wii_max_x = 1024
wii_max_y = 768


def calibrazione(wii_coords, screen_coords) -> np.ndarray:
    """Calcola gli 8 parametri di conversione coordinate

    Parameters
    ----------
    screen_coords:
        array di 4 tuple (x, y) delle coordinate dei punti di calibrazione impostati su schermo
    wii_coords:
        array di 4 tuple (x, y) delle coordinate dei rilevate dal wiimote in prossimità dei punti di calibrazione
    """
    A = np.empty((8, 8))
    x = np.empty(8)

    # Costruisco A ed x
    for punto in range(4):
        riga_a = 2*punto
        riga_b = riga_a + 1

        A[riga_a] = ( wii_coords[punto][0], wii_coords[punto][1], 1, 0, 0, 0, -screen_coords[punto][0] * wii_coords[punto][0], -screen_coords[punto][0] * wii_coords[punto][1] )
        A[riga_b] = ( 0, 0, 0, wii_coords[punto][0], wii_coords[punto][1], 1, -screen_coords[punto][1] * wii_coords[punto][0], -screen_coords[punto][1] * wii_coords[punto][1] )

        x[riga_a] = ( screen_coords[punto][0] )
        x[riga_b] = ( screen_coords[punto][1] )
    
    # Calcolo il prodotto Ah = x
    # h = np.matmul(A, x)
    h = solve(A, x)
    return h


def wii_to_screen(wii_coords, screen_res) --> (screen_x, screen_y):
    A_riga_1 = (wii_coords[0], wii_coords[1], 1, 0, 0, 0, 0, -scr)