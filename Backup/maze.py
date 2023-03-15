    # -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
"""

import search
import copy
import maze_maps
import matplotlib
import matplotlib.pyplot as plt

class Maze:
  """
  This class outlines the structure of the maze problem
  """
  
  maze_map = []# To store map data, start and goal points
  
  # Legal moves
  # [delta_x, delta_y, description]
  #TODO
  four_neighbor_actions = {'stay':[0, 0, 1],'up':[-1, 0, 1], 'down':[1, 0, 1], 'left': [0, -1, 1], 'right': [0, 1, 1]}
  
  #Setup plot
  map_plot_copy = []
  plot_colormap_norm = matplotlib.colors.Normalize(vmin=0.0, vmax=19.0)
  fig,ax = plt.subplots(1)
  plt.axis('equal')
  
  
  def plot_map(self):
      
      
        """ Plot """
        start = self.getStartState()
        goal = self.getGoalState()
        self.map_plot_copy[start[0]][start[1]] = maze_maps.start_id
        self.map_plot_copy[goal[0]][goal[1]] = maze_maps.goal_id
        print(self.map_plot_copy)
        plt.imshow(self.map_plot_copy, cmap=plt.cm.tab20c, norm=self.plot_colormap_norm)
        #plt.show()
      
  # default constructor
  def __init__(self, id):
          """
          Sets the map as defined in file maze_maps
          """
          #Set up the map to be used
          self.maze_map = maze_maps.maps_dictionary[id]
          self.map_plot_copy = copy.deepcopy(self.maze_map.map_data)
          self.plot_map()
          return
     
  def getStartState(self):
         """
         Returns the start state for the search problem 
         """
         start_state = self.maze_map.start
         return start_state
 
  def getGoalState(self):
         """
         Returns the start state for the search problem 
         """
         goal_state =  self.maze_map.goal
         return goal_state
        
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
         #Update changes on the plot copy
         #TODO CHanges
         self.map_plot_copy[state[0]][state[1]] = maze_maps.expanded_id
         
         successors = []
         for action in self.four_neighbor_actions:
             
             #Get indiivdual action
             #TODO
             del_x, del_y, del_t  = self.four_neighbor_actions.get(action)
             
             #Get successor
             #TODO
             new_successor = [state[0] + del_x , state[1] + del_y, state[2] + del_t ]
             new_action = action
             
             # Check for obstacle 
             if self.maze_map.map_data[new_successor[0]][new_successor[1]] == maze_maps.obstacle_id:
                 continue
              
             #Update changes on the plot copy
             if self.map_plot_copy[new_successor[0]][new_successor[1]] != maze_maps.expanded_id:
                 self.map_plot_copy[new_successor[0]][new_successor[1]] = maze_maps.fringe_id
             
             #Check cost
             if self.maze_map.map_data[new_successor[0]][new_successor[1]] == maze_maps.free_space_id2:
                 new_cost = maze_maps.free_space_id2_cost
             else:
                 new_cost = maze_maps.free_space_id1_cost 
                 
             successors.append([new_successor, new_action, new_cost])
             
         #Plot the changes
         self.plot_map()
         return successors

if __name__ == '__main__':
    
        current_maze = Maze(1)
        path = search.breadthFirstSearch(current_maze)
        if path:
            print('Found a path of %d moves: %s' % (len(path), str(path))) 
            #Display solution
            row,col,time = current_maze.getStartState() 
            for action in path:
                del_x, del_y, del_t = current_maze.four_neighbor_actions.get(action)
                newrow = row + del_x
                newcol = col + del_y
                newtime = time + del_t
                #Update changes on the plot copy
                current_maze.map_plot_copy[newrow][newcol] = 10
                row = newrow
                col = newcol
            #Plot the solution
            current_maze.plot_map()
            
        else:
            print("Could not find a path")
        
    
 