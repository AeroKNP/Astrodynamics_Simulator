# This contains data of all the bodies used by the solar system module

import numpy as np
from Core import constants as cons

sun={
    "mu" : cons.mu_sun,
    "state" : np.array([0.0,0.0,0.0,0.0])
}

earth={
    "mu" : cons.mu_earth,
    "state" : np.array([1.496e11,0.0,0,29784])
}

mars={
    "mu" : cons.mu_mars,
    "state" : np.array([2.279e11,0.0,0.0,24130])
}

jupiter={
    "mu" : cons.mu_jupiter,
    "state" : np.array([7.784e11,0.0,0.0,13060])
}

satellite={
    "mu" : 0,
    "state" : np.array([earth["state"][0]+cons.R_earth,earth["state"][1],earth["state"][2]+3000.0,earth["state"][3]])
}

bodies=[sun,earth,mars,jupiter,satellite]

for body in bodies:
    body["history"]=[body["state"].copy()]
