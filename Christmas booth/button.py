#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_state = GPIO.input(26)

	if input_state == True:
        	os.system('fswebcam -r 640x480 -D 5 --no-banner --overlay christmas.png /home/pi/webcam/%d-%m-%Y_%H:%M:%S.jpg -S 2')
        	time.sleep(5)
