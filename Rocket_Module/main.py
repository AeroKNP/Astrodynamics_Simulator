# Making a rocket module containing variable mass and varying direction thrust
# Although it has a PID Controller but since we dont have any disturbances yet it is of no use

import numpy as np
import rocket as rk
from Rocket_Module import system
from Core import integrators
from Rocket_Module import plots
import guidance
from Core import constants as cons

def check_mission_phase(t_turn,t,state,dry_mass):
    mass=state[4]
    
    if t<t_turn:
        mission_phase="rise" # Corresponds to vertical rise
    elif mass>dry_mass:
        mission_phase="turn" # Corresponds to thrusters still firing and doing a gravity turn 
    else:
        mission_phase="coasting" # Corresponds to thrusters swtiched off
    
    return mission_phase

def choose_integrator():
    n=int(input("Choosing the integrator:\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    while n!=1 and n!=2 and n!=3:
        n=int(input("Invalid Input\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    return n

# region Initiasling the variables
state=np.array([0.0,cons.R_earth,0.0,0.0,rk.total_mass])
history=[state.copy()]

# Creating time parameters
t=[0]
dt=0.01
t_final=3000

mission_phase=0

# For PID Controller
theta_actual=90.0
prev_error=0.0
integrated=0.0

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

    mission_phase=check_mission_phase(guidance.t_turn,t[-1],state,rk.dry_mass)

    # Getting the derivatives from system
    derivatives=system.derivatives

    # Getting the desried theta value from guidance to pass it to PID then to thruster
    theta_des=guidance.calc_theta_desried(t[-1],mission_phase)
    theta_dot,prev_error,integrated=guidance.PID(theta_actual,theta_des,prev_error,integrated,dt)
    theta_actual+=theta_dot*dt
    
    # Updating the state
    state=integrator(state,t[-1],dt,derivatives,[rk.mdot,rk.T,mission_phase,theta_actual,cons.mu_earth])
    
    # If it strikes earth then simulation stops
    if (np.sqrt(state[0]**2+state[1]**2)-cons.R_earth)<0:
        break
    
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
