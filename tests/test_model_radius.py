#testing
from src.kinematic_bicycle import model
import numpy as np

L = 0.22
ANGLES = [5, 10, 15, 30, 45]
dt = 0.02
v = 5.0
run_time_steps = 3000


def r_circle_fit_check(x, y):
    #from x^2 + y^2 = R^2 
    #Use matrix to solve instead [x,y,1]
    A =  A = np.column_stack([x, y, np.ones_like(x)])
    C = x**2 + y **2
    p, q, c = variable
    #least square solver*
    variable = np.linalg.lstsq(A, C, rcond=None)[0]
    x_c, y_c = p/2, q/2
    R = np.sqrt(c + x_c**2 + y_c**2)
    return R
#outputs the R of circle of the path


def measure(deg :float, ):
    x_pos, y_pos = [], []
    state = [0.0, 0.0, 0.0, v]
    for _ in range (run_time_steps):
        new_state = model.model_derivation(state, 0.0, deg ,dt)
        x_pos.append(new_state[0])
        y_pos.append(new_state[1])
    return r_circle_fit_check(np.array(x_pos), np.array(y_pos))   
    
    
def result():
    rows = ["| Steering angle | Theoretical R (m) | Measured R (m) | Error |",
            "|---|---|---|---|"]
    for deg in ANGLES:
        expected = model.radius(v, deg)
        measured = measure(deg)
        error = abs(measured - expected) / expected * 100
        rows.append(f"| {deg} deg | {expected:.3f} | {measured:.3f} | {error:.4f}% |")
    table = "\n".join(rows)

    print(table)
    print(f"\nParameters: wheelbase {L} m, speed {V} m/s, time step {DT} s, {run_time_steps} steps")


result()