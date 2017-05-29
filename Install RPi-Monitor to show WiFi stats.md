Add RPi-Monitor into repository list: 

    sudo wget http://goo.gl/vewCLL -O /etc/apt/sources.list.d/rpimonitor.list

Install public key to trust RPi-Monitor repository:

    sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 2C0D3C0F 

Update and install RPi-Monitor:

    sudo apt-get update
    sudo apt-get install rpimonitor

Upgrade RPi-Monitor:

    sudo apt-get update
    sudo apt-get upgrade


Update information about upgradable packages:

    sudo /etc/init.d/rpimonitor update
  
Edit network.conf to show wifi only:

    sudo nano /etc/rpimonitor/template/network.conf

Change the file to:

    ########################################################################
    # Graph WLAN
    ########################################################################
    dynamic.17.name=wifi_received
    dynamic.17.source=/sys/class/net/wlan0/statistics/rx_bytes
    dynamic.17.regexp=(.*)
    dynamic.17.postprocess=$1*-1
    dynamic.17.rrd=DERIVE
    
    dynamic.18.name=wifi_send
    dynamic.18.source=/sys/class/net/wlan0/statistics/tx_bytes
    dynamic.18.regexp=(.*)
    dynamic.18.postprocess=
    dynamic.18.rrd=DERIVE
    
    web.status.1.content.9.name=WiFi
    web.status.1.content.9.icon=wifi.png
    web.status.1.content.9.line.1="WiFi Sent: <b>"+KMG(data.wifi_send)+"<i class='icon-arrow-up'></i></b> Received: <b>"+KMG(Math.abs(data.wifi_received)) + "<i class='icon-arrow-down'></i></b>"
    
    web.statistics.1.content.9.name=WiFi
    web.statistics.1.content.9.graph.1=wifi_send
    web.statistics.1.content.9.graph.2=wifi_received
    web.statistics.1.content.9.ds_graph_options.net_send.label=Upload bandwidth (bits)
    web.statistics.1.content.9.ds_graph_options.net_send.lines={ fill: true }
    web.statistics.1.content.9.ds_graph_options.net_send.color="#FF7777"
    web.statistics.1.content.9.ds_graph_options.net_received.label=Download bandwidth (bits)
    web.statistics.1.content.9.ds_graph_options.net_received.lines={ fill: true }
    web.statistics.1.content.9.ds_graph_options.net_received.color="#77FF77"
