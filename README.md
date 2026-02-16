# Q-Learning
Team project on a machine learning model. 

# User Instructions

## 1. Requirements
You need to install the following libraries via your terminal:
pip install numpy
pip install matplotlib

## 2. How to Use
* Grid Setup: Upon launching the program, you will be prompted to enter an integer "x" for the Gridworld size (x > 2).
* Obstacles: Next, you will be asked to enter the number of obstacles "y" (y < x - 1).
* Environment Generation: The program creates a random x-by-x square grid with y obstacles, one target, and the agent.
* Monitoring Progress: Every 99 iterations, the agent's progress is visualized. The terminal will display the Total Reward and the epsilon value for each episode.
* Strategy Selection: After 1,000 iterations, you can choose the epsilon (e) factor:
    1. e = 1: Random moves only.
    2. 0 < e < 1: Balance between random exploration and optimal moves.
    3. e = 0: The agent follows the optimal path and the program terminates.

## 3. Output
The final Q-value table is printed. Each row represents a grid cell with 4 values showing the best move for each state.
