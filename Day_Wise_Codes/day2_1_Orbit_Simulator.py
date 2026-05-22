# Simulating the orbit equation using euler equation and doing it manually 
# In Day 2, we'll be adding the E and L of the system
# We'll analyse the behaviour of the system by changing the time steps and duration
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
dt=0.2
t_final = 100

# State update
while t[-1]<t_final:
    state=state+(derivative(t,state))*dt
    history.append(state.copy())
    t.append(t[-1]+dt)

history=np.array(history)
x=history[:,0]
y=history[:,1]

# Getting the radius
# Getting the energy and the angluar momentum equations
r=np.sqrt(np.array(x)**2+np.array(y)**2)
E=0.5*(np.array(x)**2+np.array(y)**2)
L=(np.array(x)**2+np.array(y)**2)

# # Plotting the graphs
fig,ax=plt.subplots(2,2,figsize=(10,12))
plt.subplots_adjust(hspace=0.5,wspace=0.5)

ax[0][0].plot(x,y)
ax[0][0].set_aspect('equal')
ax[0][0].set_xlabel("X Co Ordinate")
ax[0][0].set_ylabel("Y Co ordinate")
ax[0][0].grid()

ax[0][1].plot(t,E)
ax[0][1].set_xlabel("Time")
ax[0][1].set_ylabel("Energy")
ax[0][1].grid()

ax[1][0].plot(t,L)
ax[1][0].set_xlabel("Time")
ax[1][0].set_ylabel("Angular Momentum")
ax[1][0].grid()

ax[1][1].plot(t,r)
ax[1][1].set_xlabel("Time")
ax[1][1].set_ylabel("Radius")
ax[1][1].grid()

plt.show()