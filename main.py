# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:55:37 2023

@author: Hruthik V S
"""

import search
from robot import Robot
import maze_maps

import numpy as np
import time

r1 = Robot(mapid=1,start=[14,1],goal=[13,17])
r2 = Robot(mapid=1,start=[14,17],goal=[13,1])
# r3 = Robot(mapid=1,start=[14,17],goal=[12,1])

#r2.plot_map()
r1.getPath() 

print('PATH',r2.getPath(r1.path_set))
path1 = r1.pathSpacetime
path2 = r2.pathSpacetime
print('SpaceTime', path2)
# set_tot = r1.path_set.union(r2.path_set)
# r3.getPath(set_tot)



# # #Pseudo Code
t = 1

T= 10
while (t<T):
    print('Robot 1 :',path1[t])
    print('Robot 2:',path2[t])
     
    if np.linalg.norm(np.array(path1[t])-np.array(path2[t]))<=2.0:
        
        print('------Robot reached Closeby--------')
        
        #update start of robots
        r1.start = list(path1[t][:2])
        r2.start = list(path2[t][:2])
        
        r1.getPath()
        r2.getPath(r1.path_set)
        
        new_path1 = r1.pathSpacetime
        new_path2 = r2.pathSpacetime
        
        path1[t+1:] = new_path1
        path2[t+1:] = new_path2
        
    time.sleep(1)
    t+=1



