import cwiid
import time

def dry(w: cwiid.Wiimote):
    print(w.state['ir_src'])
    for sorg in w.state['ir_src']: # per ogni sorgente IR letta dal wiimote
        if sorg is not None:
            posix = sorg['pos'] # tupla coordinate
            print(posix[0], ', ', posix[1], ', ', sorg['size'])


print("Connetto...")
wm = cwiid.Wiimote()
print("Connessione effettuata")
wm.led = 3
time.sleep(1)
wm.led = 5

wm.rpt_mode = cwiid.RPT_IR # chiedo che mi mandi i dati degli IR
print(wm.state)


for i in range(1000):
    #print(wm.state['ir_src'])
    dry(wm)
    time.sleep(0.02)

print("Fine!\n")