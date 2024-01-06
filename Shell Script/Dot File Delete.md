# Below script will delete all .* files in present working directory. (dotdelete.sh)

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
