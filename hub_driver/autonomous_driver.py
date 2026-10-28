"""Experimental low-speed approach; locked until the BLE protocol is verified.

Run this program on HubDriver at the same time as hub_claw/autonomous_pickup.py.
Keep the robot raised for the first test and verify wheel directions first.
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis
from pybricks.tools import wait

from constants import (
    BLE_PROTOCOL_CONFIRMED,
    FRONT_LEFT_PORT,
    FRONT_RIGHT_PORT,
    REAR_LEFT_PORT,
    REAR_RIGHT_PORT,
)
from pybricks.pupdevices import Motor


if not BLE_PROTOCOL_CONFIRMED:
    raise RuntimeError(
        "Locomocao autonoma bloqueada: valide o protocolo BLE entre os hubs."
    )


CLAW_TO_DRIVER = 144
DRIVER_SPEED = 60  # deg/s; deliberately slow for the first test
COMMAND_TIMEOUT_MS = 500

hub = PrimeHub(
    front_side=Axis.Z,
    top_side=Axis.X,
    broadcast_channel=145,
    observe_channels=[CLAW_TO_DRIVER],
)

motors = [
    Motor(FRONT_LEFT_PORT),
    Motor(FRONT_RIGHT_PORT),
    Motor(REAR_LEFT_PORT),
    Motor(REAR_RIGHT_PORT),
]

print("HubDriver waiting for HubClaw. All wheels will run slowly forward.")
last_command = None
last_sequence = None
last_command_time = 0

while True:
    packet = hub.ble.observe(CLAW_TO_DRIVER)
    now = hub.system.time()

    if (
        isinstance(packet, tuple)
        and len(packet) == 2
        and packet[0] in ("FWD", "STOP")
        and packet[1] != last_sequence
    ):
        last_command = packet[0]
        last_sequence = packet[1]
        last_command_time = now
        print("Command:", last_command)

    if last_command == "FWD" and now - last_command_time <= COMMAND_TIMEOUT_MS:
        for motor in motors:
            motor.run(DRIVER_SPEED)
    else:
        for motor in motors:
            motor.brake()
        if last_command == "FWD":
            last_command = "STOP"
            print("BLE timeout: stopped")

    wait(50)
