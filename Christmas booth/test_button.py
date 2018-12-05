#!/usr/bin/python

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

# Define what to do on button push
def button_callback(channel):
    print("Button was pushed!")

# Set up physical GPIO 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Run event on pin 26 rising edge
GPIO.add_event_detect(26,GPIO.RISING,callback=button_callback) 

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
