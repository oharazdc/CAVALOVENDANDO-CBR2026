"""HubDriver startup monitor. This entry point intentionally does not drive."""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis
from pybricks.tools import wait

from drive import Drive
from ground_sensors import GroundSensors


hub = PrimeHub(front_side=Axis.Z, top_side=Axis.X)
drive = Drive()
sensors = GroundSensors()
drive.stop()

print("HubDriver online; diagnostic mode, no movement commanded.")
print("Wheel angles:", drive.motor_angles())

while True:
    print("Floor candidates (HSV, closest reference):", sensors.candidates())
    wait(500)
