Remove the old files replacing * with your server number, and follow the instructions on [low flying wales](http://radar.lowflyingwales.co.uk/installing-the-mlat-client-on-a-raspberry-pi-python-3-4/) to install the new feeder:

    cd /etc/default/
    sudo rm -r lfw-mlat-client-rx*
    
Update position in dump1090-multability:

    sudo nano /etc/default/dump1090-mutability

Or run:

    sudo dpkg-reconfigure dump1090-mutability
