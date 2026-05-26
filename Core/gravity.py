# This is the gravity function for a two body system

import numpy as np

# Creating the gravity function
def gravity(t,state,mu,other_state=None):

    if other_state is None:
        other_state=np.zeros(len(state),dtype=float)
        
    x=state[0]
    y=state[1]

    other_x=other_state[0]
    other_y=other_state[1]
    
    r=np.sqrt((other_x-x)**2+(other_y-y)**2)

    dvxdt=(mu)*(other_x-x)/(r)**3
    dvydt=(mu)*(other_y-y)/(r)**3

    grav_der=np.zeros(len(state),dtype=float)
    grav_der[2]=dvxdt
    grav_der[3]=dvydt

    return grav_der
