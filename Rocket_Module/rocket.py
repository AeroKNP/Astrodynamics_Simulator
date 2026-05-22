import numpy as np

dry_mass=5.0
fuel_mass=5.0
total_mass=dry_mass+fuel_mass
T=0.02
mdot=0.005
cd = 0.5
A=0.01


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
