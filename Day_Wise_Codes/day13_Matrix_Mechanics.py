# In day 7, we'll be creating an integrator engine which has all Euler, RK4 and Leapfrog integrators in it
# We'll be simulating orbital motion 
# 
# 
import matplotlib.pyplot as plt
import numpy as np

# Initialsing Variables
state=np.array([1.0,0.0,0.0,1.0])
history=[state.copy()]

A=np.array([
    [0,0,1,0],
    [0,0,0,1],
    [-1,0,0,0],
    [0,-1,0,0]
])


# Creating time array
t=[0]
dt=0.01
t_final=100

# Getting the derivatives
def derivatives(t,state):
    
    dstate=A@state

    return dstate

# Writing the integrator for Euler
def euler_step(state,t,dt):
    
    state = state + derivatives(t,state)*dt

    return state

# Writing the integrator for RK4
def rk4_step(state,t,dt):

    k1=derivatives(t,state)
    k2=derivatives(t+(dt/2),state+(dt/2)*k1)
    k3=derivatives(t+(dt/2),state+(dt/2)*k2)
    k4=derivatives(t+(dt),state+(dt)*k3)

    state = state + (dt/6)*(k1+2*k2+2*k3+k4)

    return state

# Writing the integrator for Leapfrog
def leapfrog_step(state,t,dt):
    
    # For half velcoity update
    dstate=derivatives(t,state)
    state[2:4]=state[2:4]+dstate[2:4]*(dt/2)

    # For full position update
    dstate=derivatives(t,state)
    state[0:2]=state[0:2]+dstate[0:2]*dt

    # For remaining half velocity update
    dstate=derivatives(t,state)
    state[2:4]=state[2:4]+dstate[2:4]*(dt/2)

    return state

# Choosing the integrator
def choose_integrator():
    n=int(input("Press 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    while n!=1 and n!=2 and n!=3:
        n=int(input("Press 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    return n

integrator=choose_integrator()

# Propagation
while t[-1]<t_final:
    if integrator==1:
        state=euler_step(state,t[-1],dt)
    elif integrator==2:
        state=rk4_step(state,t[-1],dt)
    else:
        state=leapfrog_step(state,t[-1],dt)

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
earth = plt.Circle((0,0), 8e-2, fill=True)
ax[0][0].add_patch(earth)
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

