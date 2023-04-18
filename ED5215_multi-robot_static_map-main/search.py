# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
modified : Hruthik V S
"""
from matplotlib import pyplot as plt

"""
Implement your search algorithsm here
"""

import operator
import math

def depthFirstSearch(problem):
    """
    Your search algorithm needs to return a list of actions that reaches the goal
    Strategy: Search the deepest nodes in the search tree first
    """
    "*** YOUR CODE HERE ***"
    fringe = []
    close = []
    parent = {}
    
    #Append Start State
    fringe.append(problem.getStartState())
     
    i=0
    fin = 0
    while fringe and not problem.isGoalState(fringe[-1]):
        
        #pop fringe
        curr = fringe.pop()
         
        close.append(curr) 
        
        succ = problem.getSuccessors(curr)
        
        for ele,mv,_ in succ:
            
            
            if ele not in close and ele not in fringe:
                fringe.append(ele)
                parent[tuple(ele)] = (tuple(curr),mv)
                
       
        i+=1
    
    
    print('Nodes Expanded =',i) 
    
    node =  tuple(fringe[-1]) 
    res = []
     
    i=0 
    
    while list(node) != problem.getStartState():
               
        res.append(parent[node][1])
        
        node = parent[node][0]
        i+=1 
        
     
         
    RES = [i for i in reversed(res)]
    
   
 
    return RES
    





def breadthFirstSearch(problem):
    """
    Your search algorithm needs to return a list of actions that reaches the goal
    Strategy: Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    fringe = []
    close = []
    parent = {}
    
    fringe.append(problem.getStartState())
    
    # print(fringe) 
    fringe[0].append(0)
    # print(problem.getSuccessors(fringe[0]))
    # print(problem.getGoalState())
    i=0
    fin = 0
    while fringe and not problem.isGoalState(fringe[0][:2]):
        # print(fringe)
        curr = fringe.pop(0)
         
        close.append(curr) 
         
        succ = problem.getSuccessors(curr)
        
        for ele,mv,_ in succ:
            
            
            if ele not in close and ele not in fringe:
                fringe.append(ele)
                parent[tuple(ele)] = (tuple(curr),mv)
            
        i+=1
    
    
    #print('Nodes Expanded =',i) 
    
    node =  tuple(fringe[0])
    res = []
     
  
    i=0 
    res_2 =[]
    while list(node) != problem.getStartState():
        res_2.append(parent[node]) 
        res.append(parent[node][1])
        
        node = parent[node][0]
        i+=1 
    
   # print('Nodes:',[x for x,_ in reversed(res_2)])   
    RES = [i for i in reversed(res)]
    
    xline = [x[0] for x,_ in  reversed(res_2)]
    yline = [x[1] for x,_ in  reversed(res_2)]
    zline = [x[2] for x,_ in  reversed(res_2)]
    
   
    #TODO
    # ax = plt.axes(projection='3d')
    # ax.plot3D(xline, yline, zline, 'red' , linewidth=10)
    return RES

def uniformCostSearch(problem):
    """
    Your search algorithm needs to return a list of actions that reaches the goal
    Strategy: Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
  
    
    fringe = []
    close = []
    parent = {}
    #cost ={}
    
    fringe.append([problem.getStartState(),0])
     
      
     
    i=0 
      
    while fringe and not problem.isGoalState(fringe[0][0]):
         
        fringe.sort(key=lambda x: x[1])
        curr = fringe.pop(0)
        fringe_wo = [a for a,_ in fringe]
        close.append(curr[0]) 
        succ = problem.getSuccessors(curr[0])
        
        for ele,mv,cost in succ:
            
            if ele not in close and ele not in fringe_wo:
                fringe.append([ele,cost + curr[1]])
                
                parent[tuple(ele)] = (tuple(curr[0]),mv) 
                
            elif ele not in close and ele in fringe_wo:
                
                for idx,f in enumerate(fringe):
                    if f[0]==ele and f[1]>cost+curr[1]:
                        fringe[idx][1] = cost+curr[1]
                        parent[tuple(ele)] = (tuple(curr[0]),mv)
                    
             
       
        i+=1
    
    print('Nodes Expanded =',i) 
    node =  tuple(fringe[0][0])
    res = []
     
    i=0
    while list(node) != problem.getStartState():
      
        res.append(parent[node][1])
        node = parent[node][0]
        
        i+=1
        
     
  
    RES = [i for i in reversed(res)]
    
    return RES
def heuristic_1(problem, state):
    """
    Euclidean distance
    """
    "*** YOUR CODE HERE ***"
    #implimentation for calculating eulcidean distance to goal
    goal_state = problem.getGoalState()
    h = math.sqrt((goal_state[0]-state[0][0])**2+(goal_state[1]-state[0][1])**2)
    return h

def heuristic_2(problem, state):
    """
    Manhattan distance
    """
    "*** YOUR CODE HERE ***"
    #implimentation for calculating manhattan distance to goal
    goal_state = problem.getGoalState()
    h = abs(goal_state[0]-state[0][0])+abs(goal_state[1]-state[0][1])
    return h

def aStarSearch(problem):
    #print(curr_state)
    Fringe = []
    Closed = []
    FC = {}
    Nodes_expanded = 0
    Fringe.append(problem.getStartState())
    if (len(problem.getStartState())==2):
        Fringe[0].append(0)
    Nodes_expanded = Nodes_expanded +1
    curr_state = problem.getStartState()
    FC[tuple(curr_state)] = [[],'Start',0,0]
    Found_Path = 1
    Nodes_expanded = Nodes_expanded +1
    while (problem.isGoalState(Fringe[0][0:2])==0):
        
        curr_state = Fringe[0]
        print(curr_state)
        Closed.append(Fringe.pop(0))
        for st in problem.getSuccessors(curr_state):
            heuristic = heuristic_2(problem, st)
            if st[0] not in Closed :
                if st[0] not in Fringe :
                    FC[tuple(st[0])] = [curr_state,st[1],FC[tuple(curr_state)][2]+st[2],heuristic]
                    Fringe.append(st[0])
                else:
                    if(FC[tuple(curr_state)][2]+st[2]+heuristic<FC[tuple(st[0])][2]+FC[tuple(st[0])][3]):
                        FC[tuple(st[0])] = [curr_state,st[1],FC[tuple(curr_state)][2]+st[2],heuristic]
                    else:
                        continue
        if(len(Fringe)==0):
            Found_Path = 0
            break
        Nodes_expanded = Nodes_expanded +1
        Fringe = sorted(Fringe,key=lambda x:FC[tuple(x)][2]+FC[tuple(x)][3])
    Path = []
    if(Found_Path):
        curr = Fringe[0]
        while (FC[tuple(curr)][1]!='Start'):
            Path.append(FC[tuple(curr)][1])
            curr = FC[tuple(curr)][0]
        Path.reverse()
    print("Number of Nodes Expanded: ",Nodes_expanded)
    return Path