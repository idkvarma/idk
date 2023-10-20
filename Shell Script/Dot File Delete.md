# Below script will delete all .* files in present working directory. (dotdelete.sh)

```
#!/bin/bash

# Function to delete hidden files and directories recursively
delete_hidden() {
    for item in "$1"/.*
    do
        if [[ -d "$item" && ! -L "$item" ]] && [[ $item != "$1/." && $item != "$1/.." ]]; then
            rm -rf "$item"
        elif [[ -f "$item" && ! -L "$item" ]]; then
            rm -f "$item"
        fi
    done
}

# Call the function on the current directory
delete_hidden .

# Call the function on subdirectories
for dir in ./*/
do
    delete_hidden "$dir"
done
```
