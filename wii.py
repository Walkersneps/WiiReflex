import cwiid
import numpy as np

def poll_full(wm: cwiid.Wiimote) -> list:
    """Recupera dati dal sensore IR dal WiiMote
    Anche sorgenti non presenti
    """
    return wm.state['ir_src']

def poll(wm: cwiid.Wiimote) -> list:
    """Recupera dati delle sorgenti IR rilevate dal WiiMote
    """

    dati = list()
    for sorgente in wm.state['ir_src']:
        if sorgente is not None:
            dati.append(sorgente)

    return dati

def get_wii_coords(ir_source_data) -> (int, int):
    """Ritorna le coordinate Wii della sorgente IR
    """

    return ir_source_data['pos']



def get_ir_source_size(ir_source_data) -> int:
    """Ritorna la dimensione della sorgente IR
    """

    return ir_source_data['size']



def get_best_coords(lista_sorgenti):
    """Ritorna la posizione della sorgente IR più grande
    """

    # lista che contiente tutte le sizes
    sizes = [sorgente.get('size') for sorgente in lista_sorgenti]

    return get_wii_coords(lista_sorgenti[np.argmax(sizes)])

