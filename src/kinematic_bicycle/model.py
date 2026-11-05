#model logic simulating as a base of mini-fsae project

import numpy as np
import check

#given accelertion and steering angle what does a bicycle do 
'''Define parameters for the kinematic bicycle model'''
L :float = 0.22 # Wheelbase in meters (~22cm as base line)


'''Derive formulas physics for bicycle model
    State = [x, y, yaw, v]
    e.g. model_derivation([0.0, 0.0, 0.0, 0.0], 1.0, 10.0, 0.05)
'''
def model_derivation(state,a :float, delta :float, dt :float):
    check.input_check(a, delta)
    check.dt_check(dt)
    
    [x, y, yaw, v] = state
    
    v_new = v + a * dt
    deltar = np.radians(delta)
    #rounded to 10 dc to avoid inf/NaN errors
    if round(deltar,10) == 0.0:
        yaw_rate :float = 0.0
    else:
        yaw_rate :float = v_new/L * np.tan(deltar)

    x_dot :float = v_new * np.cos(yaw)
    y_dot :float = v_new * np.sin(yaw)
    new_state = np.array([x + x_dot * dt, y + y_dot * dt, yaw + yaw_rate * dt, v_new])
    check.state_check(new_state)
    return new_state

    

'''Calculate radius of when turning
    e.g. radius(1.0, 10.0)
'''
def radius(v :float, delta :float):
    deltar = np.radians(delta)
    r_path = L /v * np.tan(deltar)
    return r_path
