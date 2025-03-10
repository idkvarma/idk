# How to Boot Ubuntu 20.04 into Text / Command Console

`Ref URL` [Here](https://ubuntuhandbook.org/index.php/2020/05/boot-ubuntu-20-04-command-console/)


## Switching boot target to text
The procedure is as follows to change into a text mode runlevel under systemd:

Open the terminal application.

For remote Linux servers, use the ssh command.

Find which target unit is used by default:

`systemctl get-default`

To change boot target to the text mode:

`sudo systemctl set-default multi-user.target`

Reboot the system using the reboot command:

`sudo systemctl reboot`

## How to switch boot target to GUI (graphical UI)
Want to revert change boot to GUI instead of console/text mode? Try:

Open the Linux terminal application.

Again, for remote Linux servers, use the ssh command.

Find which target unit is used by default:

`systemctl get-default`

To change boot target to the GUI mode:

`sudo systemctl set-default graphical.target`

Make sure you reboot the Linux box using the reboot command:

`sudo reboot`
