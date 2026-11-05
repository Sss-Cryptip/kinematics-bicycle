#Check parameters validity (only substitution for now)
import numpy as np

#counter error rises from angle = 90 -> tangent -> undefined
def steering_angle_check(delta :float):
    num_check("Steering angle", delta)
    if delta not in range(-90.0, 91.0) or not np.isfinite(delta):
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
    correct = np.isinfinite(num)
    if correct:
        raise ValueError(f"{name} must be a finite number.")
    if not correct:
        raise TypeError(f"{name} must be a number.")
