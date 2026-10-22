"""Raw and reference-based readings for HubDriver's two floor sensors."""

from pybricks.pupdevices import ColorSensor

from constants import (
    GROUND_HSV_LEFT,
    GROUND_HSV_RIGHT,
    GROUND_LEFT_PORT,
    GROUND_RIGHT_PORT,
)


def _hue_distance(first: int, second: int) -> int:
    difference = abs(first - second)
    return min(difference, 360 - difference)


def nearest_reference(hsv: tuple, references: dict) -> tuple:
    """Return the closest calibration as (color_name, normalized_distance).

    The caller must choose and validate a rejection threshold on the real mat;
    the closest sample alone is only a candidate, not a guaranteed color ID.
    """
    hue, saturation, value = hsv
    best_name = None
    best_distance = None
    for name, reference in references.items():
        ref_h, ref_s, ref_v = reference
        distance = (
            (_hue_distance(hue, ref_h) / 180) ** 2
            + ((saturation - ref_s) / 100) ** 2
            + ((value - ref_v) / 100) ** 2
        ) ** 0.5
        if best_distance is None or distance < best_distance:
            best_name = name
            best_distance = distance
    return best_name, best_distance


class GroundSensors:
    def __init__(self) -> None:
        self.left = ColorSensor(GROUND_LEFT_PORT)
        self.right = ColorSensor(GROUND_RIGHT_PORT)

    def read_left_hsv(self) -> tuple:
        color = self.left.hsv()
        return color.h, color.s, color.v

    def read_right_hsv(self) -> tuple:
        color = self.right.hsv()
        return color.h, color.s, color.v

    def candidates(self) -> tuple:
        left_hsv = self.read_left_hsv()
        right_hsv = self.read_right_hsv()
        return (
            (left_hsv, nearest_reference(left_hsv, GROUND_HSV_LEFT)),
            (right_hsv, nearest_reference(right_hsv, GROUND_HSV_RIGHT)),
        )
