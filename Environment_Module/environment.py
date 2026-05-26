
import numpy as np
from Rocket_Module import rocket as rk
from Core import constants as cons

H=8500

def calc_density(state):
    x=state[0]
    y=state[1]

    r=np.sqrt(x**2+y**2)
    h=r-cons.R_earth
    if r>(cons.R_earth+5*H):
        rho=0.0
    else:
        rho=cons.rho_surface*(np.exp(-h/H))

    return rho

def drag(t,state,extra_parameters=None):
    x,y,vx,vy,mass=state
    v=np.sqrt(vx**2+vy**2)

    fd=0.5*calc_density(state)*(rk.cd)*(rk.A)*(v**2)

    if v==0:
        dvxdt=0
        dvydt=0
    else:
        dvxdt=-(fd/mass)*(vx/v)
        dvydt=-(fd/mass)*(vy/v)

    return np.array([0,0,dvxdt,dvydt,0])
