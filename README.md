# kinematics-bicycle

A Python simulation of a kinematic bicycle model, built as the first stage of my
miniature rc project to learn vehicle control from first principles.

@Current Stage : Phase 01


## Quick start
```bash
git clone git@github.com:Sss-Cryptip/kinematics-bicycle.git
cd kinematics-bicycle
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest                  # runs the verification test
```

## How it works
```
x'   = v * cos(yaw)
y'   = v * sin(yaw)
yaw' = (v / L) * tan(delta)
v'   = a
delta = delta(degrees)

```
State: x, y, yaw, v. Inputs: acceleration a, steering angle delta. L is the wheelbase.
Integrated with a fixed-step Euler update.

## Project structure
```
model.py   the model of bicycle
test_model.py        constant-steer test and plot
tests/             verification test (pytest)
results/           docs and plots relevant
```

## Roadmap
- [x] Kinematic bicycle model and verification
- [ ] Pure pursuit path tracking
- [ ] PID speed control with anti-windup, tested in simulation
- [ ] Stanley controller and comparison
- [ ] ROS 2 digital twin
- [ ] ESP32 firmware and hardware

## Limitations and what I learned
- Kinematic model: ignores tyre slip, so it is only valid at low speed and low lateral acceleration
- Euler integration: small steps needed for accuracy