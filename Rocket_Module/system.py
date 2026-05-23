# This is the systems module which combines all derivatives from modules and decides what currently the system is

from gravity import gravity
import rocket as rk
import numpy as np
from Environment_Module.environment import drag

# Default function which will exsist in absence of any external effects
def kinematics(t,state,extra_parameters=None):
    x,y,vx,vy,mass=state

    dxdt=vx
    dydt=vy

    return np.array([dxdt,dydt,0,0,0])

# The total derivatives function
def derivatives(t,state,extra_parameters):
    mdot,T,mission_phase,theta=extra_parameters

    # Getting the total derivatives 
    total=kinematics(t,state)+gravity(t,state)+drag(t,state)

    if mission_phase=="rise" or mission_phase=="turn": # Thrusters are activated
        total+=rk.thruster(t,state,[mdot,T,theta])
    
    return total

