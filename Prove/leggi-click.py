#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame as pg
import random as rd
import sys
import math


# In[2]:


res_x = 900
res_y = 640
raggio = 50
locations = []
GREEN = (0,255,0)


# In[ ]:


pg.init()
screen = pg.display.set_mode((res_x,res_y))
pg.display.set_caption('WINDOW')

for i in range(10):
    x_dot = rd.randint(raggio, res_x-raggio)
    y_dot = rd.randint(raggio, res_y-raggio)
    locations.append((x_dot, y_dot))
    t_random = rd.randint(500, 2000)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        else:
            for locate in locations:
                if event.type == pg.MOUSEBUTTONDOWN: 
                    pg.draw.circle(screen, GREEN, locate, 20)
                    print('{}', locate)
                    pg.display.update()
                    p_x = event.pos[0]
                    p_y = event.pos[1]
                    P_event = (p_x, p_y)
                    distanza = math.sqrt((100-p_x)**2+(100-p_y)**2)
                    print('La distanza tra i centri è: {}', distanza)
                    print('Hai fatto click in x=',p_x,' e y=',p_y)
            
pg.display.flip()          


# In[25]:





# In[ ]:





# In[4]:





# In[ ]:




