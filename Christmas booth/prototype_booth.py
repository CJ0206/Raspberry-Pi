#!/usr/bin/python
import gpiozero
from signal import pause
import os
import time

# Define take photo
def take_photo():
    os.system('fswebcam -r 640x480 -D 5 --no-banner --overlay christmas.png /home/pi/webcam/%d-%m-%Y_%H:%M:%S.jpg -S 2')
    time.sleep(5)
 
# Define LED and Button Pins | Type "pinout" into the terminal to find your pin numbers
led = PWMLED(15)
button = Button(7)

# Pulse LED and take photo when Button is pressed
led.pulse()
button.when_pressed = take_photo

# Loop
pause()
