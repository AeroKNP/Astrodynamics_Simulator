# This is the plotting module which creates the plots of trajectory, mass vs time, radius vs time and velocity vs time

import matplotlib.pyplot as plt
import numpy as np

def plot_rocket(x,y,mass,v,r,t):
    
    fig,ax=plt.subplots(2,2,figsize=(14,16))
    plt.subplots_adjust(hspace=0.5,wspace=0.5)

    ax[0][0].plot(x,y-6.371e6) 
    # ax[0][0].set_aspect('equal')
    ax[0][0].set_xlabel("X Co Ordinate")
    ax[0][0].set_ylabel("Y Co ordinate from surface of earth")
    ax[0][0].grid()

    ax[0][1].plot(t,mass)
    ax[0][1].set_xlabel("Time")
    ax[0][1].set_ylabel("Mass")
    ax[0][1].grid()

    ax[1][0].plot(t,v)
    ax[1][0].set_xlabel("Time")
    ax[1][0].set_ylabel("Velocity")
    ax[1][0].grid()

    ax[1][1].plot(t,r-6.371e6)
    ax[1][1].set_xlabel("Time")
    ax[1][1].set_ylabel("Radius from surface of earth")
    ax[1][1].grid()

    plt.show()

