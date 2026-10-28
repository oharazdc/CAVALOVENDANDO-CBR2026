"""Read-only live readout for the known HubDriver floor sensors A and B."""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis
from pybricks.tools import wait

from ground_sensors import GroundSensors


hub = PrimeHub(front_side=Axis.Z, top_side=Axis.X)
sensors = GroundSensors()

print("Ground sensor readout: A=left, B=right. No motors are moved.")
print("Record readings for each real arena surface/color and lighting setup.")

while True:
    print(
        "A color/reflection:",
        sensors.read_left_color(),
        sensors.read_left_reflection(),
    )
    print(
        "B color/reflection:",
        sensors.read_right_color(),
        sensors.read_right_reflection(),
    )
    wait(500)
