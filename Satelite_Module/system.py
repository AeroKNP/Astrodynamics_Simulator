import numpy as np
from Core.gravity import gravity

x_moon,y_moon=[3.844e8,0]

# Default function which will exsist in absence of any external effects
def kinematics(t,state,extra_parameters=None):
    x,y,vx,vy=state

    dxdt=vx
    dydt=vy

    return np.array([dxdt,dydt,0.0,0.0])

# Writing the total derivatives function
def derivatives(t,state,extra_parameters):
    
    mu_earth,mu_moon,moon_state,use_moon=extra_parameters

    total=kinematics(t,state)

    # Adding earth's gravity
    total+=gravity(t,state,mu_earth)
    
    # Adding moon's gravity
    if use_moon:
        total+=gravity(t,state,mu_moon,moon_state)

    return total

