"""HubClaw startup monitor. This entry point intentionally does not move."""

from pybricks.hubs import PrimeHub
from pybricks.tools import wait

from claw import Claw
from sensors import ClawSensors


hub = PrimeHub()
claw = Claw()
sensors = ClawSensors()
claw.stop()

print("HubClaw online; diagnostic mode, no movement commanded.")
print("Motor angles:", claw.angles())
print("Cube color sensor is configured on HubClaw port F; port A is unassigned.")

while True:
    print("Claw color:", sensors.read_cube_color())
    print("Claw reflection:", sensors.read_cube_reflection())
    print("Claw HSV:", sensors.read_cube_hsv())
    print("Observed HSV candidates (not validated):", sensors.observed_cube_color_candidates())
    print("Front distance mm:", sensors.read_front_distance_mm())
    wait(500)
