#%%
import cwiid
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#%%
# Premere 1 e 2 sul wiimote durante l'esecuzione di questo
wm = cwiid.Wiimote()


#%%
wm.led = 4
wm.rpt_mode = cwiid.RPT_IR # chiedo che mi mandi i dati degli IR
wm.state # chiedo info
# %%
for i in range(10000):
    #print(wm.state['ir_src'])
    dry(wm)
    time.sleep(0.01)

# %%
for i in range(10000):
    #print(wm.state['ir_src'])
    anim(wm)
    time.sleep(0.01)

#%%
def anim(w: cwiid.Wiimote):
    plt.cla() # pulisco il frame precedente
    print(wm.state['ir_src'])
    for sorg in w.state['ir_src']: # per ogni sorgente IR letta dal wiimote
        if sorg is not None:
            posix = sorg['pos'] # tupla coordinate
            plt.plot(posix[0], posix[1])

    plt.tight_layout()
    
#%%
def dry(w: cwiid.Wiimote):
    print(wm.state['ir_src'])
    for sorg in w.state['ir_src']: # per ogni sorgente IR letta dal wiimote
        if sorg is not None:
            posix = sorg['pos'] # tupla coordinate
            print(posix[0], ', ', posix[1], ', ', sorg['size'])

# %%
#plt.axis([0, 1000, 0, 1000])
animazione = FuncAnimation(plt.gcf(), anim(wm), interval = 10)
#animazione = FuncAnimation(plt.axis([0, 1000, 0, 1000]), anim, interval = 10)
plt.tight_layout()
plt.show()
# %%

plt.show()
# %%
