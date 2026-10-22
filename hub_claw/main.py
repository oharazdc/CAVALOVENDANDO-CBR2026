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

while True:
    print("Claw sensor HSV:", sensors.read_cube_hsv())
    print("Front distance mm:", sensors.read_front_distance_mm())
    wait(500)
