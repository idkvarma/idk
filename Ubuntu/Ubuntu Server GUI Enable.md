# install a GUI interface on your Ubuntu 18.04 server

```
sudo apt update
sudo apt install tasksel
sudo tasksel
# Select ubuntu desktop
sudo systemctl set-default graphical.target 
sudo reboot

---------------------------------------------------------------------
sudo systemctl set-default graphical.target (GUI mode at start)
sudo systemctl set-default multi-user.target (cmd/text mode at start)
---------------------------------------------------------------------

```
