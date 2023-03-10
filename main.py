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



#Pseudo Code

while (t<T):
    
    path1[t]
    path2[t]
    
    if r1 and r2 in vicinity ie |path1[t]-path2[t]|<=root2:
        new_path = r2.replan(path[t],goal2, r1spacetime)
        
        {inside r2 function} = if not rspacetime[i][j][t]: then append node
        
        path1[t+1:] = path1[t+1:]
        path2[t+1:] = new_path



