# This is the gravity function for a two body system

import numpy as np

# Creating the gravity function
def gravity(t,state,mu,other_state):

    x,y,vx,vy=state
    other_x,other_y,other_vx,other_vy=other_state
    
    r=np.sqrt((other_x-x)**2+(other_y-y)**2)

    dvxdt=(mu)*(other_x-x)/(r)**3
    dvydt=(mu)*(other_y-y)/(r)**3

    return np.array([0.0,0.0,dvxdt,dvydt])
