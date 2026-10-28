# Hardware map and calibration record

This is the team's current **provisional** map, updated from the written notes
and Pybricks backup received on 2026-10-28. Confirm every port against the
physical build before running a program. In particular, HubClaw port F is
unknown and must not be initialized as a guessed sensor type.

## HubDriver

| Port | Connection |
| --- | --- |
| A | Lower-left LEGO SPIKE color sensor, facing the floor; about 1.3 cm above it |
| B | Lower-right LEGO SPIKE color sensor, facing the floor; about 1.3 cm above it |
| C | Rear-right drive motor |
| D | Front-left drive motor |
| E | Front-right drive motor |
| F | Rear-left drive motor |

The team reports that the wheel motors they checked rotate forward with positive
rotation, but confirmation for all four motors is still outstanding.

## HubClaw

| Port | Connection |
| --- | --- |
| A | Front LEGO SPIKE color sensor aimed at cubes, mounted about 2 cm above floor |
| B | Empty / not assigned |
| C | Claw motor |
| D | Elevator motor |
| E | LEGO SPIKE ultrasonic distance sensor; exact physical orientation unconfirmed |
| F | Type, orientation, and function unconfirmed; do not assume color or distance |

The team reports the claw can carry two cubes stacked vertically. Physical
retention and stability on the course are not yet documented.

## Provisional geometry

Earlier notes record a lateral wheel-center spacing of **15.5 cm**, longitudinal
axle spacing of approximately **8.05 cm**, and mecanum wheel diameter of
approximately **6.225 cm**. A newer message mentions **8.3 cm** without saying
which centers were measured. Keep all these values provisional until the team
identifies what 8.3 cm refers to and remeasures the current build.

The current source constants (`WHEEL_RADIUS_CM = 3`, `LX_CM = 12.818 / 2`,
`LY_CM = 7.978 / 2`) are legacy estimates and disagree with the earlier written
measurements. They are not calibrated and are not currently used by the
low-level drive class. The old frame notes (8 cm lateral, 13.5 cm structural
height) also need rechecking after the physical changes. The complete robot,
including fully extended claw, must remain within the competition's
300 x 300 mm footprint.

## Historical actuator references - not confirmed on the current build

| Motion | Old angle / timing note | Status |
| --- | --- | --- |
| Claw open | 389°; old timed test also used 2.3 s at 180°/s | Unconfirmed |
| Claw closed | -60°; old timed test also used 0.4 s at 180°/s | Unconfirmed |
| Elevator down | 197°; old timed test used 0.7 s at 180°/s | Unconfirmed |
| Elevator up | -1262° | Unconfirmed |

Do not treat old angles or timed motions as current calibration. The code blocks
claw/elevator movement until `MECHANISM_CALIBRATION_CONFIRMED` is deliberately
enabled after supervised calibration. Autonomous drive and pickup also remain
blocked by `BLE_PROTOCOL_CONFIRMED` until the two-hub protocol is tested. Do not
enable either flag solely to make a program start; do not drive mechanisms into
hard stops.

## Sensor readings and calibration

The backup includes readout attempts for the lower A/B sensors, a sensor at F,
the ultrasonic sensor at E, and a color sensor at F. These scripts do not prove
the physical identity or hub assignment of port F. One log reports that
`ColorSensor.rgb()` is unsupported on the tested firmware; the new in-project
diagnostics use `color()` and `reflection()` for known sensor ports.

Older floor HSV values remain in `hub_driver/constants.py` only as historical
samples. They are not verified on the current build or arena surface. New
readings for both lower sensors and the front cube sensor are still required.
Calibrate any side color sensor separately only after confirming that one is
physically present. Do not reuse floor samples as cube thresholds.

## Communication and strategy status

Two-hub BLE communication has not been confirmed. The prototype channel values
in the scripts do not match, and no successful exchange test is recorded.
Platform localization in the Ecoponto, route sweep order, intersection logic,
180-degree turn conditions, and the white-cube signal remain undefined.
