# We'll be creating the solar system module, however we have not developed a very efficient way as we have to store
# data spearately for each body

import numpy as np
from bodies import bodies
from Solar_System_Module import system
from Core import integrators
from Solar_System_Module import plots

def choose_integrator():
    n=int(input("Choosing the integrator:\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    while n!=1 and n!=2 and n!=3:
        n=int(input("Invalid Input\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    return n

# region Initialsing all the variables
sun_history=[bodies[0]["state"].copy()]
earth_history=[bodies[1]["state"].copy()]
mars_history=[bodies[2]["state"].copy()]
jupiter_history=[bodies[3]["state"].copy()]
satellite_history=[bodies[4]["state"].copy()]

# Creating time arrays
t=[0.0]
dt=3600
t_final=3.743e8

# endregion

# region Choosing the integrator
choice = choose_integrator()
if choice == 1:
    integrator = integrators.euler_step

elif choice == 2:
    integrator = integrators.rk4_step

else:
    integrator = integrators.leapfrog_step

# endregion

# region Propagation
while t[-1]<t_final:

    derivatives=system.derivatives

    # Iterating for every body in bodies list
    for body in bodies:
        body["state"]=integrator(body["state"],t[-1],dt,derivatives,[body,bodies])
        
        # All states do not update simultaneously ie Mars uses the updated state of Earth to get its derivatives
        # Although the error due to this is very small, but we'll try to fix this in upcoming updates
        
    sun_history.append(bodies[0]["state"].copy())
    earth_history.append(bodies[1]["state"].copy())
    mars_history.append(bodies[2]["state"].copy()) 
    jupiter_history.append(bodies[3]["state"].copy())
    satellite_history.append(bodies[4]["state"].copy())
    t.append(t[-1]+dt)

# endregion

# region Creating the arrays
sun_history=np.array(sun_history)
earth_history=np.array(earth_history)
mars_history=np.array(mars_history)
jupiter_history=np.array(jupiter_history)
satellite_history=np.array(satellite_history)

xsun=sun_history[:,0]
ysun=sun_history[:,1]
xearth=earth_history[:,0]
yearth=earth_history[:,1]
xmars=mars_history[:,0]
ymars=mars_history[:,1]
xjupiter=jupiter_history[:,0]
yjuptier=jupiter_history[:,1]
xsatellite=satellite_history[:,0]
ysatellite=satellite_history[:,1]

# endregion

# Plotting
plots.plotting([xsun,ysun],[xearth,yearth],[xmars,ymars],[xjupiter,yjuptier],[xsatellite,ysatellite])