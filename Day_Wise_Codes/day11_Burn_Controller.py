# In day 11, we'll be using our orbit simulator and adding a controller module into it 
# Aim is to let the controller decide when and by how much should we fire the thrusters
# 
# 
import matplotlib.pyplot as plt
import numpy as np


# region Initialsing Variables
state=np.array([1.0,0.0,0.0,1.1])
prev_states=np.array([1.0,0.0,0.0,1.1,1.0,0.0,0.0,1.1])  # Keeps the data of previous two states
history=[state.copy()]
mu=1
fire_thruster=False
burn_pending = True # for single burn right now 

# endregion

# region Creating time array
t=[0]
dt=0.01
t_final=314.16

# endregion

# Getting the derivatives
def derivatives(t,state):
    x=state[0]
    y=state[1]
    vx=state[2]
    vy=state[3]

    r=np.sqrt(x**2+y**2)

    dxdt=vx
    dydt=vy

    dvxdt=-mu*x/(r**3)
    dvydt=-mu*y/(r**3)

    return np.array([dxdt,dydt,dvxdt,dvydt])

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
    n=int(input("Choosing the integrator:\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    while n!=1 and n!=2 and n!=3:
        n=int(input("Invalid Input\nPress 1 for Euler\nPress 2 for RK4\nPress 3 for Leapfrog\n"))
    return n

# Firing the thruster
def burn(state,deltavx,deltavy):
    state[2]=state[2]+deltavx
    state[3]=state[3]+deltavy
    return state

# Making the controller
def controller(state,t,prev_states,burn_pending):
    xn=state[0]
    yn=state[1]
    rn=np.sqrt(xn**2+yn**2)

    xn_1=prev_states[0]
    yn_1=prev_states[1]
    rn_1=np.sqrt(xn_1**2+yn_1**2)

    xn_2=prev_states[4]
    yn_2=prev_states[5]
    rn_2=np.sqrt(xn_2**2+yn_2**2)

    if rn>1.4 and burn_pending==True:
        fire=True
    else:
        fire=False
    
    # burn values temporarily coded in the controller
    dvx=0.0
    dvy=0.25

    return fire,dvx,dvy



# region Choosing the integrator 
integrator=choose_integrator() 

# endregion

# region Propagation
while t[-1]<t_final:
    
    fire_thruster,dvx,dvy=controller(state,t[-1],prev_states,burn_pending)

    # Updating the previous states
    prev_states[4:8]=prev_states[0:4].copy()
    prev_states[0:4]=state.copy()

    if fire_thruster:
        state=burn(state,dvx,dvy)
        burn_pending=False

    # Without thruster propagation
    if integrator==1:
        state=euler_step(state,t[-1],dt)
    elif integrator==2:
        state=rk4_step(state,t[-1],dt)
    else:
        state=leapfrog_step(state,t[-1],dt)

    history.append(state.copy())
    t.append(t[-1]+dt)

# endregion

# region Creating the arrays 
history=np.array(history)
x=history[:,0]
y=history[:,1]
vx=history[:,2]
vy=history[:,3]

# endregion

# region Getting the radius, energy and angular momentum of the system 
r=np.sqrt(np.array(x)**2+np.array(y)**2)
E=0.5*(np.array(vx)**2+np.array(vy)**2) -mu/r
L=(np.array(x)*np.array(vy)-np.array(y)*np.array(vx))

# endregion

# region Plotting the graphs
fig,ax=plt.subplots(2,2,figsize=(14,16))
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

# endregion
