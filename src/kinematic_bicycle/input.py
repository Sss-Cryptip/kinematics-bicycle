#input

import numpy as np
from model import model_derivation
import check

'''Define state params :
Units 
    x, y, yaw, v = [m, m, rad, m/s] 
'''

initial_state = np.array([0.0, 0.0, 0.0, 0.0])  # [x, y, yaw, v]
np.set_printoptions(precision=3, suppress=True)
#Add printing restrictions to 3 dc. places more readable


while True:
    try:
        cmd = input(f"Enter acceleration and steering angle (a,delta): ")
        check.input_check(cmd)
        a, delta = map(float, cmd.split(','))
        new_state = model_derivation(initial_state, a, delta, 0.05)
        print(f"Update New state: {new_state}")
        initial_state = new_state

    except ValueError as e:
        print(f"Invalid input: {e}")
        
    except KeyboardInterrupt:
        print("Exiting the simulation.")
        break