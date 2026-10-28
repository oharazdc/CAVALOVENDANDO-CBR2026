# Hardware map and calibration record

This is the team's current map, updated from the written notes
received on 2026-10-28. Dimensions and sensor HSV ranges remain approximate or
unvalidated as marked below. Confirm ports against the physical build before
running a program.

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
| A | Unassigned in the latest hardware map |
| B | Empty / not assigned |
| C | Claw motor |
| D | Elevator motor |
| E | LEGO SPIKE ultrasonic distance sensor; exact physical orientation unconfirmed |
| F | LEGO SPIKE color sensor in the claw, used to identify cubes; mounted about 2 cm above floor |

Physical actuator directions reported by the team: clockwise closes the claw
and counterclockwise opens it; counterclockwise raises the elevator and
clockwise lowers it. Pybricks defines positive motor direction as clockwise by
default when viewed from the output shaft. The angle endpoints below remain
unconfirmed, so movement stays locked.

The team reports the claw can carry two cubes stacked vertically. Physical
retention and stability on the course are not yet documented. Sensor E is
ultrasonic and about 2.9 cm above the floor; its exact pointing direction still
needs confirmation.

## Provisional geometry

Earlier notes record a lateral wheel-center spacing of **15.5 cm**, longitudinal
axle spacing of approximately **8.05 cm**, and mecanum wheel diameter of
approximately **6.225 cm**. A newer message mentions **8.3 cm** without saying
which centers were measured. Keep all these values provisional until the team
identifies what 8.3 cm refers to and remeasures the current build.

The source geometry constants have been updated to radius 3.1125 cm,
`LX_CM = WHEELBASE_CM / 2`, and `LY_CM = TRACK_WIDTH_CM / 2`. Measurements remain
approximate; the 8.3 cm note is still unresolved, and actual distance/turn
accuracy is not calibrated. The old frame notes (8 cm lateral, 13.5 cm
structural height) also need rechecking after the physical changes. The complete robot,
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

The backup includes readout attempts for the lower A/B sensors, the ultrasonic
sensor at E, and the claw color sensor at F. One log reports that
`ColorSensor.rgb()` is unsupported on the tested firmware; use `hsv()` for
cube readings. The in-project diagnostics also print `color()` and
`reflection()` for context.

Older floor HSV values remain in `hub_driver/constants.py` only as historical
samples. They are not verified on the current build or arena surface. Observed
cube HSV ranges are stored in `hub_claw/constants.py`; they are not definitive
classification limits. Validate especially blue/green/black before using them
for autonomous pickup. The brown hue was reported only as approximately 10, so
the code deliberately does not match brown to a candidate yet. Do not reuse
floor samples as cube thresholds.

| Cube color | H (hue) | S (saturation) | V (brightness) |
| --- | ---: | ---: | ---: |
| Red | 348–354 | 77–80 | 26–28 |
| Yellow | 55–56 | 61–62 | 99–100 |
| Green | 170–180 | 57–67 | 7–10 |
| Blue | 189–200 | 66–71 | 8–10 |
| Black | 170–190 | 45–51 | 7–10 |
| White | 194–215 | 15–27 | 34–100 |
| Brown | ~10 | 39–42 | 20–22 |

Brown's hue is approximate and is intentionally not included in automatic
candidate matching yet. The code prints candidate matches only; it does not use
these observations to authorize pickup.

## Communication and strategy status

Two-hub BLE communication has not been confirmed. The prototype channel values
in the scripts do not match, and no successful exchange test is recorded.
Platform localization in the Ecoponto, route sweep order, intersection logic,
180-degree turn conditions, and the white-cube signal remain undefined.
