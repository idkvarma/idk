# Install Ansible on ubuntu system

**Step 1 edit the hosts file after installing ansible on ubuntu system** 

```
cd /etc/ansible
```
```
vi hosts
```

```
[remote]
192.168.1.230   ansible_ssh_user=ubuntu2        ansible_ssh_pass=ubuntu2

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

Once don save the file **:wq**

**Step 2 if you wanna install net-tools on client system try below command**

```
ansible remote -m shell -a "echo 'password' | sudo -S apt install net-tools"
```
**Example below**

```
ansible remote -m shell -a "echo 'ubuntu2' | sudo -S apt install net-tools"
```

-------------------------------------------------------------------------------

# if you wanna install something on remote system by using shell (single line command)

```
ssh -t -p 22 ubuntu2@192.168.1.230 "echo 'password' | sudo -S apt install net-tools"
```
**Example below**
```
ssh -t -p 22 ubuntu2@192.168.1.230 "echo 'ubuntu2' | sudo -S apt install net-tools"
```
