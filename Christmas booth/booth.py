#!/usr/bin/python
from gpiozero import PWMLED
from gpiozero import Button
from signal import pause
import os
import time

# Define take photo
def take_photo():
        os.system('fswebcam -r 640x480 -D 5 --no-banner --overlay christmas.png /home/pi/webcam/%d-%m-%Y_%H:%M:%S.jpg -S 2')
        os.system("echo '\n\n\n\n\n\n\033[1mYour photo has been saved!\n\033[00mYour photo will be available from \033[1m WEBSITE \033[00m tonight.")
        time.sleep(10)
        os.system('clear')
        os.system("echo '\033[1mPush button to take photograph\033[00m'")

# Define LED and Button pins | Type "pinout" into the terminal to find your pin numbers
led = PWMLED(15)
button = Button(7)

# Instructions
os.system('clear')
os.system("echo '\033[1mPush button to take photograp\033[00m'")

# Pulse LED and take photo when Button is pressed
led.pulse()
button.when_pressed = take_photo

# Loop
pause()
