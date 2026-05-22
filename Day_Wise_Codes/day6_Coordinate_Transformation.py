# Making the co ordinate rotation using rotation matrix 
# We'll first find the solution to our problem in one co ordinate frame then use the rotation matrix to get solution in other frame
# We'll be using RK4 method for solving

import matplotlib.pyplot as plt
import numpy as np

# Initialsing Variables
state=np.array([1.0,0.0])
history=[state.copy()]

# Creating time array
t=[0]
dt=0.2
t_final=5

# Getting the derivatives
def derivative(t,state):
    x=state[0]
    y=state[1]

    dxdt=-y
    dydt=x

    return np.array([dxdt,dydt])

# Writing the integrator for RK4
def rk4_step(state,t,dt):

    k1=derivative(t,state)
    k2=derivative(t+(dt/2),state+(dt/2)*k1)
    k3=derivative(t+(dt/2),state+(dt/2)*k2)
    k4=derivative(t+(dt),state+(dt)*k3)

    state+=(dt/6)*(k1+2*k2+2*k3+k4)

    return state
    
# Propagation
while t[-1]<t_final:
    state=rk4_step(state,t[-1],dt)
    
    history.append(state.copy())
    t.append(t[-1]+dt)

# Creating the arrays 
history=np.array(history)
pos=np.transpose(history)

# Taking the theta for rotation
theta=int(input("Enter the value of theta in degrees: "))
theta_rad=np.deg2rad(theta)
R=np.array([
    [np.cos(theta_rad), -np.sin(theta_rad)],
    [np.sin(theta_rad),  np.cos(theta_rad)]
])

# Calculating the new pos vector and new co ordinates in the rotated co ordinate system
new_pos= R@pos
x=new_pos[0,:]
y=new_pos[1,:]

# Getting the radius, energy and angular momentum of the system
r=np.sqrt(np.array(x)**2+np.array(y)**2)
E=0.5*(np.array(x)**2+np.array(y)**2)
L=(np.array(x)**2+np.array(y)**2)

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
