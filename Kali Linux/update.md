# enable fast update on kali linux

got to ` cat /etc/apt/sources.list` file delete everything and paste the below line in the same file.

```
# See https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/
deb https://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware

# Additional line for source packages
# deb-src http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware

```
