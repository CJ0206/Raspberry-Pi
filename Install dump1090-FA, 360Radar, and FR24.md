# Instructions on how to install [dump1090-fa](https://uk.flightaware.com/adsb/piaware/install)


Ensure that you have the latest OS updates before you install FlightAware packages.:
```
sudo apt update
sudo apt full-upgrade
sudo reboot
```

Download and install the FlightAware APT repository package, which tells your Pi's package manager (apt) how to find FlightAware's software packages in addition to the packages provided by Raspbian.
```
wget https://uk.flightaware.com/adsb/piaware/files/packages/pool/piaware/f/flightaware-apt-repository/flightaware-apt-repository_1.2_all.deb
sudo dpkg -i flightaware-apt-repository_1.2_all.deb
```

Update your apt package sources and install PiAware. This will install all the required dependencies on your Raspberry Pi.
```
sudo apt update
sudo apt install piaware
```

Enable automatic and manual (web-based, via your request) PiAware software updates. These updates are disabled by default. To leave updates disabled, skip this step.
```
sudo piaware-config allow-auto-updates yes
sudo piaware-config allow-manual-updates yes
```

Install FlightAware's version of dump1090 by executing the following command.
```
sudo apt install dump1090-fa
```

978 MHz UAT is only present in the U.S., if you need it execute the following.
```
sudo apt install dump978-fa
```

Once you have finished installing and configuring the packages, reboot your Raspberry Pi to ensure that everything starts correctly.
```
sudo reboot
```

You should wait about four or five minutes for your PiAware to start and then you can associate your FlightAware account with your PiAware device to receive all the benefits.
[https://uk.flightaware.com/adsb/piaware/claim](https://uk.flightaware.com/adsb/piaware/claim)

# Install [360 Radar](http://radar.lowflyingwales.co.uk/installing-and-using-a-dvb-t-dongle-on-a-raspberry-pi/)

# Install [FR24](https://forum.flightradar24.com/forum/radar-forums/flightradar24-feeding-data-to-flightradar24/8950-new-flightradar24-feeding-software-for-raspberry-pie?8908-New-Flightradar24-feeding-software-for-Raspberry-Pie=#post66479)

The recommended way to install the decoder software is through our APT repository in order to simplify future update process.

SSH into your Raspberry Pi and execute this command
```
sudo bash -c "$(wget -O - http://repo.feed.flightradar24.com/install_fr24_rpi.sh)"
```

You will be asked to enter your email address, antenna position and other details.
