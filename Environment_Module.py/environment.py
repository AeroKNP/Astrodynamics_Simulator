import numpy as np

rho_surface=1.0
R_Earth=1.0
H=0.1

def calc_density(state):
    x=state[0]
    y=state[1]

    r=np.sqrt(x**2+y**2)
    h=r-R_Earth

    rho=rho_surface*(np.exp(-h/H))

    return rho

