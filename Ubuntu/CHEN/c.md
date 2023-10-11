```
apt update  
apt install vim -y 
apt install g++ -y 
apt install nis -y 
apt install autofs -y  
apt install -y openssh-server python3 perl 
apt install -y gcc manpages manpages-dev freebsd-manpages man2html manpages-posix manpages-posix-dev glibc-doc 
apt install -y virtualbox virtualbox-guest-additions-iso 
sed -i '3s/^/192.168.2.2     ns1 nis-server vectorindia.net \n/' /etc/hosts  
echo 'domain vectorindia.net server ns1' >> /etc/yp.conf  
sed -i '/passwd:/ s/$/ nis/' /etc/nsswitch.conf  
sed -i '/group:/ s/$/ nis/' /etc/nsswitch.conf  
sed -i '/shadow:/ s/$/ nis/' /etc/nsswitch.conf  
sed -i '/hosts:/ s/$/ nis/' /etc/nsswitch.conf  
echo 'session optional pam_mkhomedir.so skel=/etc/skel umask=007' >> /etc/pam.d/common-session  
sed -e '/IPAddressDeny=any/ s/^#*/#/' -i /lib/systemd/system/systemd-logind.service  
echo '192.168.2.2:/home       /home   nfs     defaults        0       0' >> /etc/fstab  
echo '/-      /etc/auto.mount' >> /etc/auto.master  
touch /etc/auto.mount  
echo '/home -fstype=nfs,rw 192.168.2.2:/home/' >> /etc/auto.mount  
sudo ufw disable 
ping 192.168.2.167
#reboot 
```
