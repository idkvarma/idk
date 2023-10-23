# How to Set Up Static IP on Ubuntu server 18.04

Ref Link: [Link Here](https://devicetests.com/fixing-start-job-running-wait-network-configured-error-ubuntu-server)


```
ubuntu@ubuntu:~$ cat /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    eno1:
      addresses:
      - 192.168.2.2/16
      gateway4: 192.168.2.1
      nameservers:
        addresses:
        - 192.168.2.1
        - 8.8.8.8
        - 8.8.4.4
        - 1.1.1.1
        search: []
  version: 2
```
