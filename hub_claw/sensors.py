"""HubClaw sensor access. Port F is omitted until its sensor type is confirmed."""

from pybricks.pupdevices import ColorSensor, UltrasonicSensor

from constants import CLAW_SENSOR_PORT, ULTRASONIC_SENSOR_PORT


class ClawSensors:
    def __init__(self) -> None:
        self.claw_color = ColorSensor(CLAW_SENSOR_PORT)
        self.front_distance = UltrasonicSensor(ULTRASONIC_SENSOR_PORT)

    def read_cube_hsv(self) -> tuple:
        hsv = self.claw_color.hsv()
        return hsv.h, hsv.s, hsv.v

    def read_front_distance_mm(self) -> int:
        return self.front_distance.distance()
