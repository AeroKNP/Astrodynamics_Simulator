# This is the systems module which combines all derivatives from modules and decides what currently the system is

import numpy as np
from Core.gravity import gravity
from Environment_Module.environment import drag
import rocket as rk

# Default function which will exsist in absence of any external effects
def kinematics(t,state,extra_parameters=None):
    vx=state[2]
    vy=state[3]

    dxdt=vx
    dydt=vy

    return np.array([dxdt,dydt,0,0,0])

# The total derivatives function
def derivatives(t,state,extra_parameters):
    mdot,T,mission_phase,theta_actual,mu_earth=extra_parameters

    # Getting the total derivatives 
    total=kinematics(t,state)+gravity(t,state,mu_earth)+drag(t,state)

    if mission_phase=="rise" or mission_phase=="turn": # Thrusters are activated
        total+=rk.thruster(t,state,[mdot,T,theta_actual])
    
    return total

