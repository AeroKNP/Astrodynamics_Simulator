# Importing all the modules
#
import numpy as np
from Core import integrators
from Satelite_Module import system 
from Satelite_Module import plots
import thruster
from controller import controller
from Core import constants as cons

def choose_integrator():
    n=int(input("Choosing the integrator:\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    while n!=1 and n!=2 and n!=3:
        n=int(input("Invalid Input\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    return n

def choose_model():
    n=int(input("Choosing the system:\nPress 1 for Earth only system\nPress 2 for Earth-Moon system\n"))
    while n!=1 and n!=2 :
        n=int(input("Invalid Input\nPress 1 for Earth only system\nPress 2 for Earth-Moon system\n"))
    if n==1:
        return False
    else:
        return True

# region Initialsing Variables
state=np.array([cons.R_earth+4.0e5,0.0,0.0,7670])
prev_states=np.array([cons.R_earth+4.0e5,0.0,0.0,7670,cons.R_earth+4.0e5,0.0,0.0,7670])  # Keeps the data of previous two states
history=[state.copy()]

fire_thruster=False
burn_pending = True # for single burn right now 

# Creating the time array
t=[0]
t_final=7000
dt=0.01

# endregion

# region Choosing the system model and integrator 
use_moon=choose_model()

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
    
    fire_thruster,dvx,dvy=controller(state,t[-1],prev_states,burn_pending)

    # Updating the previous states
    prev_states[4:8]=prev_states[0:4].copy()
    prev_states[0:4]=state.copy()

    # Firing the thrusters
    if fire_thruster:
        state=thruster.burn(state,dvx,dvy)
        burn_pending=False

    # Without thruster propagation
    derivatives = system.derivatives
    state=integrator(state,t[-1],dt,derivatives,
                     [cons.mu_earth,cons.mu_moon,[system.x_moon,system.y_moon],use_moon])

    history.append(state.copy())
    t.append(t[-1]+dt)

# endregion

# region Creating Arrays
history=np.array(history)
x=history[:,0]
y=history[:,1]
vx=history[:,2]
vy=history[:,3]

# endregion

# region Getting the radius, energy and angular momentum of the system 
if use_moon:
    # For both earth moon system
    r_earth=np.sqrt(x**2+y**2)
    r_moon=np.sqrt((x-system.x_moon)**2+(y-system.y_moon)**2)
    E=0.5*(np.array(vx)**2+np.array(vy)**2) - cons.mu_earth/r_earth - cons.mu_moon/r_moon
    L=(np.array(x)*np.array(vy)-np.array(y)*np.array(vx))

else:
    # For only earth system
    r_earth=np.sqrt(np.array(x)**2+np.array(y)**2)
    E=0.5*(np.array(vx)**2+np.array(vy)**2) -cons.mu_earth/r_earth
    L=(np.array(x)*np.array(vy)-np.array(y)*np.array(vx))

# endregion

# Plotting the graphs
plots.plot_orbit(x,y,t,E,L,r_earth,system.x_moon,system.y_moon,use_moon)