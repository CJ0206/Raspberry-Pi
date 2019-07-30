### Instructions on how to install [dump1090-multability fork](https://forum.flightradar24.com/threads/10232-How-to-Install-dump1090-mutability_1-15-dev-on-RPi)


Update and install required packages:

    sudo bash -c "$(wget -O - https://raw.githubusercontent.com/abcd567a/dump1090/master/install_dump1090_mut_1.15.sh)"

Configure dump1090-multability:

    sudo dpkg-reconfigure dump1090-mutability

When promplted remove the IP and hit enter:

    127.0.0.1

Additional arguements:

    --quiet --net --net-ro-size 500 --net-ro-rate 5 --net-beast --mlat --no-fix --modeac


Bug fix:

    sudo wget -O /etc/udev/rules.d/rtl-sdr.rules "https://raw.githubusercontent.com/osmocom/rtl-sdr/master/rtl-sdr.rules" 
    
    sudo reboot

Update the system:

    sudto apt-get update
    sudo apt-get upgrade
    sudo apt-get dist-upgrade

