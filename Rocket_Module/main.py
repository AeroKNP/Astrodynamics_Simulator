# Making a rocket module containing variable mass and varying direction thrust

import numpy as np
import rocket as rk
import system
import integrators
import plots
import guidance

def check_mission_phase(state,dry_mass):
    mass=state[4]
    
    if mass>dry_mass:
        mission_phase=0 # Corresponds to thrusters still firing 
    else:
        mission_phase=1 # Corresponds to thrusters swtiched off
    
    return mission_phase

def choose_integrator():
    n=int(input("Choosing the integrator:\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    while n!=1 and n!=2 and n!=3:
        n=int(input("Invalid Input\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    return n

# region Initiasling the variables
state=np.array([0.0,6.371e6,0.0,0.0,rk.total_mass])
history=[state.copy()]

t=[0]
dt=0.01
t_final=1500
mission_phase=0

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

# Propagation
while t[-1]<t_final:
    mission_phase=check_mission_phase(state,rk.dry_mass)

    # Getting the derivatives from system
    derivatives=system.derivatives

    # Getting the theta value from guidance to pass it to thruster
    theta=guidance.calc_theta(t[-1])

    # Updating the state
    state=integrator(state,t[-1],dt,derivatives,[rk.mdot,rk.T,mission_phase,theta])

    history.append(state.copy())
    t.append(t[-1]+dt)
    
# endregion

# region Creating the arrays
history=np.array(history)
x=history[:,0]
y=history[:,1]
vx=history[:,2]
vy=history[:,3]
mass=history[:,4]
r=np.sqrt(x**2+y**2)
v=np.sqrt(vx**2+vy**2)

# endregion

# Plotting the graphs
plots.plot_rocket(x,y,mass,v,r,t)
