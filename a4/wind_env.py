#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Code for the Gambler's problem environment from the Sutton and Barto
  Reinforcement Learning: An Introduction Chapter 4.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta 
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

num_total_row = 7 # num_total_rows: integer
num_total_column = 10
current_state = None
final_state = None
wind = None
def env_init():
    global current_state,final_state,wind
    current_state = np.zeros(2)
    final_state = np.zeros(2)
    wind = np.zeros(num_total_column)
def env_start():
    """ returns numpy array """
    global current_state,wind,final_state
    
    current_state = np.asarray([0,3])
    final_state = np.asarray([7,3])
    wind = np.asarray([0,0,0,1,1,1,2,2,1,0])
    
    return current_state

def env_step(action):
    global current_state, final_state, wind
    change = np.zeros(2)
    if action=="up":
        change[1] += 1
    elif action == "down":
        change[1]-=1
    elif action == "right":
        change[0]+=1
        
    elif action == "left":
        change[0]-= 1  
        
    elif action == "upleft":
        change[0]-= 1  
        change[1] += 1
    elif action == "upright":
        change[0]+= 1  
        change[1] += 1
    elif action == "downleft":
        change[0]-= 1  
        change[1] += 1
    elif action == "downright":
        change[0]+= 1  
        change[1] += 1  
    elif action=="ninth":
        change[1] = change[1]
    else:
        print("unkown action")
        
    #if the it's still in the grid, we update the coordinates; otherwise, we let the point in the old coordinates
    if [0]+change[0] in range(0,num_total_column) and current_state[1]+change[1] in range(0,num_total_row):
        current_state[0] += change[0]
        current_state[1] += change[1]
        
    #add the effect of the wind
    current_state[1]+=wind[current_state[0]]
    
    #check if the wind blow the point out of the grid or not
    if current_state[1] not in range(0,num_total_row):
        current_state[1]-= wind[current_state[0]]
        
    reward = -1
    is_terminal = False
    
    #if get the goal,terminate with reward = 1; otherwise, keep itterating with reward = -1
    if np.array_equal(current_state,final_state):
        is_terminal = True
        current_state = None
        reward = 0

    result = {"reward": reward, "state": current_state, "isTerminal": is_terminal}

    return result

def env_cleanup():
    #
    return

def env_message(in_message): # returns string, in_message: string
    """
    Arguments
    ---------
    inMessage : string
        the message being passed

    Returns
    -------
    string : the response to the message
    """
    
    
    return ""
