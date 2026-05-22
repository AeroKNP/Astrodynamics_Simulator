from gravity import gravity
import rocket as rk
import numpy as np

def kinematics(t,state,extra_parameters=None):
    x,y,vx,vy,mass=state

    dxdt=vx
    dydt=vy

    return np.array([dxdt,dydt,0,0,0])

def derivatives(t,state,extra_parameters):
    mdot,T,mission_phase=extra_parameters

    total=kinematics(t,state)+gravity(t,state)

    if mission_phase==0: # Thrusters are activated
        total+=rk.thruster(t,state,[mdot,T])
    
    return total

