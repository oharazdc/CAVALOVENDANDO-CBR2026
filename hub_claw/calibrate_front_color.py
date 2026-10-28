"""Read-only live readout for the known HubClaw front color sensor on A."""

from pybricks.hubs import PrimeHub
from pybricks.tools import wait

from sensors import ClawSensors


hub = PrimeHub()
sensors = ClawSensors()

print("Front color sensor A readout. No motors are moved.")
print("Measure real cubes at the mounted viewing distance; do not infer thresholds.")

while True:
    print(
        "Color/reflection:",
        sensors.read_cube_color(),
        sensors.read_cube_reflection(),
    )
    wait(300)
