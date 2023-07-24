# Blr-Lab (18.04)

Download the **xp.tar.xz** from OneDrive.

Extract **xp.tar.xz** file & copy the **xp** folder to **/** (root directory)

**Step-1 (run a script as sudo at boot time)**

Create a file **vim /etc/systemd/system/ethtool.service** and copy the below content.

```
[Unit]
Description=ethtool script

[Service]
ExecStart=/script.sh

[Install]
WantedBy=multi-user.target
```

**Step-2 (Disable USB)**

First need to create a file by following the commands.

```
sudo nano /etc/modprobe.d/blacklist.conf
```
In the end of the config file we need to add the following code.
```
blacklist usb_storage
blacklist uas
```
Save and exit from the nano editor. (see the Ref URL for better understanding)

Ref: [URL](https://www.techbeginner.in/2020/01/how-to-disable-usb-storage-in-ubuntu-16-04-18-04-20-04.html) 


**Step-3 (Script.sh file at boot time)**
Create a file in **/** directory **vim /script.sh**

```
#!/bin/bash
chmod 777 -R /xp
sudo modprobe -r uas
sudo rmmod usb_storage
chattr +i /xp
sudo chmod 777 /dev/ttyUSB0
```

```diff
- Note: 
- Reboot the system and try to add **.vbox** file and start working on it.
