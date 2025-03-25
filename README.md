# Raspberry Pi
Just some useful codes and some I have written or installed for my Raspberry Pi.

---
## [Force HDMI on the Raspberry Pi](/boot/config.txt)

When the raspberry pi boots without HDMI connected it automatically sets itself up to send video through composite, I wanted to change this as I only use a HDMI monitor so all I had to do was edit the config file.

```
sudo nano /boot/config.txt
```

and uncomment the following lines

```
# uncomment if hdmi display is not detected and composite is being output
hdmi_force_hotplug=1

# uncomment to force a specific HDMI mode (this will force VGA)
hdmi_group=1
hdmi_mode=5

# uncomment to force a HDMI mode rather than DVI. This can make audio work in
# DMT (computer monitor) modes
hdmi_drive=2
```

I changed hdmi_mode=5 to force 1080, you can change the resolution by referring to the documentation at [RaspberryPi.org](https://www.raspberrypi.org/documentation/configuration/config-txt/video.md)

---
## [Powering down a RaspberryPi using a momentary switch](/scripts/shutdown.py)

This code will safely power down your Raspberry Pi using a momentary switch.

#### Required Hardware
* [Rasberry Pi B v1.2](https://www.amazon.co.uk/Raspberry-Pi-Model-512MB-RAM/dp/B008PT4GGC)
* [Momentary Switch](https://www.amazon.co.uk/dp/B016YIYAH0/ref=wl_it_dp_o_pC_nS_ttl?_encoding=UTF8&colid=1VFE04IJ9AZ9T&coliid=I1Q0O4MYQDCNC2)

#### Prepairing Hardware
Plug the momentary switch into GPIO 7, Pin 26 and GND, Pin 25

![GPIO Pin Out](http://elinux.org/images/8/80/Pi-GPIO-header-26-sm.png)

#### Step 1
Before we get into the code you will need to make sure you have the latest software installed by running the following scripts:

```
sudo apt-get update
sudo apt-get upgrade

```

#### Step 2
Next you will need to create the shutdown scrypt, first open the editor:

```
sudo nano shutdown.py

```
Next paste the [shutdown.py](/scripts/shutdown.py) scrypt into the file. Press Ctrl + C, Y, and enter to save the scrypt.

#### Step 3
Next we want to run the file at start up by running 

```
sudo nano /etc/rc.local

```

and pasting the following code before 'exit 0'

```
sudo python /home/pi/shutdown.py &

```
Press Ctrl + C, Y, and enter to save the scrypt.

#### Step 4

Reboot your Pi and everything should work.

```
sudo shutdown -r now

```

---
## [Relay testing with Raspberry Pi](/scripts/4%20Channel%20Relay/)

These codes are written to test a four channel relay with a Raspberry Pi.

#### Hardware I used
* [Rasberry Pi B v1.2](https://www.amazon.co.uk/Raspberry-Pi-Model-512MB-RAM/dp/B008PT4GGC) 
* [4 channel relay](http://www.ebay.co.uk/itm/-/222433474124?roken=cUgayN)
* [Jumper cables](http://www.ebay.co.uk/itm/-/182307853751?roken=cUgayN)

#### Wiring Raspberry Pi A and B
* VCC to 5v
* IN1 to GPIO(2)
* IN2 to GPIO(3)
* IN3 to GPIO(4)
* IN4 to GPIO(17)
* GND to GND

![GPIO Pin Out](http://elinux.org/images/8/80/Pi-GPIO-header-26-sm.png)

#### Increase/Decrease Speed of Testing
You can increase or decrease the speed of each of these programs by changing the following line to the number of seconds you want before each step:

```
SleepTimeL = *

```

#### [RelayTest1.py](/scripts/4%20Channel%20Relay/RelayTest1.py)
The first file will count through each of the relays one by one, before turning them off and exiting.

#### [RelayTest2.py](/scripts/4%20Channel%20Relay/RelayTest2.py)
The second file will run through the relays turning them on and off one by one, to exit the program hold 'Ctrl + C'

#### [RelayTest3.py](/scripts/4%20Channel%20Relay/RelayTest3.py)
The last file will turn the relays on and off together, to exit the program hold 'Ctrl + C'

## Disable screen sleep
Edit lightdm
```
sudo nano /etc/lightdm/lightdm.conf
```
Look for the line starts “xserver-command” and modify as below:
```
xserver-command=X -s 0 -dpms
```
Reboot the system.
```
sudo reboot
```


---
## [Add voice shutdown and reboot to AIY](aiyprojects-raspbian/src/action.py)
Update the code in the link above using:
```
sudo nano ~/voice-recognizer-raspi/src/action.py

```
Restart the voice recogniser service:
```
sudo systemctl restart voice-recognizer.service

```

---
## Display GPIO pins
To see the pin out of your Raspberry Pi
```
pinout

```
By default, if stdout is a console that supports color, ANSI codes will be used to produce color output. Output can be forced to be monochrome:
```
pinout --monochrome
```
To manually specify the revision of Pi you want to query, use ```--revision```. To find the revision code you need you can [click here](https://elinux.org/RPi_HardwareHistory):
```
pinout -r 000d
```

---
## Clear terminal history
To clear the terminal history:
```
history -c
```

---
## [Install rpi-monitor with wifi stats](Install%20rpi-monitor%20to%20show%20wifi%20stats.md)


---
## [Install dump1090-FA, 360Radar, and FR24](Install%20dump1090-FA,%20360Radar,%20and%20FR24.md)


---
## [Update/Install 360Radar, FR24 and drump1090-multability](Update%20360radar%20feeder%20with%20dump1090-multability.md)

