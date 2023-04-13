#!/usr/bin/env python

"""
Multi robot simulation setup
Changed Sim__init()
@author: Bijo Sebastian 
"""

#Import libraries
import time

#Import files
import sim_interface

sim_interface.sim_init()

#Create three robot and setup interface for all three 
robot1 = sim_interface.Pioneer(1)
robot2 = sim_interface.Pioneer(2)
robot3 = sim_interface.Pioneer(3)
         
def RobotMove(x1,x2,x3):
    if (True):

        
        
        #Start simulation
        if (sim_interface.start_simulation()):
            
            robot1.goal_state = [x1[0] - 0.5 , x1[1] - 0.5]
            robot2.goal_state = [x2[0] - 0.5 , x2[1] - 0.5]
            robot3.goal_state = [x3[0] - 0.5 , x3[1] - 0.5]
                    
            while not robot1.robot_at_goal() or not robot2.robot_at_goal() or not robot3.robot_at_goal():
                #Run the control loops for three robots
                robot1.run_controller()
                robot2.run_controller()
                robot3.run_controller()
                
        else:
            print ('Failed to start simulation')
    else:
        print ('Failed connecting to remote API server')
    
    #shutdown
    #sim_interface.sim_shutdown()
    # time.sleep(2.0)
    return

#run
if __name__ == '__main__':

    RobotMove([1,2], [9,9], [9,8])()                    
    print ('Program ended')
            

 