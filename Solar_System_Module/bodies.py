# This contains data of all the bodies used by the solar system module

import numpy as np

sun={
    "mu" : 1.327e20,
    "state" : np.array([0.0,0.0,0.0,0.0])
}

earth={
    "mu" : 3.986e14,
    "state" : np.array([1.496e11,0.0,0,29784])
}

mars={
    "mu" : 4.283e13,
    "state" : np.array([2.279e11,0.0,0.0,24130])
}

jupiter={
    "mu" : 1.267e17,
    "state" : np.array([7.784e11,0.0,0.0,13060])
}

bodies=[sun,earth,mars,jupiter]