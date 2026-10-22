# Hardware map and calibration record

## HubDriver

| Port | Connection |
| --- | --- |
| A | Left lower color sensor |
| B | Right lower color sensor |
| C | Rear right motor |
| D | Front left motor |
| E | Front right motor |
| F | Rear left motor |

Known drive measurements: wheel radius 3 cm; `LX = 12.818 / 2 cm`;
`LY = 7.978 / 2 cm`; `WALL_TO_ROAD = 8 cm`. Motor direction signs and
distance/turn accuracy still need physical verification.

## HubClaw

| Port | Connection |
| --- | --- |
| A | Color sensor mounted at the claw |
| B | Empty |
| C | Claw motor |
| D | Elevator motor |
| E | Ultrasonic sensor |
| F | Side sensor; sensor type not recorded yet |

| Motion | Target angle | Physical reference |
| --- | ---: | --- |
| Claw open | 389° | 9 cm opening |
| Claw closed | -60° | Calibrated closed endpoint |
| Elevator down | 197° | Claw 0.5 cm above floor |
| Elevator up | -1262° | Claw 7.5 cm above floor |

The frame dimensions given by the team are 8 cm lateral and 13.5 cm structural
height. The claw must stay within the competition's 30 x 30 cm footprint even
when fully extended.

## HubDriver floor sensor HSV samples

Samples below are reference readings, not validated classification ranges.

| Color | Left (H,S,V) | Right (H,S,V) |
| --- | --- | --- |
| Blue | (217, 57, 28) | (222, 59, 38) |
| Red | (350, 84, 62) | (354, 86, 78) |
| Green | (140, 37, 22) | (140, 36, 31) |
| Yellow | (57, 39, 58) | (55, 42, 78) |
| Black | (200, 20, 14) | (200, 9, 18) |
| White | (194, 15, 65) | (193, 13, 80) |
| Brown | (330, 19, 26) | (345, 29, 35) |

The claw color sensor needs its own cube calibration at its actual viewing
distance and lighting. Floor samples must not be reused as claw sensor samples.
