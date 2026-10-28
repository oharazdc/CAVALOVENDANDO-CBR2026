"""Small individual-wheel bench test. Lift the robot before using it."""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button
from pybricks.tools import wait

from constants import BENCH_STEP_DEGREES, BENCH_STEP_SPEED
from drive import Drive


hub = PrimeHub(front_side=Axis.Z, top_side=Axis.X)
drive = Drive()

print("Driver wheel test: LEFT=FL, RIGHT=FR, BLUETOOTH=RL, LEFT+RIGHT=RR")
print("Each press moves one wheel by only 5 degrees. Center stops the program.")

while True:
    pressed = hub.buttons.pressed()
    if Button.CENTER in pressed:
        drive.stop()
        break

    wheel = None
    if Button.LEFT in pressed and Button.RIGHT in pressed:
        wheel = "rear_right"
    elif Button.LEFT in pressed:
        wheel = "front_left"
    elif Button.RIGHT in pressed:
        wheel = "front_right"
    elif Button.BLUETOOTH in pressed:
        wheel = "rear_left"

    if wheel is not None:
        drive.jog_wheel(wheel, BENCH_STEP_DEGREES, BENCH_STEP_SPEED)
        print(wheel, "angles:", drive.motor_angles())
        while hub.buttons.pressed():
            wait(20)
    wait(20)
