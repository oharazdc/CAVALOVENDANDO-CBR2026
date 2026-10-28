# Arena readiness checklist

The files in this project are an organized starting point, not a certified
competition program. Complete and record these checks before autonomous runs.

- [ ] Confirm the HubClaw port F claw color sensor orientation and behavior.
- [ ] Confirm HubClaw port A is unused in the current physical build, or update
      the map if a device is connected there.
- [ ] Confirm the exact orientation of the HubClaw port E ultrasonic sensor.
- [ ] Measure cube colors with the HubClaw port F sensor at the real claw
      distance; identify all seven competition colors and unknown readings.
      Validate the observed HSV ranges, especially blue, green, and black,
      before using any match as an autonomous pickup decision.
- [ ] Confirm the four wheel directions and mecanum roller orientation with the
      robot lifted, then test forward, sideways, and rotation on the floor.
- [ ] Resolve the wheel-geometry notes: older lateral spacing 15.5 cm,
      longitudinal spacing 8.05 cm, diameter 6.225 cm, and newer ambiguous
      8.3 cm measurement. Re-measure the current robot before using odometry.
- [ ] Calibrate actual distance per motor degree, turn accuracy, and heading
      behavior on the competition surface.
- [ ] Verify the claw/elevator angle reference survives program start and hub
      power cycles. Test every target with the robot supported and at low speed.
      Confirm physically that clockwise closes the claw and lowers the elevator
      with the current motor mounting and Pybricks direction settings.
- [ ] Confirm the historical angles (claw 389°/-60°, elevator 197°/-1262°)
      against the current build. Old timed values (2.3 s, 0.4 s, 0.7 s at
      180°/s) are references only; do not use them as calibration.
- [ ] Determine a gentle cube-grip angle; do not use the fully closed endpoint
      to squeeze a cube unless the mechanism has been checked physically.
- [ ] Map platform colors and positions as required for each match.
- [ ] Implement and bench-test the two-hub Bluetooth message protocol.
- [ ] Check current BLE channel assignments: prototype sender/receiver
      channels do not match. Keep autonomous drive disabled until verified.
- [ ] Implement the autonomous route and one-cube pickup/delivery state machine.
- [ ] Verify immediate response to red boundary lines and avoidance of brown
      center obstacles, white cubes, cubes without a destination, and opponents.
- [ ] Check the full extended footprint stays within 300 x 300 mm.
- [ ] Run repeated full-course trials under the 12-minute match limit.

Never run a new motor target against a hard stop at full speed. Keep the robot
clear of people and arena edges during all commissioning tests.
