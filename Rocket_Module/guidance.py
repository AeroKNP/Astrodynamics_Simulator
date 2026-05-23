# This is the guidance module currently it gives the angle of firing to the thrusters

import numpy as np

t_turn=15

def calc_theta(t,mission_phase):  

    if mission_phase=="rise":
        theta=90
    else:
        theta=90-0.67*(t-t_turn)

    # Safety clamp to prevent downward firing
    if theta<0:
        theta=0

    return theta







