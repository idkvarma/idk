# How to Set Up Static IP on Ubuntu server 18.04

Ref Link: [Link Here](https://devicetests.com/fixing-start-job-running-wait-network-configured-error-ubuntu-server)


```
ubuntu@ubuntu:~$ cat /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: false
      addresses:
        - 192.168.2.3/24
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
      routes:
        - to: default
          via: 192.168.2.1

```
