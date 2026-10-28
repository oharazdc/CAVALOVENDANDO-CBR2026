from pybricks.parameters import Port


# HubClaw port map.
CLAW_SENSOR_PORT = Port.A
CLAW_MOTOR_PORT = Port.C
ELEVATOR_MOTOR_PORT = Port.D
ULTRASONIC_SENSOR_PORT = Port.E
SIDE_SENSOR_PORT = Port.F  # Sensor model/type still needs confirmation.

# Historical motor targets in degrees. The team has not confirmed these against
# the current physical build. Mechanism movement stays disabled until calibrated.
MECHANISM_CALIBRATION_CONFIRMED = False
BLE_PROTOCOL_CONFIRMED = False
CLAW_OPEN_ANGLE = 389
CLAW_CLOSED_ANGLE = -60
ELEVATOR_DOWN_ANGLE = 197
ELEVATOR_UP_ANGLE = -1262

CLAW_BENCH_SPEED = 20
ELEVATOR_BENCH_SPEED = 20
BENCH_STEP_DEGREES = 10

# Historical/unverified BLE channel notes. The current prototype uses different
# raw channel values and has not passed a two-hub communication test.
BLE_CHANNEL_CLAW_TO_DRIVER = 144
BLE_CHANNEL_DRIVER_TO_CLAW = 141
