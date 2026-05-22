# In day 10, we'll be using our orbit simulator and adding a thruster module into it 
# We can vary when, how much, and in which direction we are firing the thruster
# Additional thing added is that we can fire multiple thrusters at differnt times
# 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# region Initialsing Variables
state=np.array([1.0,0.0,0.0,1.0])
history=[state.copy()]
mu=1
fire_thruster=False

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

# Checking if we are firing the thruster and getting the dv after thruster
def if_thruster_fire():

    # Checking if thruster firing is there
    fire=int(input("\nAre we firing the thrusters during the orbit simulation?\nPress 1 for Yes\nPress 2 for No\n"))
    while fire!=1 and fire!=2:
        print("\nInvalid Response")
        print("Are we firing the thrusters during the orbit simulation")
        fire=int(input("Press 1 for Yes\nPress 2 for No"))

    # If thruster fire is there
    if fire==1:
        fire_thruster=True

        # Checking how many times thruster is fired
        num_burn=int(input("\nHow many times are we firing the thrusters: "))

        t_fire_percent=np.zeros(num_burn)
        dvx=np.zeros(num_burn)
        dvy=np.zeros(num_burn)
        burn_pending=np.ones(num_burn,dtype=bool)

        # Getting the time and dv values of each thruster
        for i in range(num_burn):

            t_fire_percent[i]=int(input(f"\nAt what % of simulation time, we are firing the burn no. {i+1}: "))
            while t_fire_percent[i]<t_fire_percent[i-1]:
                print(f"\n\nInvalid time input the burn no. {i+1} must be after burn no. {i}")
                t_fire_percent[i]=int(input(f"\nAt what % of simulation time, we are firing the burn no. {i+1}: "))
            
            dvx[i]= float(input(f"Enter the increase in Vx due to burn no. {i+1}: "))
            dvy[i]= float(input(f"Enter the increase in Vy due to burn no. {i+1}: "))
    
    # If thruster fire is not there 
    else:
        t_fire_percent=0 
        dvx=0
        dvy=0
        fire_thruster=False
        burn_pending=False

    return  [fire_thruster,burn_pending,t_fire_percent,dvx,dvy]

# Firing the thruster
def burn(state,deltavx,deltavy):
    state[2]=state[2]+deltavx
    state[3]=state[3]+deltavy
    return state


# region Choosing the integrator and thruster 
integrator=choose_integrator() 
fire_thruster,burn_pending,t_fire_percent,dvx,dvy=if_thruster_fire()
t_fire=(t_fire_percent/100)*t_final

# endregion

# region Propagation
while t[-1]<t_final:

    # Firing the thruster at given time
    if fire_thruster==True:
        for i in range(len(t_fire)):
            if np.abs(t_fire[i]-t[-1])<0.1 and burn_pending[i]==True:
                state=burn(state,dvx[i],dvy[i])
                burn_pending[i]=False

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

# region Making the animation

# fig, ax = plt.subplots(figsize=(10,10))

# earth = plt.Circle((0,0),0.08,fill=True,color='blue')
# ax.add_patch(earth)

# trajectory, = ax.plot([],[],lw=2,label='Trajectory')
# spacecraft, = ax.plot([],[],'o',
#                       color='yellow',
#                       markersize=8,
#                       label='Spacecraft')

# ax.set_aspect("equal")
# ax.grid(True,linestyle='--',alpha=0.6)
# ax.legend()

# ax.set_xlim(np.min(x)-1,np.max(x)+1)
# ax.set_ylim(np.min(y)-1,np.max(y)+1)

# title=ax.set_title("Time = 0.00")

# # Skip frames so video isn't insanely large
# frame_skip=5

# def init():
#     trajectory.set_data([],[])
#     spacecraft.set_data([],[])
#     return trajectory,spacecraft

# def update(frame):

#     i=frame*frame_skip

#     if i>=len(x):
#         i=len(x)-1

#     trajectory.set_data(x[:i],y[:i])

#     spacecraft.set_data(
#         [x[i]],
#         [y[i]]
#     )

#     title.set_text(f"Time = {t[i]:.2f}")

#     return trajectory,spacecraft,title


# ani=FuncAnimation(
#     fig,
#     update,
#     frames=len(x)//frame_skip,
#     init_func=init,
#     interval=20,
#     blit=True
# )

# plt.show()

# endregion
