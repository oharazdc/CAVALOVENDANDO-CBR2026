"""Read-only live readout for the known HubClaw front color sensor on A."""

from pybricks.hubs import PrimeHub
from pybricks.tools import wait

from sensors import ClawSensors


hub = PrimeHub()
sensors = ClawSensors()

print("Claw color sensor F readout. No motors are moved.")
print("Measure real cubes at the mounted viewing distance; do not infer thresholds.")

while True:
    print(
        "Color/reflection/HSV/observed candidates:",
        sensors.read_cube_color(),
        sensors.read_cube_reflection(),
        sensors.read_cube_hsv(),
        sensors.observed_cube_color_candidates(),
    )
    wait(300)
