
import numpy as np
from Rocket_Module import rocket as rk

rho_surface=1.225
R_Earth=6.371e6
H=8500

def calc_density(state):
    x=state[0]
    y=state[1]

    r=np.sqrt(x**2+y**2)
    h=r-R_Earth
    if r>(R_Earth+5*H):
        rho=0.0
    else:
        rho=rho_surface*(np.exp(-h/H))

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
