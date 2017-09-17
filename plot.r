#!/usr/bin/env Rscript

# Author: Matthew Schlegel
# Purpose: Just a simple plotting util to read in data from RL_EXP_OUT.dat

dat1 = read.table("RL_EXP_OUT1.dat")
dat2 = read.table("RL_EXP_OUT2.dat")

plot(x = 1 : length(dat1[, 1]), y = dat1[,1], type = "l", ylab = "% Optimal Action", xlab = "Steps", col = "red")

lines(x = 1 : length(dat2[, 1]), y = dat2[,1], type = "l", ylab = "% Optimal Action", xlab = "Steps", col = "green")




