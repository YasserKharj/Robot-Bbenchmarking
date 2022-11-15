"""Sample Webots controller for the square path benchmark."""
 
from controller import Robot
 
# Get pointer to the robot.
robot = Robot()
 
# Get pointer to each wheel of our robot.
leftWheel = robot.getMotor('left wheel')
rightWheel = robot.getMotor('right wheel')
 
# Repeat the following 4 times (once for each side).
for i in range(0, 4):
    leftWheel.setPosition(float('inf'))
    rightWheel.setPosition(float('inf'))
    leftWheel.setVelocity(5.24)
    rightWheel.setVelocity(5.24)
    # Wait for the robot to reach a corner.
    if i == 0:
        robot.step(3900) 
    if i == 1:
        robot.step(3950) 
    if i == 2:
        robot.step(3960) 
    if i == 3:
        robot.step(3960)
 
    leftWheel.setVelocity(5.24)
    rightWheel.setVelocity(-5.01)
    # Wait until the robot has turned 90 degrees clockwise.
    robot.step(480)
 
# Stop the robot when path is completed, as the robot performance
# is only computed when the robot has stopped.
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)