wii_max_x = 1024
wii_max_y = 768

screen_res_x = 1900
screen_res_y = 1060

polling_timeout = 15 # sec
polling_f_sample = 100 # Hz --- fps (frames/sec)

update_frequency = 70 # Hz --- fps (frames/sec)

riflessi_numero_runs = 7
riflessi_min_wait = 500
riflessi_max_wait = 2000

cursore_stroke = 5
cursore_raggio = 50
cursore_raggio_inner = 5

calibrazione_savepath = 'calib.npy'
calibrazione_minDist_x = (3/5) * wii_max_x
calibrazione_minDist_y = (3/5) * wii_max_y

menu_nbtn = 6
menu_offset = 50



# -o-o-o-o-o-o-o-o-o-o-o-o-o-

screenSize = (screen_res_x, screen_res_y)
polling_max_samples = polling_timeout * polling_f_sample
polling_T_sample = 1 / polling_f_sample
update_period = 1 / update_frequency