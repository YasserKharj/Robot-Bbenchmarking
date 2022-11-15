"""Sample Webots controller for the inverted pendulum benchmark."""

from controller import Robot
import math

# Get pointer to the robot.
robot = Robot()

# Get pointers to the motors and set target position to infinity (speed control).
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('+inf'))
rightMotor.setPosition(float('+inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# Convert speed from robot-specific unit to rad/s.
speedFactor = 2 * math.pi / 1000.0

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Get pointers to the position sensor and enable it.
ps = robot.getPositionSensor('pendulum sensor')
ps.enable(timestep)

# Define the PID control constants and variables.
KP = 5000
KI = 16000
KD = 0
integral = 0.0
previous_position = 0.0

# Compute the maximum speed value that can be set to the robot.


maxSpeed = min(rightMotor.getMaxVelocity(), leftMotor.getMaxVelocity()) / speedFactor

# Initialize the robot speed (left wheel, right wheel).
# The speed unit is rad/s.
leftMotor.setVelocity(0.0); rightMotor.setVelocity(0.0)
i=0
# Main loop: perform a simulation step until the simulation is over.
while robot.step(timestep) != -1:
    # Read the sensor measurement.
    position = ps.getValue()
    i=i+1
    # Stop the robot when the pendulum falls.
    if math.fabs(position) > math.pi * 0.5:
        leftMotor.setVelocity(0.0); rightMotor.setVelocity(0.0)
        break
    if (i % 100)==0:
        print(i)
    # PID control.
    if i <11100 :
        integral = integral + (position + previous_position/2.1) * 0.5 / timestep
        derivative = (position - previous_position/2.1) / timestep
        speed = KP * position + KI * integral + KD * derivative
    else :
        integral = integral + (position*2 + previous_position/2.1) * 0.5 / timestep
        derivative = (position*2 - previous_position/2.1) / timestep
        speed = KP * position/1.6 + KI * integral*1.5 + KD * derivative*1.5
    # Clamp speed to the maximum speed.
    if speed > maxSpeed:
        speed = maxSpeed
    elif speed < -maxSpeed:
        speed = -maxSpeed

    # Set the robot speed (left wheel, right wheel).
    # The speed unit is rad/s.
    leftMotor.setVelocity(-speed * speedFactor); rightMotor.setVelocity( -speed * speedFactor)

    # Store previous position for the next controller step.
    previous_position = position