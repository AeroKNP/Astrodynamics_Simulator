# This is the guidance module currently it gives the desired angle of firing to the thrusters
# It also has a basic PID Controller in it
#  
import numpy as np

t_turn=15
k=0.67

# Calculating the desired theta value based upon current time and mission phase
def calc_theta_desried(t,mission_phase):  

    if mission_phase=="rise":
        theta_des=90
    else:
        theta_des=90-k*(t-t_turn)

    # Safety clamp to prevent downward firing
    if theta_des<0:
        theta_des=0

    return theta_des

# PID Controller to match the actual theta to desired theta
def PID(theta_actual,theta_des,prev_error,integrated,dt):
    
    kp,ki,kd=[2.0,0.01,0.5]

    error=theta_des-theta_actual
    dedt=(error-prev_error)/dt
    integrated+=error*dt

    theta_dot=(kp*error)+(ki*integrated)+(kd*dedt)

    theta_dot=max(min(theta_dot,5.0),-5.0)

    return  theta_dot,error,integrated




