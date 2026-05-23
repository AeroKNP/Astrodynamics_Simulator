import numpy as np


# Defining the variables for earth and moon
mu_earth=3.986e14
mu_moon = 4.9048695e12

x_moon,y_moon=[3.844e8,0]

# Making the system for only earth state
def earth_system(t,state):
    x,y,vx,vy=state

    dxdt=vx
    dydt=vy

    r_earth=np.sqrt(x**2+y**2)

    dvxdt=-mu_earth*x/(r_earth**3)
    dvydt=-mu_earth*y/(r_earth**3)

    return np.array([dxdt,dydt,dvxdt,dvydt])

# Making the system for moon earth state
def earth_moon_system(t,state):
    x,y,vx,vy=state

    dxdt=vx
    dydt=vy

    r_earth=np.sqrt(x**2+y**2)
    r_moon=np.sqrt((x-x_moon)**2+(y-y_moon)**2)

    dvxdt=-mu_earth*x/(r_earth**3) - mu_moon*(x-x_moon)/(r_moon)**3
    dvydt=-mu_earth*y/(r_earth**3) - mu_moon*(y-y_moon)/(r_moon)**3

    return np.array([dxdt,dydt,dvxdt,dvydt])


