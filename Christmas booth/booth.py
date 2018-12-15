#!/usr/bin/python
from gpiozero import PWMLED
from gpiozero import Button
from signal import pause
from PIL import Image
import glob
import os
import time

# Define take photo
def take_photo():
        os.system("echo 'We will take your photo in'")
        
        #Countdown
        count = 5
        while count != 0:
                print(count)
                sleep(1)
                os.system("clear")
                count -= 1
                
        #Take Photo
        os.system('fswebcam -r 640x480 --no-banner --overlay christmas.png /home/pi/webcam/%d-%m-%Y_%H:%M:%S.jpg -S 2')
        os.system('clear')
        
        #Open image
        list_of_files = glob.glob('/home/pi/webcam/*.jpg')
        latest_file = max(list_of_files, key=os.path.getctime)
        img = Image.open(latest_file)
        img.show()
        
        #Exit message
        os.system("echo '\033[1mYour photo has been saved!\n\033[00mYour photo will be available from \033[1m WEBSITE \033[00m tonight.")
        time.sleep(10)
        
        #Reset
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
