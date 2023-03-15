# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:55:37 2023

@author: Hruthik V S
"""

import search
from robot import Robot
import maze_maps
from matplotlib import pyplot as plt
import matplotlib

import numpy as np
import time
import copy

r1 = Robot(robotid = 1,mapid=1,start=[14,1],goal=[8,8])
r2 = Robot(robotid = 2,mapid=1,start=[14,15],goal=[8,8])
# r3 = Robot(mapid=1,start=[14,17],goal=[12,1])

print('-----Plotting------')
'''Maps plotting'''

maze_map = maze_maps.maps_dictionary[1]
map_plot_copy = copy.deepcopy(maze_map.map_data)

map_plot_copy[r1.start[0]][r1.start[1]] = maze_maps.start_id
map_plot_copy[r2.start[0]][r2.start[1]] = maze_maps.start_id
map_plot_copy[r1.goal[0]][r1.goal[1]] = maze_maps.goal_id
map_plot_copy[r2.goal[0]][r2.goal[1]] = maze_maps.goal_id
plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
plt.imshow(map_plot_copy, cmap=plt.cm.tab20c, norm= plot_colormap_norm)
plt.show()


#r2.plot_map()
r1.getPath() 
r2.getPath(r1.path_set)

path1 = r1.pathSpacetime
path2 = r2.pathSpacetime
print('SpaceTime', path2)
# set_tot = r1.path_set.union(r2.path_set)
# r3.getPath(set_tot)


'''Plot Map'''


# # #Pseudo Code
t = 1

T= 20
while (t<T):
    print('Robot 1 :',path1[t][:2],'t=',t)
    print('Robot 2:',path2[t][:2])
    
    
     
    if np.linalg.norm(np.array(path1[t])-np.array(path2[t]))<=2.0:
        
        print('------Robot reached Closeby--------')
        
        #update start of robots
        r1.start = list(path1[t][:2])
        r2.start = list(path2[t][:2])
        
        r1.getPath()
        r2.getPath(r1.path_set)
        
        new_path1 = r1.pathSpacetime
        new_path2 = r2.pathSpacetime
        
        path1[t+1:] = new_path1[t+1:]
        path2[t+1:] = new_path2[t+1:]
        
    time.sleep(0.4 )
    
    '''Maps plotting'''
    map_plot_copy[path1[t][0]][path1[t][1]] = 13
    map_plot_copy[path2[t][0]][path2[t][1]] = 10
    plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
    plt.imshow(map_plot_copy, cmap=plt.cm.tab20c, norm= plot_colormap_norm)
    plt.show()
    
    t+=1



