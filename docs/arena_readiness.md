# Arena readiness checklist

The files in this project are an organized starting point, not a certified
competition program. Complete and record these checks before autonomous runs.

- [ ] Confirm the side sensor on HubClaw port F model and behavior.
- [ ] Measure cube colors with the HubClaw port A sensor at the real claw
      distance; identify all seven competition colors and unknown readings.
- [ ] Confirm the four wheel directions and mecanum roller orientation with the
      robot lifted, then test forward, sideways, and rotation on the floor.
- [ ] Calibrate actual distance per motor degree, turn accuracy, and heading
      behavior on the competition surface.
- [ ] Verify the claw/elevator angle reference survives program start and hub
      power cycles. Test every target with the robot supported and at low speed.
- [ ] Determine a gentle cube-grip angle; do not use the fully closed endpoint
      to squeeze a cube unless the mechanism has been checked physically.
- [ ] Map platform colors and positions as required for each match.
- [ ] Implement and bench-test the two-hub Bluetooth message protocol.
- [ ] Implement the autonomous route and one-cube pickup/delivery state machine.
- [ ] Verify immediate response to red boundary lines and avoidance of brown
      center obstacles, white cubes, cubes without a destination, and opponents.
- [ ] Check the full extended footprint stays within 300 x 300 mm.
- [ ] Run repeated full-course trials under the 12-minute match limit.

Never run a new motor target against a hard stop at full speed. Keep the robot
clear of people and arena edges during all commissioning tests.
