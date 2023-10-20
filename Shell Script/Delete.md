# delete.sh

```
#!/bin/sh
find . -iname "*.pdf" -o -iname "*.doc" -o -iname "*.out" -o -iname "*.docx" -o -iname "*.exe" -o -iname "*.swp" -o -iname "*.pif" -o -iname "*.obj" -o -iname "*.lst" -o -iname "*.plg" -o -iname "*.bak" -o -iname "*.ppt*" -o -iname "*.odt" -o -iname "*.swp" -o -iname "*~" -o -iname "*.uv*" -o -iname "*.i" -o -iname "*.o" -o -iname "*.axp" -o -iname "*.lnp" -o -iname "*.htm*" -o -iname "*.chm" -o -iname "*.crf" -o -iname "*.d" -o -iname "*.tra" -o -iname "*.__i" -o -iname "*.sct" -o -iname "*.dep" -o -iname "*.map" -o -iname "*.s" -o -iname "*.cmd" -o -iname "out" -o -name "*.axf" -type f | while read DIR
do
     rm "${DIR}"
echo rm "${DIR}"

done
```
