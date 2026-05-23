# This is the guidance module currently it gives the angle of firing to the thrusters

import numpy as np

def calc_theta(t):  

    theta=90-0.05*t

    # Safety clamp to prevent downward firing
    if theta<0:
        theta=0

    return theta







