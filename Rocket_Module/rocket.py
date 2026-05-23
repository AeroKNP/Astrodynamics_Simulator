# This is the rocket module storing data about the rocket

import numpy as np

dry_mass=20000
fuel_mass=80000
total_mass=dry_mass+fuel_mass
T=1.8e6
mdot=600
cd = 0.3
A=10

# This is the function simulating the firing of thrusters
def thruster(t,state,extra_parameters):
    x,y,vx,vy,mass=state
    v=np.sqrt(vx**2+vy**2)

    mdot,T,theta= extra_parameters
    theta=np.deg2rad(theta)
    
    dxdt=vx
    dydt=vy

    dvxdt=(T/mass)*np.cos(theta)
    dvydt=(T/mass)*np.sin(theta)

    dmdt=-mdot

    return np.array([0,0,dvxdt,dvydt,dmdt])
