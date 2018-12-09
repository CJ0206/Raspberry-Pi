#!/usr/bin/python
from gpiozero import Button
from signal import pause
import os

# Set what to do when button is pressed 
def take_photo():
    os.system('fswebcam -r 640x480 -D 5 --no-banner --overlay christmas.png /home/pi/webcam/%d-%m-%Y_%H:%M:%S.jpg -S 2')

# Set Button pin
button = Button(7)

# Run code when Button is presssed
button.when_pressed = take_photo

# Loop
pause()
