### Instructions on how to install [dump1090-multability fork](https://github.com/mutability/dump1090)

Add dump1090-multability into repository list:

    wget https://github.com/mutability/mutability-repo/releases/download/v0.1.1/mutability-repo_0.1.1_armhf.deb
    sudo dpkg -i mutability-repo_0.1.1_armhf.deb

Update and install required packages:

    sudo apt-get update && sudo apt-get install dump1090-mutability

Configure dump1090-multability:

    sudo dpkg-reconfigure dump1090-mutability

Additional arguements:

    --quiet --net --net-ro-size 500 --net-ro-rate 5 --net-beast --mlat --no-fix --modeac

Install webserver integration

    sudo apt-get install lighttpd && sudo lighty-enable-mod dump1090

As the key to install dump1090-multability is out of date I removed it to stop getting the error messages every time I update.

Remove outdated key:

    sudo apt-key del 1495751596
    
Remove dump1090-multability from the repository list:

    sudo rm -r /etc/apt/sources.list.d/mutability.list
    sudo apt-get clean
    sudo apt-get autoclean
    sudo apt-get remove
    sudo apt-get autoremove

Update the system:

    sudto apt-get update
    sudo apt-get upgrade
    sudo apt-get dist-upgrade

