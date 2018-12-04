#!/bin/bash

# Set date
DATE=$(date +"%Y-%m-%d_%H%M")

# Take photo 1280 x 720
fswebcam -r 1280x720 -D 5 --no-banner --overlay christmas.png /home/pi/webcam/$DATE.jpg

# Display photo
gpicview /home/pi/webcam/$DATE.jpg

#  Wait 5
sleep 5

# Kill photo
pkill -f gpicview

# Exit
exit
