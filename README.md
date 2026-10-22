# Cavalo Vendado - RCB Challenge 2026

Organized Pybricks project for the robot's two independent hubs. Each hub gets
its own program and its own port constants because `Port.A` means a different
physical connection on each hub.

## Project layout

```text
hub_driver/   HubDriver entry point, drive motors, and floor sensors
hub_claw/     HubClaw entry point, claw/elevator, and claw sensors
docs/         Hardware map and arena commissioning checklist
```

Keep all `.py` files in a hub's folder together when transferring that hub's
program. Start with that folder's `main.py`; use `test_driver.py` and
`test_claw.py` only for supervised bench checks.

## Known hardware map

### HubDriver

| Port | Device |
| --- | --- |
| A | Left floor color sensor |
| B | Right floor color sensor |
| C | Rear right drive motor |
| D | Front left drive motor |
| E | Front right drive motor |
| F | Rear left drive motor |

### HubClaw

| Port | Device |
| --- | --- |
| A | Claw color sensor |
| B | Empty |
| C | Claw open/close motor |
| D | Elevator motor |
| E | Ultrasonic sensor |
| F | Side sensor; device type still needs confirmation |

Motor target angles currently recorded for HubClaw:

- Claw: open `389°`, closed `-60°`.
- Elevator: down `197°` (5 mm above floor), up `-1262°` (75 mm above floor).

These values rely on the same motor-angle reference used during calibration.
Do not reset the motor angle before using them.

## Current state

This folder is a clean, safe starting project. The entry points only initialize
devices and report sensor readings; they do not start autonomous movement.
The diagnostic button programs move one mechanism at a time in small steps.
The robot is **not yet ready to run a competition match**: see
[`docs/arena_readiness.md`](docs/arena_readiness.md) for the remaining physical
commissioning work. Do not treat a successful Python upload as proof that the
robot can safely navigate or score.
