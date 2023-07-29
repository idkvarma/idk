#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 path_to_usernames_file"
    exit 1
fi

usernames_file=$1

# Check if the usernames file exists
if [ ! -f "$usernames_file" ]; then
    echo "Error: File '$usernames_file' not found."
    exit 1
fi

# Loop through the list of usernames in the file
while IFS= read -r username; do
    # Create the user with the provided username and password
    useradd -m -s /bin/bash -p p9PhJ2Pf9K94g "$username"
    echo "User '$username' has been created."

    # Set permissions for the home directory
    chmod 700 "/home/$username"
    echo "Permissions set for '/home/$username'."

    # Update NIS database (make command)
    make -C /var/yp
    echo "NIS database updated for '$username'."
done < "$usernames_file"
