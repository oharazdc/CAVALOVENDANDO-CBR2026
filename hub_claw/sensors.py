"""HubClaw sensor access for claw color sensor F and ultrasonic sensor E."""

from pybricks.pupdevices import ColorSensor, UltrasonicSensor

from constants import CLAW_SENSOR_PORT, CUBE_HSV_OBSERVED, ULTRASONIC_SENSOR_PORT


class ClawSensors:
    def __init__(self) -> None:
        self.claw_color = ColorSensor(CLAW_SENSOR_PORT)
        self.front_distance = UltrasonicSensor(ULTRASONIC_SENSOR_PORT)

    def read_cube_hsv(self) -> tuple:
        hsv = self.claw_color.hsv()
        return hsv.h, hsv.s, hsv.v

    def read_cube_color(self):
        return self.claw_color.color()

    def read_cube_reflection(self) -> int:
        return self.claw_color.reflection()

    def observed_cube_color_candidates(self, hsv: tuple = None) -> tuple:
        """Return matches to observed HSV ranges, not validated color decisions."""
        if hsv is None:
            hsv = self.read_cube_hsv()

        hue, saturation, value = hsv
        matches = []
        for name, ranges in CUBE_HSV_OBSERVED.items():
            if ranges is None:
                continue
            h_range, s_range, v_range = ranges
            if (
                h_range[0] <= hue <= h_range[1]
                and s_range[0] <= saturation <= s_range[1]
                and v_range[0] <= value <= v_range[1]
            ):
                matches.append(name)
        return tuple(matches)

    def read_front_distance_mm(self) -> int:
        return self.front_distance.distance()
