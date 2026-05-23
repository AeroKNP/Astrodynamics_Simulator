# This is the gravity module which contains the effects of gravity

import numpy as np

mu_earth=3.986e14

# Creating the gravity fucntion 
def gravity(t,state,extra_parameters=None):
    x,y,vx,vy,mass=state

    r=np.sqrt(x**2+y**2)

    dxdt=vx
    dydt=vy

    dvxdt=-mu_earth*x/(r**3)
    dvydt=-mu_earth*y/(r**3)

    return np.array([0,0,dvxdt,dvydt,0])
