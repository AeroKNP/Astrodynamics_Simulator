# We'll be creating the solar system module, however our way of updating the state variable is not so efficient

import numpy as np
import matplotlib.pyplot as plt
from Core import integrators
from Solar_System_Module.bodies import bodies
from Solar_System_Module import system
from Solar_System_Module import plots

def choose_integrator():
    n=int(input("Choosing the integrator:\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    while n!=1 and n!=2 and n!=3:
        n=int(input("Invalid Input\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    return n

# History of all bodies is stored inside the dictnoary itself
# region Creating time arrays
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

    # Getting the derivatives
    derivatives=system.derivatives

    # Iterating for every body in bodies list
    for body in bodies:
        body["state"]=integrator(body["state"],t[-1],dt,derivatives,[body,bodies])
        body["history"].append(body["state"].copy())
        # All states do not update simultaneously ie Mars uses the updated state of Earth to get its derivatives
        # Although the error due to this is very small, but we'll try to fix this in upcoming updates
        
    t.append(t[-1]+dt)

# endregion

# Creating the arrays
for body in bodies:
    body["history"]=np.array(body["history"])

# Plotting
fig,ax=plt.subplots()
plots.plotting(ax,bodies[0]["history"],bodies[1]["history"],bodies[2]["history"],bodies[3]["history"],bodies[4]["history"])
plt.show()