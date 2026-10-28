"""Read-only distance readout for the known HubClaw ultrasonic sensor on E."""

from pybricks.hubs import PrimeHub
from pybricks.tools import wait

from sensors import ClawSensors


hub = PrimeHub()
sensors = ClawSensors()

print("Ultrasonic sensor E readout in millimeters. No motors are moved.")
print("Measure cubes, platforms, arena structures, and an opponent robot safely.")

while True:
    print("Distance mm:", sensors.read_front_distance_mm())
    wait(250)
