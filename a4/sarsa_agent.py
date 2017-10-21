#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle
import random

epsilon = 0.1
alpha = 0.5
Q = None
last_state=None
last_action = None
num_total_row = 7 # num_total_rows: integer
num_total_column = 10
#a list of all action
action=["up","down","left","right","upleft","upright","downleft","downright","ninth"]

def choose_random_largest(Q):
    old_Q = Q
    Q = sorted(Q,reverse = True)
    choices = []
    for i in range(len(Q)):
        if old_Q[i]==Q[0]:
            choices.append(i)
    #randomly choose from largest estimate actions
    return random.choice(choices)

def epsilon_greedy(state1,Q1):
    global action
    #rand_in_range(10)>0 means 90% agent goes for greedy choice
    if rand_in_range(10)>0:
        #find the action with the largest estimated Q value
        action_index = choose_random_largest(Q1[state1[0]][state1[1]])
    else:
        #10% agent choose from random
        
        action_index= rand_in_range(len(action))
        
    return action_index
    

def agent_init():
    #initialize the policy array in a smart way
    global Q,last_state,last_action,action
    
    #Q = np.zeros((num_total_column,num_total_row,len(action)))
    Q = [[[0 for k in range(len(action)) ] for j in range(num_total_row)] for i in range(num_total_column)]
    last_state = [0,0]
    last_action= 0

def agent_start(state):
    # pick the first action, pick a action from random
    global action,last_state,last_action
    
    action_index = rand_in_range(len(action))
    
    #update last_state, try to use last_state=state, but there is a bug of it.
    last_state[0] = state[0]
    last_state[1] = state[1]
    last_action = action_index
    #print "start_state is %d %d:"%(last_state[0],last_state[1])
    #print "action is %d %s: "%(action_index,action[action_index]) 
    return action[action_index]


def agent_step(reward, state): 
    # select an action, based on Q
    global Q,action,last_state,last_action
    action_index = epsilon_greedy(state,Q)
    Q[last_state[0]][last_state[1]][last_action]+=alpha*(reward+int(Q[state[0]][state[1]][action_index])-int(Q[last_state[0]][last_state[1]][last_action]))
    
    #print "last_state is %d %d:"%(last_state[0],last_state[1])
    #print Q[last_state[0]][last_state[1]]
    #print "action is %d %s: "%(action_index,action[action_index]) 
    
    last_action = action_index
    last_state[0] = state[0]
    last_state[1] = state[1]
    #print "current state is %d %d:"%(last_state[0],last_state[1])
    return action[action_index]    
     
    
def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """

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

