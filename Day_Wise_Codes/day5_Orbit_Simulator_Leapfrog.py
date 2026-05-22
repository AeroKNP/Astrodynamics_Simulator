# Simulating the orbit using leapfrog method manually
# In Day 5, we'll be using the leapfrog step methods to simulate the orbit 
# 
# 
import numpy as np
import matplotlib.pyplot as plt

# Initializing the state variables
state=np.array([1.0,0.0,0.0,1.0])
history=[state.copy()]

# Setting the time 
t=[0.0]
t_final=1000
dt=0.2

# Getting the derivatives
def derivatives(t,state):
    x=state[0]
    y=state[1]
    vx=state[2]
    vy=state[3]

    dxdt=vx
    dydt=vy

    dvxdt=-x
    dvydt=-y

    return np.array([dxdt,dydt,dvxdt,dvydt])

# Propagation for leapfrog
while t[-1]<t_final:
    
    # For half velcoity update
    dstate=derivatives(t[-1],state)
    state[2:4]=state[2:4]+dstate[2:4]*(dt/2)

    # For full position update
    dstate=derivatives(t[-1],state)
    state[0:2]=state[0:2]+dstate[0:2]*dt

    # For remaining half velocity update
    dstate=derivatives(t[-1],state)
    state[2:4]=state[2:4]+dstate[2:4]*(dt/2)

    history.append(state.copy())
    t.append(t[-1]+dt)

# Creating the arrays 
history=np.array(history)
x=history[:,0]
y=history[:,1]
vx=history[:,2]
vy=history[:,3]

# Getting the radius, energy and angular momentum of the system
r=np.sqrt(np.array(x)**2+np.array(y)**2)
E=0.5*(np.array(x)**2+np.array(y)**2) + 0.5*(np.array(vx)**2+np.array(vy)**2)
L=(np.array(x)*np.array(vy)-np.array(y)*np.array(vx))

# Plotting the graphs
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

