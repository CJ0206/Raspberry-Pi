#!/usr/bin/env python
from gpiozero import PWMLED
from signal import pause

# Set LED pin and for PWM
led = PWMLED(15)

# Run PWM
led.pulse()

# Loop
pause()
