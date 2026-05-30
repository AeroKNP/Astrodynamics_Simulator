# This is the plotting module which creates the plots of trajectory, mass vs time, radius vs time and velocity vs time

import matplotlib.pyplot as plt
import numpy as np
from Core import constants as cons

def plot_rocket(ax,x,y,mass,v,r,t):
    
    plt.subplots_adjust(hspace=0.5,wspace=0.5)
    
    ax[0][0].plot(x,y-cons.R_earth) 
    # ax[0][0].set_aspect('equal')
    ax[0][0].set_xlabel("X Co Ordinate in Earth centered frame")
    ax[0][0].set_ylabel("Y Co ordinate from surface of earth")
    ax[0][0].grid()

    ax[0][1].plot(t,mass)
    ax[0][1].set_xlabel("Time")
    ax[0][1].set_ylabel("Mass")
    ax[0][1].grid()

    ax[1][0].plot(t,v)
    ax[1][0].set_xlabel("Time")
    ax[1][0].set_ylabel("Velocity with respect to velocity of earth")
    ax[1][0].grid()

    ax[1][1].plot(t,r-cons.R_earth)
    ax[1][1].set_xlabel("Time")
    ax[1][1].set_ylabel("Radius from surface of earth")
    ax[1][1].grid()


