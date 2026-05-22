# Simulating the orbit using the solve ivp's RK45 method 
# We'll be testing the adaptive timestep against our fixed timestep method of RK4 
# We'll also add rtol and atol
# 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Initialsing the variables
state0=[1.0,0.0]
tspan=(0,100)

# Generating the derivatives
def derivative(t,state):
    x=state[0]
    y=state[1]

    dxdt=-y
    dydt=x

    return [dxdt,dydt]

# Solving the equations
sol=solve_ivp(derivative,tspan,state0,method="RK45",rtol=1e-8,atol=1e-10)

# Getting the radius, energy and angular momentum of the system
r=np.sqrt(sol.y[0]**2 + sol.y[1]**2)
E=0.5*(sol.y[0]**2 + sol.y[1]**2)
L=(sol.y[0]**2 + sol.y[1]**2)


# Plotting the graphs
fig,ax=plt.subplots(2,2,figsize=(10,12))
plt.subplots_adjust(hspace=0.5,wspace=0.5)

ax[0][0].plot(sol.y[0],sol.y[1])
ax[0][0].set_aspect('equal')
ax[0][0].set_xlabel("X Co Ordinate")
ax[0][0].set_ylabel("Y Co ordinate")
ax[0][0].grid()

ax[0][1].plot(sol.t,E)
ax[0][1].set_xlabel("Time")
ax[0][1].set_ylabel("Energy")
ax[0][1].grid()

ax[1][0].plot(sol.t,L)
ax[1][0].set_xlabel("Time")
ax[1][0].set_ylabel("Angular Momentum")
ax[1][0].grid()

ax[1][1].plot(sol.t,r)
ax[1][1].set_xlabel("Time")
ax[1][1].set_ylabel("Radius")
ax[1][1].grid()

plt.show()


