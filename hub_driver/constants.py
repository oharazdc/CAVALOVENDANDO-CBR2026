from pybricks.parameters import Port


# HubDriver port map.
GROUND_LEFT_PORT = Port.A
GROUND_RIGHT_PORT = Port.B
REAR_RIGHT_PORT = Port.C
FRONT_LEFT_PORT = Port.D
FRONT_RIGHT_PORT = Port.E
REAR_LEFT_PORT = Port.F

# Provisional geometry notes only. These values conflict with newer physical
# notes and must not be used for calibrated motion until remeasured.
MAX_MOTOR_SPEED = 700
BENCH_STEP_SPEED = 60
BENCH_STEP_DEGREES = 5
WHEEL_RADIUS_CM = 3  # Legacy estimate; newer note says diameter ~= 6.225 cm.
LX_CM = 12.818 / 2  # Legacy estimate; axis convention/measurement unverified.
LY_CM = 7.978 / 2  # Legacy estimate; axis convention/measurement unverified.
WALL_TO_ROAD_CM = 8

# Autonomous BLE movement is disabled until the two-hub protocol is tested.
BLE_PROTOCOL_CONFIRMED = False

# Legacy floor HSV samples, not verified on the current build or arena surface.
# Do not use these as final color thresholds without fresh calibration.
GROUND_HSV_LEFT = {
    "blue": (217, 57, 28),
    "red": (350, 84, 62),
    "green": (140, 37, 22),
    "yellow": (57, 39, 58),
    "black": (200, 20, 14),
    "white": (194, 15, 65),
    "brown": (330, 19, 26),
}

GROUND_HSV_RIGHT = {
    "blue": (222, 59, 38),
    "red": (354, 86, 78),
    "green": (140, 36, 31),
    "yellow": (55, 42, 78),
    "black": (200, 9, 18),
    "white": (193, 13, 80),
    "brown": (345, 29, 35),
}
