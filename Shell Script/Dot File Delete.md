# Below script will delete all .* files, The following script will delete all occurrences of the .* file within the present working directory and its subdirectories.. (dotdelete.sh)

```
#!/bin/bash

echo "Deleting hidden files and directories in the current directory..."
# Delete hidden files in the current directory
find . -type f -name ".*" -delete

echo "Deleting hidden directories in the current directory..."
# Delete hidden directories in the current directory
find . -type d -name ".*" -exec rm -rf {} +

echo "Deletion of hidden files and directories complete."
```

# Below script will delete all a.out files, The following script will delete all occurrences of the a.out file within the present working directory and its subdirectories. (delete_a_files.sh)

```
#!/bin/bash

echo "Deleting 'a.out' files in the current directory and its subdirectories..."
# Delete 'a.out' files recursively
find . -type f -name 'a.out' -delete

echo "Deletion of 'a.out' files complete."
```
