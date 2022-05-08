Remove the old files replacing *360r-mlat-test-svr2* with your server connection file you are using, and follow the instructions on [low flying wales](https://radar.lowflyingwales.co.uk/installing-the-mlat-client-on-a-raspberry-pi/) to install the new feeder:

    cd /etc/default/
    sudo rm -r 360r-mlat-test-svr2
       
Update FR24 position:

    fr24feed --signup

Update position in dump1090-multability:

    sudo dpkg-reconfigure dump1090-mutability

---
You can also edit the dump1090-multability fille directly:

    sudo nano /etc/default/dump1090-mutability 
    
---
To install [360Radar](http://radar.lowflyingwales.co.uk/installing-and-using-a-dvb-t-dongle-on-a-raspberry-pi/).

To install [dump1090-multability](Install%20dump1090-multability%20fork.md). (I've swapped to [FlightAware](https://uk.flightaware.com/adsb/piaware/install) with dump1090-fa instead).

To install [FR24](https://forum.flightradar24.com/threads/8908-New-Flightradar24-feeding-software-for-Raspberry-Pie?p=66479#post66479).

---
To edit the web interface of dump1090-multability, including location/range rings:

    sudo nano /usr/share/dump1090-mutability/html/config.js

My file is [here](/usr/share/dump1090-mutability/html/config.js) with location removed.
