# Simulating the orbit integrator using both euler and rk4 method
# 
# 
import matplotlib.pyplot as plt
import numpy as np

# Initialsing Variables
state=np.array([1.0,0.0])
history=[state.copy()]

# Creating time array
t=[0]
dt=0.01
t_final=100

# Getting the derivatives
def derivative(t,state):
    x=state[0]
    y=state[1]

    dxdt=-y
    dydt=x

    return np.array([dxdt,dydt])

# Writing the integrator for Euler
def euler_step(state,t,dt):

    state=state+derivative(t,state)*dt

    return state

# Writing the integrator for RK4
def rk4_step(state,t,dt):

    k1=derivative(t,state)
    k2=derivative(t+(dt/2),state+(dt/2)*k1)
    k3=derivative(t+(dt/2),state+(dt/2)*k2)
    k4=derivative(t+(dt),state+(dt)*k3)

    state+=(dt/6)*(k1+2*k2+2*k3+k4)

    return state

# Deciding which integrator to use
n=int(input("Press 1 for Euler\nPress 2 for RK4\n"))
while n!=1 and n!=2:
    print("Invalid input")
    n=int(input("Press 1 for Euler\nPress 2 for RK4\n"))
    
# Propagation
while t[-1]<t_final:
    if n==1:
        state=euler_step(state,t[-1],dt)
    else:
        state=rk4_step(state,t[-1],dt)
    
    history.append(state.copy())
    t.append(t[-1]+dt)

# Creating the arrays 
history=np.array(history)
x=history[:,0]
y=history[:,1]

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
