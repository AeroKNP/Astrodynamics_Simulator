import numpy as np

dry_mass=20000
fuel_mass=80000
total_mass=dry_mass+fuel_mass
T=1.8e6
mdot=600
cd = 0.3
A=10


def thruster(t,state,extra_parameters):
    x,y,vx,vy,mass=state
    v=np.sqrt(vx**2+vy**2)

    mdot,T = extra_parameters

    dxdt=vx
    dydt=vy

    dvxdt=(T/mass)*(vx/v)
    dvydt=(T/mass)*(vy/v)

    dmdt=-mdot

    return np.array([0,0,dvxdt,dvydt,dmdt])
