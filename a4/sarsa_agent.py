#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

epsilon = 0.1
alpha = 0.5
Q = None
num_total_row = 7 # num_total_rows: integer
num_total_column = 10
#a list of all action
action=["up","down","left","right","upleft","upright","downleft","downright"]

def epsilon_greedy(state,Q):
    
    #rand_in_range(10)>0 means 90% agent goes for greedy choice
    if rand_in_range(10)>0:
       
        #10% agent choose from random
    else:
            
    

def agent_init():
    #initialize the policy array in a smart way
    
    Q = [[[0 for k in range(len(action))] for j in range(num_total_row)] for i in range[num_total_column]]
    

def agent_start(state):
    # pick the first action, pick a action from random
    action_index = rand_in_range(len(action))
    return action[action_index]


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    
    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi

    return

def agent_cleanup():
    """
    This function is not used
    """
    # clean up
    return

def agent_message(in_message): # returns string, in_message: string
    global Q
    """
    Arguments: in_message: string
    returns: The value function as a string.
    This function is complete. You do not need to add code here.
    """
    # should not need to modify this function. Modify at your own risk
    if (in_message == 'ValueFunction'):
        return pickle.dumps(np.max(Q, axis=1), protocol=0)
    else:
        return "I don't know what to return!!"

