import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from Core import constants as cons

# This function plots the orbits of all bodies 
def plotting(ax,sun_cords,earth_cords,mars_cords,jupiter_cords,satellite_cords):
    
    xsun=sun_cords[:,0]
    ysun=sun_cords[:,1]
    xearth=earth_cords[:,0]
    yearth=earth_cords[:,1]
    xmars=mars_cords[:,0]
    ymars=mars_cords[:,1]
    xjupiter=jupiter_cords[:,0]
    yjupiter=jupiter_cords[:,1]
    xsatellite=satellite_cords[:,0]
    ysatellite=satellite_cords[:,1]

    ax.plot(xsun,ysun,color='yellow',label='Sun')
    ax.plot(xearth,yearth,color='blue',label='Earth')
    ax.plot(xmars,ymars,color='red',label='Mars')
    ax.plot(xjupiter,yjupiter,color='brown',label='Jupiter')
    ax.plot(xsatellite,ysatellite,color='green',label='Satellite')
    ax.set_aspect('equal')
    
    sun=plt.Circle((0,0),cons.R_sun+6e9,color='yellow',fill=True)
    ax.add_patch(sun)

    ax.set_xlabel("X Co ordinate in sun centered frame")
    ax.set_ylabel("Y Co ordinate in sun centered frame")

    ax.legend()
    ax.grid()

# region This function animates the solar system
def animate_orbits(
    sun_cords,
    earth_cords,
    mars_cords,
    jupiter_cords,
    satellite_cords,
    t
):

    xsun, ysun = sun_cords
    xearth, yearth = earth_cords
    xmars, ymars = mars_cords
    xjupiter, yjupiter = jupiter_cords
    xsatellite, ysatellite = satellite_cords

    fig, ax = plt.subplots(figsize=(10,10))

    # Setting limits
    xmin = min(
        np.min(xearth),
        np.min(xmars),
        np.min(xjupiter),
        np.min(xsatellite)
    )

    xmax = max(
        np.max(xearth),
        np.max(xmars),
        np.max(xjupiter),
        np.max(xsatellite)
    )

    ymin = min(
        np.min(yearth),
        np.min(ymars),
        np.min(yjupiter),
        np.min(ysatellite)
    )

    ymax = max(
        np.max(yearth),
        np.max(ymars),
        np.max(yjupiter),
        np.max(ysatellite)
    )

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.set_aspect('equal')

    ax.set_xlabel("X Co ordinate")
    ax.set_ylabel("Y Co ordinate")

    ax.grid()

    # Orbit trails
    sun_line, = ax.plot([], [], color='yellow', label='Sun')
    earth_line, = ax.plot([], [], color='blue', label='Earth')
    mars_line, = ax.plot([], [], color='red', label='Mars')
    jupiter_line, = ax.plot([], [], color='brown', label='Jupiter')
    satellite_line, = ax.plot([], [], color='green', label='Satellite')

    # Planet patches
    sun_patch = plt.Circle((0,0), 3.5e10, color='yellow')
    earth_patch = plt.Circle((0,0), 1.5e10, color='blue')
    mars_patch = plt.Circle((0,0), 1.2e10, color='red')
    jupiter_patch = plt.Circle((0,0), 3e10, color='brown')
    satellite_patch = plt.Circle((0,0), 5e9, color='green')

    ax.add_patch(sun_patch)
    ax.add_patch(earth_patch)
    ax.add_patch(mars_patch)
    ax.add_patch(jupiter_patch)
    ax.add_patch(satellite_patch)

    # Timer text
    timer_text = ax.text(
        0.02,
        0.95,
        '',
        transform=ax.transAxes,
        fontsize=12
    )

    ax.legend()

    def update(frame):

        # Updating orbit trails
        sun_line.set_data(xsun[:frame], ysun[:frame])
        earth_line.set_data(xearth[:frame], yearth[:frame])
        mars_line.set_data(xmars[:frame], ymars[:frame])
        jupiter_line.set_data(xjupiter[:frame], yjupiter[:frame])
        satellite_line.set_data(
            xsatellite[:frame],
            ysatellite[:frame]
        )

        # Updating planet positions
        sun_patch.center = (
            xsun[frame],
            ysun[frame]
        )
        earth_patch.center = (xearth[frame], yearth[frame])
        mars_patch.center = (xmars[frame], ymars[frame])
        jupiter_patch.center = (
            xjupiter[frame],
            yjupiter[frame]
        )

        satellite_patch.center = (
            xsatellite[frame],
            ysatellite[frame]
        )

        # Time in months
        months = t[frame] / (60*60*24*30)

        timer_text.set_text(
            f"Months Passed : {months:.2f}"
        )

        return (
            sun_line,
            earth_line,
            mars_line,
            jupiter_line,
            satellite_line,
            sun_patch,
            earth_patch,
            mars_patch,
            jupiter_patch,
            satellite_patch,
            timer_text
        )

    ani = FuncAnimation(
        fig,
        update,
        frames=range(1, len(t),50),
        interval=1,
        blit=False
    )

    plt.show()

# endregion