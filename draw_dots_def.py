#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pygame as pg


# In[18]:


res_x = 900
res_y = 640
off_set = 100
radius_big = 50
radius_small = 5
stroke = 5


# In[20]:


pg.init()
screen= pg.display.set_mode((res_x,res_y))
pg.display.set_caption('CALIBRAZIONE')

#COLORI
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)

#ALTO SX
pg.draw.circle(screen, CYAN, (off_set, off_set), radius_big, stroke)
pg.draw.circle(screen, CYAN, (off_set, off_set), radius_small, stroke)

pg.draw.circle(screen, CYAN, (res_x-off_set, off_set), radius_big, stroke)
pg.draw.circle(screen, CYAN, (res_x-off_set, off_set), radius_small, stroke)

pg.draw.circle(screen, CYAN, (res_x-off_set, res_y-off_set), radius_big, stroke)
pg.draw.circle(screen, CYAN, (res_x-off_set, res_y-off_set), radius_small, stroke)

pg.draw.circle(screen, CYAN, (off_set, res_y-off_set), radius_big, stroke)
pg.draw.circle(screen, CYAN, (off_set, res_y-off_set), radius_small, stroke)

pg.display.flip()


# In[ ]:




