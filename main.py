# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:55:37 2023

@author: Hruthik V S
"""



#NOTE: Tune value of cose for Wait and proceed

import search
from robot import Robot
import maze_maps


r1 = Robot(mapid=1,start=[14,1],goal=[1,2])
r2 = Robot(mapid=1,start=[14,10],goal=[1,5])

#r2.plot_map()

print(r2.getPath())



