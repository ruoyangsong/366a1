#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

action_hist = None
Return = None
Hits = None
policy = None
Q = None

def clearhist():
    #clear the action history after each episode
    global action_hist
    action_hist = [[0 for j in range(1,i+1)] for i in range(1,100)]
    
    
def agent_init():
    #initialize the policy array in a smart way
    global action_hist,policy,Return,Q,Hits
    
    #number of same action performed in one episode!
    action_hist = [[0 for j in range(1,i+1)] for i in range(1,100)]
    
    #Return[state][action] how many reward of this pair in one run!
    Return = [[0 for j in range(1,i+1)] for i in range(1,100)]
    #How many time a (state,action) pair is used
    Hits = [[0 for j in range(1,i+1)] for i in range(1,100)]
    #init policy in each run
    policy = [min(i,100-i) for i in range(1,100)]
    
    #Q[state][action] = 0
    Q = np.zeros((99,99))
    
def agent_start(state):
    # pick the first action, don't forget about exploring starts 
    global action_hist
    
    #choose a random action
    action = rand_in_range(min(state[0],100-state[0]))+1
    action_hist[state[0]-1][action-1] += 1
    
    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    # select an action, based on Q
    global action_hist,Q
    action =  policy[state[0]-1]
    
    action_hist[state[0]-1][action-1] += 1
    
    
    #print "step",last_action,action_hist[last_action[0]-1][last_action[1]-1]
    return action

def agent_end(reward):
    # do learning and update pi
    global action_hist,policy,Return,Q,Hits
    for i in range(99):
        for j in range(i):
            if action_hist[i][j]!=0:
                Return[i][j] +=reward
                Hits[i][j]+=action_hist[i][j]
                Q[i][j] =Return[i][j]/Hits[i][j]
                
                policy[i] = np.argmax(Q[i])+1
    clearhist()
    print policy
                
    #(state,action) = last_action
    #Return[state-1][action-1]+=reward
    #Q[state-1][action-1] = Return[state-1][action-1]/action_hist[state-1][action-1]
    #clearhist()
    #if reward!=0:
        #policy[state-1] = np.argmax(Q[state-1])+1
    
    #print "end",policy
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
    
