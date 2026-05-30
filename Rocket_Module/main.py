# This is the main module for the simulation
# The rocket parameters are fixed in the rocket.py file and it starts from surface of earth
# It then uses Solar System Module files to simulate the motion in solar system

import numpy as np
import matplotlib.pyplot as plt
import rocket as rk
from Core import constants as cons
from Core import integrators
from Core import telemetry as tel
from Rocket_Module import system
from Rocket_Module import plots
from Rocket_Module import guidance
from Solar_System_Module.solar_propagation import run_solar_phase
from Solar_System_Module.plots import plotting
from Solar_System_Module.bodies import bodies

# Checking for the current mission phase and logging events 
def check_mission_phase(t,state,prev_mission_phase):
    r=np.sqrt(state[0]**2+state[1]**2)
    mass=state[4]
    
    if t<guidance.t_turn:
        mission_phase="rise" # Corresponds to vertical rise
    elif mass>rk.dry_mass:
        if prev_mission_phase!="turn":   # Logging the start of gravity turn
            tel.log_event(t,"End of vertical rise | Gravity turn initiated")
        mission_phase="turn" # Corresponds to thrusters still firing and doing a gravity turn
    elif r>cons.rsoi_earth:
        if prev_mission_phase!="handoff":   # Logging the SOI exit 
            tel.log_event(t,"SOI Exit | Handing off to solar system")
        mission_phase="handoff" # Handoff to solar system module 
    else:
        if prev_mission_phase!="coasting":  # Logging the start of coasting
            tel.log_event(t,"End of gravity turn | Coasting phase entered")
        mission_phase="coasting" # Corresponds to thrusters swtiched off and inside earth's soi
    
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
dt=0.1
t_final=5e7

# Mission and rocket phases
mission_phase=0
prev_mission_phase=mission_phase
rocket_phase="uncrashed"

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

# Logging the launch
tel.log_event(t[-1],"Liftoff") 

# region Propagation in Earth
while t[-1]<t_final:

    # Checking the mission phase
    prev_mission_phase=mission_phase
    mission_phase=check_mission_phase(t[-1],state,prev_mission_phase)

    # Handing off to solar system module 
    if mission_phase=="handoff":
        break

    # Getting the desried theta value from guidance to pass it to PID then to thruster
    theta_des=guidance.calc_theta_desried(t[-1],mission_phase)
    theta_dot,prev_error,integrated=guidance.PID(theta_actual,theta_des,prev_error,integrated,dt)
    theta_actual+=theta_dot*dt

    # Getting the derivatives from system
    derivatives=system.derivatives

    # Updating the state
    state=integrator(state,t[-1],dt,derivatives,[rk.mdot,rk.T,mission_phase,theta_actual,cons.mu_earth])
    
    # If it strikes earth then simulation stops
    if (np.sqrt(state[0]**2+state[1]**2)-cons.R_earth)<0:
        tel.log_event(t[-1],"Rocket Crashed")   # Logging the crash of rocket
        rocket_phase="crashed"  # Setting rocket state as crashed
        break

    history.append(state.copy())
    t.append(t[-1]+dt)
    
# endregion

# region Solar Phase
if rocket_phase!="crashed": # Phase runs only if rocket is not crashed
    
    # Initialsing for solar system module
    solar_state=state[:4]
    tleft=t_final-t[-1]
    thandoff=t[-1]

    # Running the solar phase
    tsolar,solar_history=run_solar_phase(solar_state,thandoff,tleft,integrator)
    tel.log_event(tsolar[-1],"Solar Phase ended successfully")   # Logging the end of solar phase 

else:   # Handling the crashed case
    tsolar=None
    solar_history=None
# endregion

# Logging all the states data
history=np.array(history)
if rocket_phase!="crashed": 
    solar_history=np.array(solar_history)
tel.log_state(t,history,tsolar,solar_history)

# region Creating the arrays for earth phase
x=history[:,0]
y=history[:,1]
vx=history[:,2]
vy=history[:,3]
mass=history[:,4]
r=np.sqrt(x**2+y**2)
v=np.sqrt(vx**2+vy**2)

# endregion

# Creating arrays for solar phase
if rocket_phase!="crashed":
    for body in bodies:
        body["history"]=np.array(body["history"])

# region Plotting the graphs

# Graphs for earth phase
fig_earth,ax_earth=plt.subplots(2,2,figsize=(14,12))
fig_earth.suptitle("Earth Phase")
plots.plot_rocket(ax_earth,x,y,mass,v,r,t)

# Graphs for solar phase
if rocket_phase!="crashed":
    fig_solar,ax_solar=plt.subplots(figsize=(12,8))
    fig_solar.suptitle("Solar Phase")
    plotting(ax_solar,bodies[0]["history"],bodies[1]["history"],bodies[2]["history"],bodies[3]["history"],bodies[4]["history"])

plt.show()

# endregion