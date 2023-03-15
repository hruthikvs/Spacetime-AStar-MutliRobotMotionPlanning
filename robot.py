# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:53:05 2023

@author: Hruthik V S
"""
import maze_maps
from matplotlib import pyplot as plt
import copy
import matplotlib
from maze import Maze
import search 

class Robot():
    
    
    four_neighbor_actions = {'stay':[0, 0, 1],'up':[-1, 0, 1], 'down':[1, 0, 1], 'left': [0, -1, 1], 'right': [0, 1, 1]}
  
    #Setup plot
    map_plot_copy = []
    plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
    fig,ax = plt.subplots(1)
    plt.axis('equal')
     
    def __init__(self,mapid,start,goal):
        self.mapid = mapid
        self.maze_map = maze_maps.maps_dictionary[mapid]
        self.start = start
        self.goal = goal 
        self.map_plot_copy = copy.deepcopy(self.maze_map.map_data)
        #to store path of robot after generation
        self.path =[]
        
        self.pathSpacetime = []
        self.path_set = set()
        #self.plot_map()
        
        
    def plot_map(self):
      
      
        """ Plot """ 
        self.current_maze.plot_map()
        #plt.show()
        
    def getStartState(self):
         """
         Returns the start state for the search problem 
         """
         return self.current_maze.getStartState()
 
    def getGoalState(self):
         """
         Returns the start state for the search problem 
         """
         return self.current_maze.getGoalState()
 
     
    def isGoalState(self, state):
         """
           state: Search state
        
         Returns True if and only if the state is a valid goal state
         """
         if state == self.getGoalState():
             return True
         else:
             return False

    def getSuccessors(self, state):
         """
           state: Search state
         
         For a given state, this should return a list of triples, 
         (successor, action, stepCost), where 'successor' is a 
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental 
         cost of expanding to that successor
         """
         
         return self.current_maze.getSuccessors(state, self.occupied_path_set)
     
    
        
        
    def getPath(self, occupied_path_set=set()):
        #setting occupied path from previous robots
        
        
        current_maze =  Maze(self.mapid,self.start,self.goal, occupied_path_set)
        self.path = search.breadthFirstSearch(current_maze)
        if self.path:
            print('Found a path of %d moves: %s' % (len(self.path), str(self.path))) 
            #Display solution
            row,col,time =  current_maze.getStartState() 
            self.pathSpacetime.append((row,col,time))
            for action in self.path:
                del_x, del_y, del_t = current_maze.four_neighbor_actions.get(action)
                newrow = row + del_x
                newcol = col + del_y
                newtime = time + del_t
                #Update changes on the plot copy
                current_maze.map_plot_copy[newrow][newcol] = 10
                row = newrow
                col = newcol
                time = newtime
                
                self.pathSpacetime.append((row,col,time))
            
            self.path_set = set(self.pathSpacetime)
            #Plot the solution
            current_maze.plot_map()
            return self.path
        else:
            print("Could not find a path")