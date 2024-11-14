# How to Set Up Static IP on Ubuntu server 18.04

Ref Link: [Link Here](https://devicetests.com/fixing-start-job-running-wait-network-configured-error-ubuntu-server)


```
ubuntu@ubuntu:~$ cat /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  version: 2
  renderer: networkd
  ethernets:
    enp5s0:
      addresses:
        - 172.16.2.32/24
      gateway4: 172.16.2.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4

```

```
sudo netplan generate

sudo netplan apply

```
