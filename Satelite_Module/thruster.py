
# Contains the burn 
def burn(state,deltavx,deltavy):
    state[2]=state[2]+deltavx
    state[3]=state[3]+deltavy
    return state