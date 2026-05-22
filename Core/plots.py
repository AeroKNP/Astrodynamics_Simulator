import matplotlib.pyplot as plt
import numpy as np

def plot_orbit(x,y,t,E,L,r_earth,x_moon,y_moon,use_moon):
    
    fig,ax=plt.subplots(2,2,figsize=(14,16))
    plt.subplots_adjust(hspace=0.5,wspace=0.5)

    ax[0][0].plot(x,y)
    earth = plt.Circle((0,0), 8e-2, fill=True)
    ax[0][0].add_patch(earth)

    if use_moon:
        moon = plt.Circle((x_moon,y_moon),8e-2,color="red",fill=True)
        ax[0][0].add_patch(moon)
        ax[0][0].set_xlim(min(np.min(x),x_moon)-1,max(np.max(x),x_moon)+1)
        ax[0][0].set_ylim(min(np.min(y),y_moon)-1,max(np.max(y),y_moon)+1)

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

    ax[1][1].plot(t,r_earth)
    ax[1][1].set_xlabel("Time")
    ax[1][1].set_ylabel("Radius")
    ax[1][1].grid()

    plt.show()

