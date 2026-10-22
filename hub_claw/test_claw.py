"""Button-controlled, bounded claw/elevator bench test for HubClaw."""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

from claw import Claw
from constants import (
    BENCH_STEP_DEGREES,
    CLAW_CLOSED_ANGLE,
    CLAW_OPEN_ANGLE,
    ELEVATOR_DOWN_ANGLE,
    ELEVATOR_UP_ANGLE,
)
from sensors import ClawSensors


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(value, high))


def wait_for_release(hub: PrimeHub) -> None:
    while hub.buttons.pressed():
        wait(20)


hub = PrimeHub()
claw = Claw()
sensors = ClawSensors()

print("No automatic movement.")
print("LEFT=open 10 deg; RIGHT=close 10 deg")
print("BLUETOOTH=elevator up 10 deg; LEFT+RIGHT=down 10 deg")
print("CENTER stops the program; angles:", claw.angles())
print("Cube HSV:", sensors.read_cube_hsv())
print("Distance mm:", sensors.read_front_distance_mm())

while True:
    pressed = hub.buttons.pressed()
    if Button.LEFT in pressed and Button.RIGHT in pressed:
        current = claw.elevator_motor.angle()
        target = clamp(
            current + BENCH_STEP_DEGREES,
            min(ELEVATOR_DOWN_ANGLE, ELEVATOR_UP_ANGLE),
            max(ELEVATOR_DOWN_ANGLE, ELEVATOR_UP_ANGLE),
        )
        claw.set_elevator_angle(target)
        print("Elevator target:", target)
    elif Button.LEFT in pressed:
        target = clamp(
            claw.claw_motor.angle() + BENCH_STEP_DEGREES,
            CLAW_CLOSED_ANGLE,
            CLAW_OPEN_ANGLE,
        )
        claw.set_claw_angle(target)
        print("Claw target:", target)
    elif Button.RIGHT in pressed:
        target = clamp(
            claw.claw_motor.angle() - BENCH_STEP_DEGREES,
            CLAW_CLOSED_ANGLE,
            CLAW_OPEN_ANGLE,
        )
        claw.set_claw_angle(target)
        print("Claw target:", target)
    elif Button.BLUETOOTH in pressed:
        current = claw.elevator_motor.angle()
        target = clamp(
            current - BENCH_STEP_DEGREES,
            min(ELEVATOR_DOWN_ANGLE, ELEVATOR_UP_ANGLE),
            max(ELEVATOR_DOWN_ANGLE, ELEVATOR_UP_ANGLE),
        )
        claw.set_elevator_angle(target)
        print("Elevator target:", target)

    if pressed:
        print("HSV:", sensors.read_cube_hsv())
        print("Distance mm:", sensors.read_front_distance_mm())
        wait_for_release(hub)
    wait(20)
