#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Init list with pin numbers
pinList = [2, 3, 4, 17]

# Loop through pins and set mode state to 'low'
for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

# Time to sleep between operations in the main loop
SleepTimeL = 2

# Main loop
try:
        GPIO.output(2, GPIO.LOW)
        print "One"
        time.sleep(SleepTimeL)
        GPIO.output(3, GPIO.LOW)
        print "Two"
        time.sleep(SleepTimeL)
        GPIO.output(4, GPIO.LOW)
        print "Three"
        time.sleep(SleepTimeL)
        GPIO.output(17, GPIO.LOW)
        print "Four"
        time.sleep(SleepTimeL)
        GPIO.cleanup()
        print "Good bye!"

# End program cleanly with a keyboard
except KeyboardInterrupt:
        print "Good bye!"
        GPIO.cleanup()
