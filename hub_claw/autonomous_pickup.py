"""One-cube approach-and-grab proof of concept for HubClaw.

It approaches whatever is in front of the ultrasonic sensor; it does not yet
classify cube colors or search the arena. Start only in a clear, bounded area.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

from claw import Claw
from constants import (
    CLAW_OPEN_ANGLE,
    ELEVATOR_DOWN_ANGLE,
    ELEVATOR_UP_ANGLE,
)
from sensors import ClawSensors


CLAW_TO_DRIVER = 144
APPROACH_DISTANCE_MM = 80
APPROACH_TIMEOUT_MS = 8000
STABLE_READINGS = 3

hub = PrimeHub(broadcast_channel=141, observe_channels=[145])
claw = Claw()
sensors = ClawSensors()


message_sequence = 0


def tell_driver(command: str) -> None:
    global message_sequence
    message_sequence += 1
    # A changing sequence number lets HubDriver detect a lost BLE heartbeat.
    hub.ble.broadcast((command, message_sequence))
    wait(100)


def wait_for_start() -> None:
    print("Place one cube ahead, clear the area, then press Bluetooth to start.")
    while Button.BLUETOOTH not in hub.buttons.pressed():
        wait(20)
    while Button.BLUETOOTH in hub.buttons.pressed():
        wait(20)


try:
    tell_driver("STOP")
    wait_for_start()

    # Prepare the mechanism using the team's recorded calibration angles.
    claw.set_claw_angle(CLAW_OPEN_ANGLE)
    claw.set_elevator_angle(ELEVATOR_DOWN_ANGLE)

    print("Approaching. Press the hub center button to abort.")
    start_time = hub.system.time()
    near_count = 0
    found = False

    while hub.system.time() - start_time < APPROACH_TIMEOUT_MS:
        if Button.CENTER in hub.buttons.pressed():
            break

        distance = sensors.read_front_distance_mm()
        if 0 < distance <= APPROACH_DISTANCE_MM:
            near_count += 1
        else:
            near_count = 0

        if near_count >= STABLE_READINGS:
            found = True
            break

        tell_driver("FWD")
        wait(50)

    tell_driver("STOP")
    wait(300)  # allow HubDriver to receive STOP and brake

    if found:
        print("Object nearby; closing claw and lifting.")
        # Conservative partial close: avoids driving to the hard-stop angle.
        grip_target = max(-60, min(389, claw.claw_motor.angle() - 80))
        claw.set_claw_angle(grip_target)
        claw.set_elevator_angle(ELEVATOR_UP_ANGLE)
        print("Pickup sequence complete. Check physically whether it held a cube.")
    else:
        claw.set_elevator_angle(ELEVATOR_DOWN_ANGLE)
        print("No object reached. Robot stopped; no pickup attempted.")

finally:
    tell_driver("STOP")
    claw.stop()
