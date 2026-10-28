from pybricks.parameters import Port


# HubClaw port map.
CLAW_SENSOR_PORT = Port.F
CLAW_MOTOR_PORT = Port.C
ELEVATOR_MOTOR_PORT = Port.D
ULTRASONIC_SENSOR_PORT = Port.E
# Port A is not assigned in the latest hardware map.

# Historical motor targets in degrees. The team has not confirmed these against
# the current physical build. Mechanism movement stays disabled until calibrated.
MECHANISM_CALIBRATION_CONFIRMED = False
BLE_PROTOCOL_CONFIRMED = False
CLAW_OPEN_ANGLE = 389
CLAW_CLOSED_ANGLE = -60
ELEVATOR_DOWN_ANGLE = 197
ELEVATOR_UP_ANGLE = -1262
# Physical direction notes from the team. Pybricks' default positive motor
# direction is clockwise when viewed from the motor shaft; current angle limits
# remain provisional and must be recalibrated before enabling movement.
CLAW_CLOCKWISE_CLOSES = True
ELEVATOR_CLOCKWISE_LOWERS = True

# Observed cube HSV ranges from the current sensor setup. These are candidate
# ranges only; do not use them as final pickup decisions until validated.
CUBE_HSV_OBSERVED = {
    "red": ((348, 354), (77, 80), (26, 28)),
    "yellow": ((55, 56), (61, 62), (99, 100)),
    "green": ((170, 180), (57, 67), (7, 10)),
    "blue": ((189, 200), (66, 71), (8, 10)),
    "black": ((170, 190), (45, 51), (7, 10)),
    "white": ((194, 215), (15, 27), (34, 100)),
    # Brown hue is only approximate; it is not matched until a range is measured.
    "brown": None,
}
CUBE_HSV_RANGES_VALIDATED = False
CUBE_HSV_APPROXIMATE = {"brown": (10, (39, 42), (20, 22))}

CLAW_BENCH_SPEED = 20
ELEVATOR_BENCH_SPEED = 20
BENCH_STEP_DEGREES = 10

# Historical/unverified BLE channel notes. The current prototype uses different
# raw channel values and has not passed a two-hub communication test.
BLE_CHANNEL_CLAW_TO_DRIVER = 144
BLE_CHANNEL_DRIVER_TO_CLAW = 141
