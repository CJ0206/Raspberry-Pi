#!/usr/bin/python
from gpiozero import PWMLED
from gpiozero import Button
from signal import pause
from time import sleep
from PIL import Image
import glob
import os

# Define take photo
def take_photo():
        os.system('clear')
        print('\n\n\n\n\n\033[1mWe will take your photo in:')
        sleep(2)

        # Countdown
        count = 5
        while count != 0:
                print(count)
                sleep(1)
                count -= 1
        
        # Smile
        os.system('clear')
        print('\n\n\n\n\n\033[1mSmile!')
        sleep(2)
        os.system('clear')

        #Take Photo
        os.system('fswebcam -r 640x480 --no-banner --overlay christmas.png /home/pi/webcam/%d-%m-%Y_%H:%M:%S.jpg -S 2')
        os.system('clear')

        # Open image
        list_of_files = glob.glob('/home/pi/webcam/*.jpg')
        latest_file = max(list_of_files, key=os.path.getctime)
        img = Image.open(latest_file)
        img.show()

        # Save message
        print('\n\n\n\n\n\033[1mYour photo has been saved!\n\nYour photo will be available from XXXXXXX')
        sleep(10)

        # Reset
        os.system('clear')
        print("\n\n\n\n\n\033[1mPush button to take photograph")

# Define LED and Button pins | Type "pinout" into the terminal to find your pin numbers
led = PWMLED(15)
button = Button(7)

# Instructions
os.system('clear')
print('\n\n\n\n\n\033[1mPush button to take photograp')

# Pulse LED and take photo when Button is pressed
led.pulse()
button.when_pressed = take_photo

# Loop
pause()
