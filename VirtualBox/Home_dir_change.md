# Change Home dir

```
echo '#My edit'
hostnamectl set-hostname system11
sudo usermod -l system11 system6
sudo groupmod -n system11 system6
sudo usermod -d /system11 -m system11
echo '#check system11 is present or not in this below line if not chnage oldName to newName'
echo '#system11:x:1000:1000:system11,,,:/system11:/bin/bash'
```

**system11 (system11 is an new user and new home directory name)**

**system6 (system6 is running system username)**
