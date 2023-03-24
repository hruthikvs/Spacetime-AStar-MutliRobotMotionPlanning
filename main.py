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

r1 = Robot(robotid = 1,mapid=1,start=[14,4],goal=[9,8])
r2 = Robot(robotid = 2,mapid=1,start=[14,18],goal=[9,7])
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
r2.getPath()

path1 = r1.pathSpacetime
path2 = r2.pathSpacetime
print('SpaceTime', path1)
# set_tot = r1.path_set.union(r2.path_set)
# r3.getPath(set_tot)


'''Plot Map'''


# # #Pseudo Code
r1.t = 0
r2.t = 0
t=0
T= 20
while not (r1.goal_reached and r2.goal_reached):
    
    print('Robot 1 :',path1[r1.t][:2],'t=',r1.t if r1.t>r2.t else r2.t)
    print('Robot 2:',path2[r2.t][:2])
    
    
     
    if np.linalg.norm(np.array(path1[r1.t])-np.array(path2[r2.t]))<=2.0:
        
        print('------Robot reached Closeby--------')
        
        #update start of robots
        
        r1.start = list(path1[r1.t][:2])
        r2.start = list(path2[r2.t][:2])
        
        r1.getPath()
        r2.getPath(r1.path_set)
        
        new_path1 = r1.pathSpacetime
        new_path2 = r2.pathSpacetime
        print('Spacetime',new_path1)
        path1[r1.t+1:] = new_path1[1:]
        path2[r2.t+1:] = new_path2[1:]
        
    time.sleep(1 )
    
    '''Maps plotting'''
    map_plot_copy[path1[r1.t][0]][path1[r1.t][1]] = 13
    map_plot_copy[path2[r2.t][0]][path2[r2.t][1]] = 10
     
    plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
    plt.imshow(map_plot_copy, cmap=plt.cm.tab20c, norm= plot_colormap_norm)
    plt.show()
    
    t+=1
     
    if r1.isGoalState(list(path1[r1.t][:2])):
        r1.goal_reached = True
    if r2.isGoalState(list(path2[r2.t][:2])):
        r2.goal_reached = True
    
    if not r1.goal_reached:
        r1.t = t
    if not r2.goal_reached:
        r2.t = t
    



