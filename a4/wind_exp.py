#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlon agent using RL_glue. 
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""

from rl_glue import *  # Required for RL-Glue
RLGlue("wind_env", "sarsa_agent")
import matplotlib.pyplot as plt

if __name__ == "__main__":
    max_episodes = 10000
    max_steps = 8000
    step=0
    episode = 0
    step_list=[]
    episode_list=[]
    RL_init()
    while step<max_steps:
        RL_episode(max_episodes)
        step+=RL_num_steps()
        episode = RL_num_episodes()
        step_list.append(step)
        episode_list.append(episode)
        
    plt.plot(step_list,episode_list)
    plt.xlim([0,8000])
    plt.xticks([0,1000,2000,3000,4000,5000,6000,7000])
    plt.xlabel('Time steps')
    plt.ylabel('Episodes')
    plt.legend()
    plt.show()   
    
        
    
   
      
      
      
   