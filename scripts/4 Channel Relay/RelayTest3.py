import RPi.GPIO as GPIO
from time import sleep

# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

# Time to sleep between operations in the main loop
SleepTimeS = 0.5

# Main Loop
try:
        while (True):

            # Turn all relays ON
            GPIO.output(2, GPIO.HIGH)
            GPIO.output(3, GPIO.HIGH)
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(17, GPIO.HIGH)
            # Sleep for 5 seconds
            sleep(SleepTimeS)
            # Turn all relays OFF
            GPIO.output(2, GPIO.LOW)
            GPIO.output(3, GPIO.LOW)
            GPIO.output(4, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            # Sleep for 5 seconds
            sleep(SleepTimeS)

# End program cleanly with keyboard
except KeyboardInterrupt:
    print "Good bye!"
    GPIO.cleanup()
