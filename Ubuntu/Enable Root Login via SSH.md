# Enable root login over SSH
1. Login to your server as root.
2. As the root user, edit the sshd_config file found in /etc/ssh/sshd_config:
`vim /etc/ssh/sshd_config`
3. Add the following line to the file, you can add it anywhere but it’s good practice to find the block about authentication and add it there.
`PermitRootLogin yes`
4. Save and exit the file.
5. Restart the SSH server:
`systemctl restart sshd` or `service sshd restart`
