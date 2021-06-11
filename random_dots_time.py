#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pygame as pg
import random as rd


# In[5]:


res_x = 900
res_y = 640
raggio = 50
locations = []
GREEN = (0,255,0)


# In[7]:


pg.init()
screen= pg.display.set_mode((res_x,res_y))
pg.display.set_caption('RANDOM DOTS')

for i in range(10):
    x_dot = rd.randint(raggio, res_x-raggio)
    y_dot = rd.randint(raggio, res_y-raggio)
    locations.append((x_dot, y_dot))

for locate in locations:
    pg.draw.circle(screen, GREEN, locate, 10)
    pg.display.update()
    pg.time.delay(1000)

pg.display.flip()


# In[ ]:





# In[ ]:




