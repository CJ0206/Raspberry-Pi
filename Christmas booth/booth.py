#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sleep
import subprocess
import os

# Display Christmas image 
os.system ('feh --hide-pointer -x -q -B black -g 1280x800 "/home/pi/myscripts/christmas.gif" &')

# Use physical pin numbers (NOT GPIO NUMBERS)
GPIO.setmode(GPIO.BOARD)  

# When pin 26 is low run
def onButton(channel):
    if channel == 26:
        os.system("/home/pi/myscripts/webcam.sh")

# Setup pin 26 as input with internal pull-up resistor to hold it HIGH until pressed 
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Register an edge detection event on FALLING edge and run onButton 
GPIO.add_event_detect(16, GPIO.FALLING, callback=onButton, bouncetime=20)

# Exit on keyboard input
input()
