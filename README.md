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

## VS Code setup on Windows

The project includes a local Python 3.12 environment in `.venv-pybricks` with
`pybricksdev` installed. Open this project folder in VS Code. The VS Code task
menu includes the hub monitors and supervised diagnostics. For a diagnostic
task, turn on only the hub you intend to program so BLE cannot choose the other.

To use the command line from this folder:

```powershell
.\.venv-pybricks\Scripts\pybricksdev.exe run ble hub_driver\test_driver.py --name HubDriver --no-wait
```

Use `hub_claw\test_claw.py` for the other hub. The autonomous prototype is not
included in the VS Code tasks yet because the hubs' firmware version and BLE
device names have not been confirmed.

`pybricksdev` on the computer uploads/runs code. Pybricks firmware must already
be installed on each hub; it cannot be confirmed without connecting to the
hardware. The separately installed `pybricks` package supplies editor support,
not the hub firmware.

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
| A | Front color sensor aimed at cubes (~2 cm above floor) |
| B | Empty |
| C | Claw open/close motor |
| D | Elevator motor |
| E | Ultrasonic distance sensor; exact physical orientation still needs confirmation |
| F | Unconfirmed device; do not initialize as a color or distance sensor until checked |

Historical HubClaw motor targets (not confirmed against the current physical build):

- Claw: open `389°`, closed `-60°`.
- Elevator: down `197°` (5 mm above floor), up `-1262°` (75 mm above floor).

Do not use these angles or the old timed motor values as current calibration.
Claw/elevator movement and autonomous pickup are blocked until calibration is
confirmed in code after a supervised check.

## Current state

This folder is a clean, safe starting project. The entry points only initialize
devices and report sensor readings; they do not start autonomous movement.
The wheel diagnostic moves one wheel by a small step. Claw/elevator movement is
locked until the current mechanism calibration is confirmed in
`hub_claw/constants.py`. Read-only sensor diagnostics are available for the
known HubDriver A/B sensors and HubClaw A/E sensors; HubClaw port F remains
unassigned until its physical device is identified.
The robot is **not yet ready to run a competition match**: see
[`docs/arena_readiness.md`](docs/arena_readiness.md) for the remaining physical
commissioning work. Do not treat a successful Python upload as proof that the
robot can safely navigate or score.

The autonomous pickup/drive prototypes are blocked by default until the
mechanism calibration and two-hub BLE protocol are confirmed. The Pybricks
backup also contains port-F and timed-motor experiments that are not treated as
current hardware assignments or validated calibration.

## Competition and autonomy reference

For the complete Portuguese reference to the official rules, arena zones,
scoring, object handling, autonomous mission flow, installed sensors, current
software limitations, and future-agent guidance, read
[`docs/GUIA_MESTRE_COMPETICAO_E_AUTONOMIA.md`](docs/GUIA_MESTRE_COMPETICAO_E_AUTONOMIA.md)
before changing strategy or robot behavior.
