import numpy as np
import pandas as pd

def log_event(t,message):

    print(f"[T={t:.2f}s] {message}")

def log_state(t,history,tsolar=None,solar_history=None):
    df_earth=pd.DataFrame({
        "Time":t,
        "X": history[:,0],
        "Y": history[:,1],
        "Vx": history[:,2],
        "Vy": history[:,3],
        "Mass": history[:,4],
        "Phase": "Earth"
    })
    if solar_history is not None:
        df_solar=pd.DataFrame({
            "Time":tsolar,
            "X": solar_history[:,0],
            "Y": solar_history[:,1],
            "Vx": solar_history[:,2],
            "Vy": solar_history[:,3],
            "Mass": history[-1,4],
            "Phase": "Solar"
        })

        df=pd.concat([df_earth,df_solar],ignore_index=True)
    else:
        df=df_earth
        
    df.to_csv("trajectory.csv",index=False)
