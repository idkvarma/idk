# Default password is "123"

# ./filename.sh user1 user2 user3

```
#!/bin/bash

# Example below
# chmod +x create_users_and_nis.sh
# ./create_users_and_nis.sh user1 user2 user3

if [ $# -eq 0 ]; then
    echo "Usage: $0 username1 [username2 username3 ...]"
    exit 1
fi

# Loop through the list of usernames provided as arguments
for username in "$@"; do
    # Create the user with the provided username and password
    useradd -m -s /bin/bash -p p9PhJ2Pf9K94g "$username"
    echo "User '$username' has been created."

    # Set permissions for the home directory
    chmod 700 "/home/$username"
    echo "Permissions set for '/home/$username'."

    # Update NIS database (make command)
    make -C /var/yp
    echo "NIS database updated for '$username'."
done
```
