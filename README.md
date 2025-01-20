# Multi-Robot Path Planning using Spacetime Grids

A robust implementation of multi-robot path planning using spacetime A* search algorithm, designed for efficient trajectory computation in decentralized systems.

## Overview

This project implements a novel framework for multi-robot path planning using spacetime grids. The solution enables multiple robots to compute efficient, collision-free trajectories in real-time while relying on localization sensors and inter-robot wireless communication. The implementation uses the A* search algorithm combined with 3D space-time path planning to resolve path conflicts dynamically.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6605d22d-3965-4a9f-9451-4141f865de55" width="400" height="300" alt="Spacetime">
  <br>
  <em>Figure 1:  Visualises the node expansion in spacetime for
 the five actions: stay, up, down, left and right.</em>
</p>
 
<p align="center">
  <img src="https://github.com/user-attachments/assets/9fb96ccf-30d4-4845-b9ca-2e9541961830" width="400" height="300" alt="Spacetime">
  <br>
  <em>Figure 2:ng the additional dimension of time. Here, the
 green robot plans first and the </em>
</p>

 https://github.com/user-attachments/assets/7ec8e9e7-9271-4800-803a-4f003a7799cd




## Key Features

- Decentralized path planning system
- Real-time trajectory computation and conflict resolution
- Efficient A* search implementation
- 3D spacetime path planning
- Inter-robot collision avoidance
- Edge clash detection and resolution
- Scalable to multiple robots with O(n) replanning time complexity
- Deadlock situation handling

## Requirements

### Hardware Requirements
- Robots with SLAM sensors
- Microcontroller with sufficient memory to store multiple robot paths
- Wireless communication capability (Bluetooth/Zigbee)

### Software Dependencies
- CoppeliaSim simulation environment
- Python with OOP support

## Implementation Details

### State Space
- Coordinates: (x, y, t) where x,y are cartesian coordinates and t is timestep
- Action Space: stay, up, down, left, right
- Cost Function: Uniform cost of 1 for all actions

### Key Components

1. **Motion Planner Module**
   - Robot class with attributes and functions
   - Search algorithms (A*, BFS, UCS, DFS)
   - Map handling

2. **Robot Controller Module**
   - PID controller parameters
   - Differential drive robot control

### Algorithm Features

- Spacetime path planning
- Dynamic replanning when robots are within threshold distance
- Edge clash detection and resolution
- Priority-based collaborative planning
- Deadlock resolution

## Performance Analysis

The efficiency of the algorithm has been analyzed based on several parameters:

1. **Stay Action Cost**
   - Initial rise in expanded nodes
   - Stabilizes at higher costs

2. **Replanning Threshold Distance**
   - Higher threshold leads to more frequent replanning
   - Linear increase in expanded nodes with threshold distance

3. **Heuristic Comparison**
   - Manhattan distance heuristic performs better than Euclidean
   - More efficient node expansion for 4-way moving robots

## Limitations

- Sequential replanning based on robot order
- Idle waiting time for lower priority robots during replanning
- Planning stops at goal achievement, potentially missing optimal paths for other robots
- Increased time complexity due to additional 'stay' action

## Future Work

- Implementation of parallel replanning
- Integration of kinodynamic constraints
- Optimization of time parameterization
- Enhancement of cost function to include both space and time weights

## Demo

The working simulation can be found at: [MultiRobotMotionPlanning](https://github.com/hruthikvs/MutliRobotMotionPLanning)
https://github.com/user-attachments/assets/7ec8e9e7-9271-4800-803a-4f003a7799cd


## Acknowledgments

This project was developed at the Department of Engineering Design, IIT Madras, with guidance from Bijo Sebastian and Nirav Patel.

## References

1. ProrokLab. (2021). Lecture 9: Multi-robot Path Planning
2. García, E., et al. (2022). An efficient multi-robot path planning solution using A* and coevolutionary algorithms
3. Jiang, Y., et al. (2019). Multi-robot planning with conflicts and synergies
4. Hwang, N. E., et al. (2023). Centralised Mission Planning for Multiple Robots Minimising Total Mission Completion Time


## Contributors

- Hruthik V S
- Sai Kumar Reddy
- Nayani Sri Harsh

Department of Engineering Design, Indian Institute of Technology Madras, Chennai, India
