#Check parameters validity (only substitution for now)
import numpy as np

'''Checking input as valid numbers and in the capped range'''

#counter error rises from angle = 90 -> tangent -> undefined
def steering_angle_check(delta :float):
    #delta = round(delta, 1)
    num_check("Steering angle", delta)
    if delta < -90.0 or delta > 90.0 or not np.isfinite(delta):
        raise ValueError("Steering angle must be between -90 and 90 degrees.")
    

#m/s^2
def acceleration_check(a :float):
    num_check("Acceleration", a)
    if a < -5.0 or a > 5.0:
        raise ValueError("Acceleration must be between -5.0 and 5.0 m/s^2.")


#m/s
def velocity_check(v :float):
    num_check("Velocity", v)
    if v < 0.0 or v > 5.0:
        raise ValueError("Velocity must be between 0 and 5 m/s.")



def dt_check(dt :float):
    num_check("Time step", dt)
    if dt <= 0.0 or dt > 0.05:
        raise ValueError("Time step must be between 0 and 0.05 seconds.")


def num_check(name, num :float):
    correct = np.isfinite(num)
    if not correct:
        raise ValueError(f"{name} must be a finite number.")
    if not isinstance(num, (int, float)):
        raise TypeError(f"{name} must be a number.")

#Check for malformed state output
def state_check(state):
    if not isinstance(state, (list, np.ndarray)):
            raise TypeError("State must be a list or numpy array.")
    if len(state) != 4:
        raise ValueError("Not the right number of parameters to unpack. 4 element is expected.")
    else:
        x, y, yaw, v = state
        num_check("x", x)
        num_check("y", y)
        num_check("yaw", yaw)
        velocity_check(v)
        
    
def input_check(cmd):
    elements = [item.strip() for item in cmd.split(",")]
    for item in elements:
        input_value = float(item)
        if not isinstance(input_value, float):
            #bug here is confusing
            raise ValueError("Input must be two numbers separated by a comma.")
    if len(elements) != 2:
        raise ValueError("Input must contain exactly two values separated by a comma.")
    if "," not in cmd:
        raise ValueError("Input must be separated by a comma.")

