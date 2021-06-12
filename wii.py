import cwiid
import numpy as np
import time
import configurazioni
import wii # !! serve anche se non sembra (sennò destroyerror)

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


def next_coords(wm: cwiid.Wiimote) -> (int, int):
    """Esegue polling finchè non trova almeno una coppia di coordinate.
    Se ce ne sono di più, ritorna la sorgente più grande
    """

    sorgenti = list()
    areNone = 0
    for _ in range(configurazioni.polling_max_samples):
        sorgenti = poll(wm)
        areNone = sorgenti.count(None)
        if areNone != len(sorgenti):
            break
        else:
            time.sleep(configurazioni.polling_T_sample)

    if areNone == 3:
        return get_wii_coords(sorgenti)
    elif areNone == 4:
        print("\nERRORE: Bad Polling!!")
        print("Rimetti il Polar H9 che non ti sento il battito! xD")
        return sorgenti
    else:
        return get_best_coords(sorgenti)
        


def rumble_alert(wm: cwiid.Wiimote):
    wm.rumble = True
    time.sleep(0.5)
    wm.rumble = False



class persistente:
    def __init__(self):
        self.parametri = None
        self.tele = None

    def connect(self):
        try:
            print("Connessione WiiMote...")
            self.tele = cwiid.Wiimote()
            print("Connessione effettuata!")
            self.tele.rpt_mode = cwiid.RPT_IR
            self.tele.led = 5
            wii.rumble_alert(self.tele)
        except RuntimeError:
            pass
    
    def set_params(self, parametri):
        self.parametri = parametri

    def g_wm(self) -> cwiid.Wiimote:
        return self.tele

    def g_params(self):
        return self.parametri
