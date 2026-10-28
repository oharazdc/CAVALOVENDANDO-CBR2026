"""Raw color and reflection readings for HubDriver's two floor sensors."""

from pybricks.pupdevices import ColorSensor

from constants import GROUND_LEFT_PORT, GROUND_RIGHT_PORT


class GroundSensors:
    def __init__(self) -> None:
        self.left = ColorSensor(GROUND_LEFT_PORT)
        self.right = ColorSensor(GROUND_RIGHT_PORT)

    def read_left_color(self):
        return self.left.color()

    def read_right_color(self):
        return self.right.color()

    def read_left_reflection(self) -> int:
        return self.left.reflection()

    def read_right_reflection(self) -> int:
        return self.right.reflection()
