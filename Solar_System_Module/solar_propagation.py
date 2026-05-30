# This is the solar propagtion module which is used to run the solar phase of a satellite in some module other than SSM

import numpy as np
import Solar_System_Module.bodies as bd
import Solar_System_Module.system as system

# Creating a function to perform propagation in solar phase
def run_solar_phase(state,tstart,tfinal,integrator):
    
    # Creating the time array
    t=[tstart]
    dt=3600

    # Co ordinate transfrom from earth state to solar system state
    bd.satellite["state"]=state+bd.earth["state"]
    
    # Propagation
    while t[-1]<tfinal:

        # Getting the derivatives
        derivatives=system.derivatives

        # Iterating for every body 
        for body in bd.bodies:
            body["state"]=integrator(body["state"],t[-1],dt,derivatives,[body,bd.bodies])
            body["history"].append(body["state"].copy())
        
        t.append(t[-1]+dt)
    
    # Returning time array and history of satellite phases
    return t,bd.satellite["history"]