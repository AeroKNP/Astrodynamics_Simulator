import numpy as np

# Making the controller
def controller(state,t,prev_states,burn_pending):
    xn=state[0]
    yn=state[1]
    rn=np.sqrt(xn**2+yn**2)

    xn_1=prev_states[0]
    yn_1=prev_states[1]
    rn_1=np.sqrt(xn_1**2+yn_1**2)

    xn_2=prev_states[4]
    yn_2=prev_states[5]
    rn_2=np.sqrt(xn_2**2+yn_2**2)

    if rn>1.4 and burn_pending==True: # Temporarily disabling the burns from controller
        fire=False
    else:
        fire=False
    
    # burn values temporarily coded in the controller
    dvx=0.0
    dvy=0.25

    return fire,dvx,dvy