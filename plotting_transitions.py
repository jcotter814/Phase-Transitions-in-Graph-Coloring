# -*- coding: utf-8 -*-
"""
@author: James Cotter
Here I look at the phase transitions in the fraction of the vertices in the
2-core and 3-core as function of the average degree. In addition I look at 
whether an exact algorithm finds a 3-coloring of an ER graph as a function
of average degree and analyze its performance on different instances.
"""

import erdos_renyi as er
import matplotlib.pyplot as plt
import numpy as np
import time

#%% First, I compute the fraction of vertices in the k-core as a function of c 
#for k = 2 and k = 3. In addition I compute the fraction of instances in which 
#a graph is 3-colorable using the greedy approach

#number of vertices
n = 1000

#c values
vals = 50
c_arr = np.linspace(0,8,vals)

#probabilities
p = c_arr/n

#number of trials
trials = 1
k = 0

#results
colorability = np.zeros(vals)
k2_results = np.zeros(vals)
k3_results = np.zeros(vals)

while k < trials:
    for i,prob in enumerate(p):
        g = er.Erdos_Renyi(n,prob)
        colorability[i] += g.greedy_coloring(3)
        k2_results[i] += g.fraction_in_k_core(2)
        k3_results[i] += (g.fraction_in_k_core(3))
    k+=1

#average over trials
colorability /= trials
k2_results /= trials
k3_results /= trials

#%% Plot results

fig1,(ax1,ax2) = plt.subplots(2,sharex = True)

ax1.plot(c_arr,k2_results,".",label = "k = 2")
ax1.plot(c_arr,k3_results,"*",label = "k = 3")
ax1.set_title("Fraction of Vertices in k-core vs. Average Degree")
ax1.set_xlabel("c")
ax1.set_ylabel("Fraction in k-core")
ax1.legend()

ax2.plot(c_arr,colorability,".")
ax2.set_xlabel("c")
ax2.set_title("Percent 3-Colorable vs. Average Degree, Greedy Algorithm")
ax2.set_ylabel("% 3-Colorable")
fig1.tight_layout()
ax2.legend()

#%% Next, record both the colorabilibilty and time used by an exact algorithm 
#for different c values. Have to use smaller graph instances as this algorithm 
#is exponential in worst case.


#number of vertices
n = 40

#probabilities
c_arr = np.linspace(0,5,vals)
p = c_arr/n

#k-colorability
k = 3

#storing results
exact_results = np.zeros(vals)
times = np.zeros(vals)

r = 0
while r < trials:
    for i,prob in enumerate(p):
        G = er.Erdos_Renyi(n,prob)
        
        #to time
        start = time.time()
        T = G.call_exact(k)
        stop = time.time()
        
        exact_results[i] += T
        times[i] += stop-start
    r+=1

#%%Plot the results of the exact algorithm

fig2,(ax1,ax2) = plt.subplots(2,sharex = True)
ax1.plot(c_arr,exact_results,".")
ax1.set_title("Percent 3-Colorable vs. Average Degree, Exact Algorithm")
ax1.set_xlabel("c")
ax1.set_ylabel("Percent 3-Colorable")

ax2.plot(c_arr,times,"*")
ax2.set_title("Time taken to Color vs. Average Degree, c")
ax2.set_ylabel("Seconds")
fig2.tight_layout()


    
    














