# Simulating the orbit equation using euler equation and doing it manually 
# 
# 
import numpy as np
import matplotlib.pyplot as plt

# Initiallsing the variables 
x=[1.0]
y=[0.0]
state=np.array([[x[0],y[0]]])

# Getting the derivatives
def derivative(t,state):
    x=state[0]
    y=state[1]

    dxdt=-y
    dydt=x

    return np.array([dxdt,dydt])

# Creating the time array
t=np.array([0.0])
dt=0.2
t_final = 20

# State update
while t[-1]<t_final:
    state=np.append(state,[state[-1]+(derivative(t,state[-1]))*dt],axis=0)
    t=np.append(t,t[-1]+dt)
    x.append(state[-1][0])
    y.append(state[-1][1])

# Getting the radius
r=np.zeros(len(x))
for i in range(len(x)):
    r[i]=np.sqrt((x[i])**2+(y[i])**2)


# Plotting the graphs
fig,ax=plt.subplots(2,2,figsize=(10,12))
plt.subplots_adjust(hspace=0.5,wspace=0.5)

ax[0][0].plot(t,x)
ax[0][0].set_xlabel("Time")
ax[0][0].set_ylabel("X Co ordinate")
ax[0][0].grid()

ax[0][1].plot(t,y)
ax[0][1].set_xlabel("Time")
ax[0][1].set_ylabel("Y Co ordinate")
ax[0][1].grid()

ax[1][0].plot(x,y)
ax[1][0].set_aspect('equal')
ax[1][0].set_xlabel("X Co ordinate")
ax[1][0].set_ylabel("Y Co ordinate")
ax[1][0].grid()

ax[1][1].plot(t,r)
ax[1][1].set_xlabel("Time")
ax[1][1].set_ylabel("Radius")
ax[1][1].grid()

plt.show()