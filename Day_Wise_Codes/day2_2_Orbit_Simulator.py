# Simulating the orbit equation using euler equation and doing it manually 
# In Day 2, we'll be analysisng the error in the system at different timesteps
# 
#  
import numpy as np
import matplotlib.pyplot as plt

# Initiallsing the variables 
state=np.array([1.0,0.0])
history=[state.copy()]

# Getting the derivatives
def derivative(t,state):
    x=state[0]
    y=state[1]

    dxdt=-y
    dydt=x

    return np.array([dxdt,dydt])

# Creating the time array
t=[0.0]
timestep=np.array([0.001,0.005,0.01,0.05,0.1,0.2,0.5])
t_final = 100

# Array of final radius and energy in for each timestep
r_error=[]
E_error=[]

# For each and every timestep
for dt in timestep:
    # State update
    while t[-1]<t_final:
        state=state+(derivative(t[-1],state))*dt
        history.append(state.copy())
        t.append(t[-1]+dt)

    # Calculating the errors in radius and energy
    rfinal=np.sqrt(state[0]**2 + state[1]**2)
    Efinal=0.5*(state[0]**2 + state[1]**2)
    r_error.append(np.abs(rfinal-1))
    E_error.append(np.abs(Efinal-0.5))

    # Re-initialising the conditions for the next loop
    state=np.array([1.0,0.0])
    history=[state.copy()]
    t=[0.0]



# Plotting the graphs
fig,ax=plt.subplots(1,2,figsize=(10,12))
plt.subplots_adjust(hspace=0.5,wspace=0.5)

ax[0].plot(timestep,r_error)
ax[0].set_xscale("log")
ax[0].set_yscale("log")
ax[0].set_xlabel("Value of dt")
ax[0].set_ylabel("Error in final Radius")
ax[0].grid()

ax[1].plot(timestep,E_error)
ax[1].set_xscale("log")
ax[1].set_yscale("log")
ax[1].set_xlabel("Value of dt")
ax[1].set_ylabel("Error in final Energy")
ax[1].grid()

plt.show()
