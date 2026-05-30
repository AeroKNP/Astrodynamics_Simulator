import numpy as np
from Core.gravity import gravity

# Default function which will exsist in absence of any external effects
def kinematics(t,state,extra_parameters=None):
    vx=state[2]
    vy=state[3]

    dxdt=vx
    dydt=vy

    return np.array([dxdt,dydt,0.0,0.0])

# Writing the total derivatives function
def derivatives(t,state,extra_parameters):
    
    body,bodies=extra_parameters

    total=kinematics(t,state)

    # Adding the gravitational forces from all other bodies
    for other_body in bodies:
        if other_body!=body:
            total+=gravity(t,state,other_body["mu"],other_body["state"])

    return total


    

    