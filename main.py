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


mapid = 1

#Case 1 : Path Clash
# r1 = Robot(robotid = 1,mapid=1,start=[14,5],goal=[12,14])
# r2 = Robot(robotid = 2,mapid=1,start=[14,18],goal=[12,6])

# #Case 2 : Goal Block

r1 = Robot(robotid = 1,mapid=1,start=[14,4],goal=[9,8])
r2 = Robot(robotid = 2,mapid=1,start=[14,18],goal=[9,5])

# #Case 3 : Rnadom Location
# r1 = Robot(robotid = 1,mapid=1,start=[14,4],goal=[4,17])
# r2 = Robot(robotid = 2,mapid=1,start=[14,18],goal=[9,5])

# #Case 4 : obstacle with map 4

# r1 = Robot(robotid = 1,mapid=4,start=[12,18],goal=[12,6])
# r2 = Robot(robotid = 2,mapid=4,start=[12,5],goal=[12,15])


print('-----Plotting------')
'''Maps plotting'''

maze_map = maze_maps.maps_dictionary[mapid]
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

replan_flag = 0
while not (r1.goal_reached and r2.goal_reached):
    
    if not r1.goal_reached:
        r1.t = t
    if not r2.goal_reached:
        r2.t = t
        
    if r1.isGoalState(list(path1[r1.t][:2])) and not r1.goal_reached:
        r1.goal_reached = True
        replan_flag = 1
        'create obstacle in all maps at goal position'
        r1.maze_map.map_data[r1.getGoalState()[0]][r1.getGoalState()[1]] = 16
        r2.maze_map.map_data[r1.getGoalState()[0]][r1.getGoalState()[1]] = 16
        
        print('-----Robot1 Goal Reached------')
        
    if r2.isGoalState(list(path2[r2.t][:2])) and not r2.goal_reached:
        r2.goal_reached = True
        replan_flag = 1
        r1.maze_map.map_data[r2.getGoalState()[0]][r2.getGoalState()[1]] = 16
        r2.maze_map.map_data[r2.getGoalState()[0]][r2.getGoalState()[1]] = 16
        print('-----Robot2 Goal Reached------')
    
    
        
    
    
    print('Robot 1 :',path1[r1.t][:2],'t=',r1.t if r1.t>r2.t else r2.t)
    print('Robot 2:',path2[r2.t][:2])
    
    
    
     
    if np.linalg.norm(np.array(path1[r1.t])-np.array(path2[r2.t]))<=2.0  :
        
        print('\n------Robot reached Closeby--------')
        time.sleep(1)
        #update start of robots
        
            
        r1.start = list(path1[r1.t][:2])
        r2.start = list(path2[r2.t][:2])
        
        r1.getPath()
        
        
        r2.getPath(r1.path_set)
        
        new_path1 = r1.pathSpacetime
        new_path2 = r2.pathSpacetime
        
        print('Spacetime-1: ',new_path1)
        print('Spacetime-2: ',new_path2)
        path1[r1.t+1:] = new_path1[1:]
        path2[r2.t+1:] = new_path2[1:]
        
        
        if r1.isGoalState(list(path1[r1.t][:2])) and not r1.goal_reached:
            r1.goal_reached = True
            replan_flag = 1
            'create obstacle in all maps at goal position'
            r1.maze_map.map_data[r1.getGoalState()[0]][r1.getGoalState()[1]] = 16
            r2.maze_map.map_data[r1.getGoalState()[0]][r1.getGoalState()[1]] = 16
            
            print('-----Robot1 Goal Reached------')
            
        if r2.isGoalState(list(path2[r2.t][:2])) and not r2.goal_reached:
            r2.goal_reached = True
            replan_flag = 1
            r1.maze_map.map_data[r2.getGoalState()[0]][r2.getGoalState()[1]] = 16
            r2.maze_map.map_data[r2.getGoalState()[0]][r2.getGoalState()[1]] = 16
            print('-----Robot2 Goal Reached------')
        
    if replan_flag:
        print('------Replanning---------')
        r1.start = list(path1[r1.t][:2])
        r2.start = list(path2[r2.t][:2])
        
        r1.getPath()
    
        r2.getPath(r1.path_set)
        
        new_path1 = r1.pathSpacetime
        new_path2 = r2.pathSpacetime
        
        print('Spacetime-1: ',new_path1)
        print('Spacetime-2: ',new_path2)
        path1[r1.t+1:] = new_path1[1:]
        path2[r2.t+1:] = new_path2[1:]
        
        replan_flag = 0
        
        
        
        
    time.sleep(0.3 )
    
    '''Maps plotting'''
    if t>0:
        #Robot trail
        map_plot_copy[path1[r1.t-1][0]][path1[r1.t-1][1]] = 2
        map_plot_copy[path2[r2.t-1][0]][path2[r2.t-1][1]] = 7
        
    
        
    
    map_plot_copy[path1[r1.t][0]][path1[r1.t][1]] = 0
    map_plot_copy[path2[r2.t][0]][path2[r2.t][1]] = 4  
    plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
    plt.imshow(map_plot_copy, cmap=plt.cm.tab20c, norm= plot_colormap_norm)
    plt.show()
    
    
    'Plotting Path to goal'
    if False:   
        path_map_plot_copy = copy.deepcopy(map_plot_copy)
        for ele in path1[r1.t+1:]:
            path_map_plot_copy[ele[0]][ele[1]] = 12
        for ele in path2[r2.t+1:]:
            path_map_plot_copy[ele[0]][ele[1]] = 9
        
        path_map_plot_copy[path1[r1.t][0]][path1[r1.t][1]] = 0
        path_map_plot_copy[path2[r2.t][0]][path2[r2.t][1]] = 4  
        plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
        plt.imshow(path_map_plot_copy, cmap=plt.cm.tab20c, norm= plot_colormap_norm)
        plt.show()  
        
        
    t+=1
     
    
    



