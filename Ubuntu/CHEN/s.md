```
sed -i '3s/^/192.168.2.2     chen.vectorindia.net    chen \n/' /etc/hosts 
apt update 
apt install nis 
apt install net-tools
apt install ssh -y
apt install build-essential 
apt install git -y 
apt install snap -y 
sudo snap install notepadqq 
apt upgrade 
apt install nfs-kernel-server

sed -i 's/NISSERVER=false/NISSERVER=master/g' /etc/default/nis 
sed -i 's/NISCLIENT=true/NISCLIENT=false/g' /etc/default/nis 
sed -e '/0.0.0.0/ s/^#*/#/' -i /etc/ypserv.securenets 
echo '255.255.0.0   192.168.0.0' >> /etc/ypserv.securenets 
/usr/lib/yp/ypinit -m 
systemctl restart rpcbind nis 

#### create user for testing ### 
useradd -m test -s /bin/bash 
passwd test 
make -C /var/yp 
################################ 

 
sed -i '8s/^/Domain = vectorindia.net \n/' /etc/idmapd.conf 
echo '/home *(rw,rsync,no_root_squash)' >> /etc/exports 
systemctl restart nfs-kernel-server 
systemctl enable nfs-kernel-server
systemctl enable rpcbind
systemctl enable nis
sudo ufw disable 
```
