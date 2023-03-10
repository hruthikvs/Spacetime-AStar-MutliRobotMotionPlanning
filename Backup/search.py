# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:50 2023

@author: Bijo Sebastian
"""
from matplotlib import pyplot as plt

"""
Implement your search algorithsm here
"""

import operator

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
    
    print(fringe) 
    fringe[0].append(0)
    print(problem.getSuccessors(fringe[0]))
    print(problem.getGoalState())
    i=0
    fin = 0
    while fringe and not problem.isGoalState(fringe[0][:2]):
        print(fringe)
        curr = fringe.pop(0)
         
        close.append(curr) 
         
        succ = problem.getSuccessors(curr)
        
        for ele,mv,_ in succ:
            
            
            if ele not in close and ele not in fringe:
                fringe.append(ele)
                parent[tuple(ele)] = (tuple(curr),mv)
            
        i+=1
    
    
    print('Nodes Expanded =',i) 
    
    node =  tuple(fringe[0])
    res = []
     
  
    i=0 
    res_2 =[]
    while list(node) != problem.getStartState():
        res_2.append(parent[node]) 
        res.append(parent[node][1])
        
        node = parent[node][0]
        i+=1 
    print('Nodes:',[i for i in reversed(res_2)])   
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
  