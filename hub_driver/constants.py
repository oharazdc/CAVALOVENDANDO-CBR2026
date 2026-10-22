from pybricks.parameters import Port


# HubDriver port map.
GROUND_LEFT_PORT = Port.A
GROUND_RIGHT_PORT = Port.B
REAR_RIGHT_PORT = Port.C
FRONT_LEFT_PORT = Port.D
FRONT_RIGHT_PORT = Port.E
REAR_LEFT_PORT = Port.F

# Drive parameters from the team's current measurements.
MAX_MOTOR_SPEED = 700
BENCH_STEP_SPEED = 60
BENCH_STEP_DEGREES = 5
WHEEL_RADIUS_CM = 3
LX_CM = 12.818 / 2
LY_CM = 7.978 / 2
WALL_TO_ROAD_CM = 8

# HubDriver floor sensor HSV references, ordered as (hue, saturation, value).
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
