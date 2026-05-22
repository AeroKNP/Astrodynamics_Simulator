# In day 9, we'll be using our orbit simulator and adding a thruster module into it 
# We can vary when, how much, and in which direction we are firing the thruster
# 
# 
import matplotlib.pyplot as plt
import numpy as np

# Initialsing Variables
state=np.array([1.0,0.0,0.0,1.01])
history=[state.copy()]
mu=1
fire_thruster=False


# Creating time array
t=[0]
dt=0.01
t_final=300

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

# Classifying the orbit
def orbit_classifier(E,r):

    if np.abs(np.mean(E))<1e-3:
        orbit_type="Escape Threshold Orbit"
    elif np.mean(E)<0:
        orbit_type="Bound Orbit"
    else:
        orbit_type="Unbound Orbit"

    print(f"\nOrbit Type: {orbit_type}")

    # Finding the shape of the orbit 
    if orbit_type=="Bound Orbit":
        
        if np.abs(np.max(r)-np.min(r))<0.05:
            orbit_shape="Circular"
        else:
            orbit_shape="Elliptical"
        print(f"Orbit Shape: {orbit_shape}")

    return 

# Checking if we are firing the thruster and getting the dv after thruster
def if_thruster_fire():
    fire=int(input("\nAre we firing the thrusters during the orbit simulation?\nPress 1 for Yes\nPress 2 for No\n"))
    while fire!=1 and fire!=2:
        print("\nInvalid Response")
        print("Are we firing the thrusters during the orbit simulation")
        fire=int(input("Press 1 for Yes\nPress 2 for No"))
    if fire==1:
        fire_thruster=True
        t_fire_percent=int(input("\nAt what % of simulation time, we are firing the thrusters?\n"))
        dvx= float(input("\nEnter the increase in Vx due to thrusters: "))
        dvy = float(input("Enter the increase in Vy due to thrusters: "))
    else:
        t_fire_percent=0 
        dvx=0
        dvy=0
        fire_thruster=False

    return  [fire_thruster,t_fire_percent,dvx,dvy]

# Firing the thruster
def burn(state,deltavx,deltavy):
    state[2]=state[2]+deltavx
    state[3]=state[3]+deltavy
    return state


# Choosing the integrator and thruster
integrator=choose_integrator() 
fire_thruster,t_fire_percent,dvx,dvy=if_thruster_fire()
t_fire=(t_fire_percent/100)*t_final

# Propagation
while t[-1]<t_final:

    # Firing the thruster at given time
    if fire_thruster==True:
        if np.abs(t_fire-t[-1])<0.1:
            state=burn(state,dvx,dvy)
            fire_thruster=False

    # Without thruster propagation
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
E=0.5*(np.array(vx)**2+np.array(vy)**2) -mu/r
L=(np.array(x)*np.array(vy)-np.array(y)*np.array(vx))

orbit_classifier(E,r)

# Plotting the graphs
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
