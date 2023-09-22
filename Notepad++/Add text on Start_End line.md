# Add Text at Start and End of Each Line Notepad++

Follow these steps:

1. Press `Ctrl+H` to bring up the Find/Replace Dialog.
2. Choose the `Regular expression` option near the bottom of the dialog.

To add a word, such as `test`, at the beginning of each line:

1. Type `^` in the `Find what` textbox
2. Type `test` in the `Replace` with textbox
3. Place cursor in the first line of the file to ensure all lines are affected
4. Click `Replace` All button

To add a word, such as `test`, at the end of each line:

1. Type `$` in the `Find wha`t textbox
2. Type `test` in the `Replace with` textbox
3. Place cursor in the first line of the file to ensure all lines are affected
4. Click `Replace` All button


# Delete all lines starting/ends with # or ; in Notepad++

Find what: ```.*%.*```

Replace with: ```empty```

```tick``` ```Wrap around``` option

```Regual expression``` make it ```tick``` and ```match line``` as ```untick```
