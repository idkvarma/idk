# Rename Username & Home directory 

1.Change Username:

To change the username, you'll need to create a new user with the desired username and then delete the old user. Follow these steps:

`usermod -l newusername oldusername  #Change username`

`usermod -d /home/newusername -m newusername # Move home directory`

2.Change Home Directory Name:

To change the home directory name, you can follow these steps:

`sudo mv /home/oldusername /home/newusername  # Rename home directory`

3.Edit /etc/passwd:

Open the /etc/passwd file in a text editor: `sudo nano /etc/passwd`
