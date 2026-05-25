import matplotlib.pyplot as plt

# This function plots the orbits of all bodies 
def plotting(sun_cords,earth_cords,mars_cords,jupiter_cords):
    
    xsun,ysun=sun_cords
    xearth,yearth=earth_cords
    xmars,ymars=mars_cords
    xjupiter,yjupiter=jupiter_cords

    fig,ax=plt.subplots()

    ax.plot(xsun,ysun,color='black',label='Sun')
    ax.plot(xearth,yearth,color='blue',label='Earth')
    ax.plot(xmars,ymars,color='red',label='Mars')
    ax.plot(xjupiter,yjupiter,color='brown',label='Jupiter')
    ax.set_aspect('equal')
    
    sun=plt.Circle((0,0),6.957e8,color='yellow',fill=True)
    ax.add_patch(sun)

    ax.set_xlabel("X Co ordinate")
    ax.set_ylabel("Y Co ordinate")

    ax.legend()
    ax.grid()

    plt.show()

