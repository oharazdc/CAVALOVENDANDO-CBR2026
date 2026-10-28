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
print("Port F is intentionally not initialized until its physical type is confirmed.")

while True:
    print("Claw color:", sensors.read_cube_color())
    print("Claw reflection:", sensors.read_cube_reflection())
    print("Front distance mm:", sensors.read_front_distance_mm())
    wait(500)
