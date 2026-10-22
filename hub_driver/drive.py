"""Low-level HubDriver motor access; no autonomous motion is started here."""

from pybricks.pupdevices import Motor

from constants import (
    FRONT_LEFT_PORT,
    FRONT_RIGHT_PORT,
    REAR_LEFT_PORT,
    REAR_RIGHT_PORT,
)


class Drive:
    def __init__(self) -> None:
        self.front_left = Motor(FRONT_LEFT_PORT)
        self.front_right = Motor(FRONT_RIGHT_PORT)
        self.rear_left = Motor(REAR_LEFT_PORT)
        self.rear_right = Motor(REAR_RIGHT_PORT)

    def motor_angles(self) -> dict:
        return {
            "front_left": self.front_left.angle(),
            "front_right": self.front_right.angle(),
            "rear_left": self.rear_left.angle(),
            "rear_right": self.rear_right.angle(),
        }

    def jog_wheel(self, name: str, degrees: int, speed: int) -> None:
        """Move exactly one wheel by a small relative angle for bench checks."""
        motor = {
            "front_left": self.front_left,
            "front_right": self.front_right,
            "rear_left": self.rear_left,
            "rear_right": self.rear_right,
        }.get(name)
        if motor is None:
            raise ValueError("Unknown wheel name: " + name)
        if not 0 < speed <= 120:
            raise ValueError("Bench speed must be between 1 and 120 deg/s.")
        if not -10 <= degrees <= 10:
            raise ValueError("Bench jog must be at most 10 degrees.")
        motor.run_angle(speed, degrees)

    def stop(self) -> None:
        self.front_left.brake()
        self.front_right.brake()
        self.rear_left.brake()
        self.rear_right.brake()
