from pybricks.parameters import Port


# HubClaw port map.
CLAW_SENSOR_PORT = Port.A
CLAW_MOTOR_PORT = Port.C
ELEVATOR_MOTOR_PORT = Port.D
ULTRASONIC_SENSOR_PORT = Port.E
SIDE_SENSOR_PORT = Port.F  # Sensor model/type still needs confirmation.

# Measured motor targets in degrees. Preserve the calibration angle reference.
CLAW_OPEN_ANGLE = 389
CLAW_CLOSED_ANGLE = -60
ELEVATOR_DOWN_ANGLE = 197
ELEVATOR_UP_ANGLE = -1262

CLAW_BENCH_SPEED = 20
ELEVATOR_BENCH_SPEED = 20
BENCH_STEP_DEGREES = 10

# BLE channel assignments reserved for the eventual two-hub protocol.
BLE_CHANNEL_CLAW_TO_DRIVER = 144
BLE_CHANNEL_DRIVER_TO_CLAW = 141
