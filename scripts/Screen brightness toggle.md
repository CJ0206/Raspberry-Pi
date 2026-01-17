# Raspberry Pi DSI Backlight Control  
Automated & Manual Brightness Scheduling (Debian Trixie)

This project provides scripts and systemd timers to automatically turn a DSI‑connected display **off at night** and **on in the morning**, plus manual toggle scripts and optional shell shortcuts.

Designed for Raspberry Pi OS (Debian Trixie) using a DSI panel exposed at:

```
/sys/class/backlight/10-0045/brightness
```

YYou can check if your controls are the same by running:

```
ls /sys/class/backlight
```

Which should return `10-0045`. Any other response will require the eblow code to be amended.

---

## ✨ Features

- Automatically turn screen **off at 23:00**
- Automatically turn screen **on at 07:00**
- Manual toggle scripts:
  - `toggle_off.sh`
  - `toggle_on.sh`
- Optional shell shortcuts:
  - `screenoff`
  - `screenon`

---

## 🖐️ Manual Controls

These scripts let you instantly turn the screen on or off at any time.

---

### 🔌 1. Create a manual “screen off” toggle

```
sudo nano /usr/local/bin/toggle_off.sh
```

Add:
```
#!/bin/bash
echo 0 > /sys/class/backlight/10-0045/brightness
```
Make it executable:
```
sudo chmod +x /usr/local/bin/toggle_off.sh
```

### 💡 2. Create a manual “screen on” toggle
```
sudo nano /usr/local/bin/toggle_on.sh
```
Add:
```
#!/bin/bash
echo 100 > /sys/class/backlight/10-0045/brightness
```
Make it executable:
```
sudo chmod +x /usr/local/bin/toggle_on.sh
```

### 🚀 3. Use the manual toggles
Turn screen off instantly:
```
sudo /usr/local/bin/toggle_off.sh
```

Turn screen on instantly:
```
sudo /usr/local/bin/toggle_on.sh
```

### ⚡ 4. Optional: Add fast shell shortcuts

You can even add aliases if you want super‑fast commands:
```
echo "alias screenoff='sudo /usr/local/bin/toggle_off.sh'" >> ~/.bashrc
echo "alias screenon='sudo /usr/local/bin/toggle_on.sh'" >> ~/.bashrc
source ~/.bashrc
```

Then you can simply type:
```
screenoff
screenon
```

---

## ⏱️ Automated Scheduling
This section creates scripts and systemd timers to automatically turn the screen off at night and on in the morning.

---

### 🌙 5. Create the automated screen‑off script

```
sudo nano /usr/local/bin/screen_off.sh
```

Add:
```
#!/bin/bash
echo 0 > /sys/class/backlight/10-0045/brightness
```

Save and make executable:
```
sudo chmod +x /usr/local/bin/screen_off.sh
```

### ⚙️ 6. Create the screen‑off systemd service

```
sudo nano /etc/systemd/system/screen_off.service
```

Add:
```
[Unit]
Description=Turn off DSI display backlight

[Service]
Type=oneshot
ExecStart=/usr/local/bin/screen_off.sh
```

### ⏰ 7. Create the screen‑off timer (23:00 daily)

```
sudo nano /etc/systemd/system/screen_off.timer
```

Add:
```
[Unit]
Description=Daily screen-off timer

[Timer]
OnCalendar=23:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable it:
```
sudo systemctl enable --now screen_off.timer
```

### 🌅 8. Create the automated screen‑on script

```
sudo nano /usr/local/bin/screen_on.sh
```

Add:
```
#!/bin/bash
echo 100 > /sys/class/backlight/10-0045/brightness
```

Save and make executable:
```
sudo chmod +x /usr/local/bin/screen_on.sh
```

### ⚙️ 9. Create the screen‑on systemd service

```
sudo nano /etc/systemd/system/screen_on.service
```

Add:
```
[Unit]
Description=Turn on DSI display backlight

[Service]
Type=oneshot
ExecStart=/usr/local/bin/screen_on.sh
```

### ⏰ 10. Create the screen‑on timer (07:00 daily)

```
sudo nano /etc/systemd/system/screen_on.timer
```

Add:
```
sudo nano /etc/systemd/system/screen_on.timer
```

Enable and start it:
```
sudo systemctl enable --now screen_on.timer
```

---

## 🎉 Done!
You now have:

screen_off.timer → turns brightness to 0 at 23:00

screen_on.timer → restores brightness to 100 at 07:00

Manual commands (`screenoff`, `screenon`) for instant control
