"""Bounded low-level claw and elevator controls for HubClaw."""

from pybricks.parameters import Stop
from pybricks.pupdevices import Motor

from constants import (
    CLAW_BENCH_SPEED,
    CLAW_CLOSED_ANGLE,
    CLAW_MOTOR_PORT,
    CLAW_OPEN_ANGLE,
    ELEVATOR_BENCH_SPEED,
    ELEVATOR_DOWN_ANGLE,
    ELEVATOR_MOTOR_PORT,
    ELEVATOR_UP_ANGLE,
)


class Claw:
    def __init__(self) -> None:
        # Keep the measured angle reference; do not zero motors on startup.
        self.claw_motor = Motor(CLAW_MOTOR_PORT, reset_angle=False)
        self.elevator_motor = Motor(ELEVATOR_MOTOR_PORT, reset_angle=False)

    def set_claw_angle(self, target: int, speed: int = CLAW_BENCH_SPEED) -> None:
        if not CLAW_CLOSED_ANGLE <= target <= CLAW_OPEN_ANGLE:
            raise ValueError("Claw target is outside the measured range.")
        if not 0 < speed <= CLAW_BENCH_SPEED:
            raise ValueError("Claw speed must be between 1 and 20 deg/s.")
        self.claw_motor.run_target(speed, target, then=Stop.HOLD)

    def set_elevator_angle(
        self, target: int, speed: int = ELEVATOR_BENCH_SPEED
    ) -> None:
        low = min(ELEVATOR_DOWN_ANGLE, ELEVATOR_UP_ANGLE)
        high = max(ELEVATOR_DOWN_ANGLE, ELEVATOR_UP_ANGLE)
        if not low <= target <= high:
            raise ValueError("Elevator target is outside the measured range.")
        if not 0 < speed <= ELEVATOR_BENCH_SPEED:
            raise ValueError("Elevator speed must be between 1 and 20 deg/s.")
        self.elevator_motor.run_target(speed, target, then=Stop.HOLD)

    def stop(self) -> None:
        self.claw_motor.hold()
        self.elevator_motor.hold()

    def angles(self) -> tuple:
        return self.claw_motor.angle(), self.elevator_motor.angle()
