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

#Case 1 : Path Clash
# r1 = Robot(robotid = 1,mapid=1,start=[14,5],goal=[12,14])
# r2 = Robot(robotid = 2,mapid=1,start=[14,18],goal=[12,6])

#Case 2 : Goal Block
r1 = Robot(robotid = 1,mapid=1,start=[14,4],goal=[9,8])
r2 = Robot(robotid = 2,mapid=1,start=[14,18],goal=[9,5])

#Case 3 : Rnadom Location
# r1 = Robot(robotid = 1,mapid=1,start=[14,4],goal=[4,17])
# r2 = Robot(robotid = 2,mapid=1,start=[14,18],goal=[9,5])


# Case 4 : Multi Robot 
'number of robots'
n = 2
r = []
for i in range(n):
    while True:
        start_rand,goal_rand = np.random.randint(1,19,size=(2)), np.random.randint(1,18,size=(2))
        if (not (maze_maps.map_data[start_rand[0]][start_rand[1]]==maze_maps.obstacle_id or 
                maze_maps.map_data[goal_rand[0]][goal_rand[1]]==maze_maps.obstacle_id)):
            break
    r.append(Robot(robotid = i,mapid=1,start=list(start_rand),goal=list(goal_rand)))
    

    

print('-----Plotting------')
'''Maps plotting'''

maze_map = maze_maps.maps_dictionary[1]
map_plot_copy = copy.deepcopy(maze_map.map_data)


for i in range(n):
    map_plot_copy[r[i].start[0]][r[i].start[1]] = maze_maps.start_id
    map_plot_copy[r[i].goal[0]][r[i].goal[1]] = maze_maps.goal_id
    
plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
plt.imshow(map_plot_copy, cmap=plt.cm.tab20c, norm= plot_colormap_norm)
plt.show()


#Getting path
path_arr = []
for i in range(n):
    r[i].getPath() 
    path_arr.append(r[i].pathSpacetime)




# set_tot = r1.path_set.union(r2.path_set)
# r3.getPath(set_tot)


'''Plot Map'''


# # #Pseudo Code

for i in range(n):
    r[i].t = 0


t=0
T= 20

replan_flag = 0

stop_planning_flag = 0

while not (stop_planning_flag):
    
    
    'Stop loop'
    var = 1
    for i in range(n):
        var = var and r[i].goal_reached
    stop_planning_flag = var
    
    
    for i in range(n):
        if not r[i].goal_reached:
            r[i].t = t
         
    for i in range(n):        
        if r[i].isGoalState(list(path_arr[i][r[i].t][:2])) and not r[i].goal_reached:
            r[i].goal_reached = True
            replan_flag = 1
            'create obstacle in all maps at goal position'
            for i in range(n):
                r[i].maze_map.map_data[r[i].getGoalState()[0]][r[i].getGoalState()[1]] = 16
             
            
            print('-----Robot {0} Goal Reached------'.format(r[i].robotid))
        
     
        
    
    
    print('t = ',t,' secs')
    for i in range(n):
        print('Robot {0} :'.format(r[i].robotid),path_arr[i][r[i].t][:2])
    
    
    
    
     
    if np.linalg.norm(np.array(path1[r1.t])-np.array(path2[r2.t]))<=2.0 and not r1.goal_reached :
        
        print('\n------Robot reached Closeby--------')
        
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
        map_plot_copy[path2[r2.t-1][0]][path2[r2.t-1][1]] = 6
    
    map_plot_copy[path1[r1.t][0]][path1[r1.t][1]] = 0
    map_plot_copy[path2[r2.t][0]][path2[r2.t][1]] = 4  
    plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
    plt.imshow(map_plot_copy, cmap=plt.cm.tab20c, norm= plot_colormap_norm)
    plt.show()
    
    t+=1
     
    
    



