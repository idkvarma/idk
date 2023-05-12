# Adding Username and passord in hosts file (/etc/ansible/hosts)

```
[remote]
192.168.1.230   ansible_ssh_user=username        ansible_ssh_pass=userpassword

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

# To run the above hosts are ON/OFF, we can run the below command (PING)
```
ansible  remote -m ping
```

# To check the version of kernal, we can run the below commands
```
ansible  remote -m shell -a "uname -a"
```
(or)
```
ansible all -m shell -a "uname -a"
```
