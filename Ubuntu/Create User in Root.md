# Creating a user directly in the root directory (/)

```
#!/bin/bash

# Check if the script is run with superuser privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root or with sudo."
  exit
fi

# Create user 'labexam' in / directory
useradd -m -d /labexam -s /bin/bash labexam

# Set a password for the user 'labexam'
echo "labexam:password123" | chpasswd

# Print a message indicating successful user creation
echo "User 'labexam' created successfully with password 'password123'."
```

In this modified script, we're creating the user `labexam` with the home directory set to `/labexam`.

Save this script with a `.sh` extension (e.g., `create_labexam_user.sh`) and then you can run it using:

```sudo bash create_labexam_user.sh```
