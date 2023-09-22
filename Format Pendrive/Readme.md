Here's the step-by-step guide to formatting a USB drive in both Linux and Windows using the command line, presented in a table format

| Linux                          | Command                                                         |
| ------------------------------ | --------------------------------------------------------------- |
| **Step 1:** Open Terminal          | Open the Terminal using **Ctrl + Alt + T**                          |
| **Step 2:** Identify the Drive     | Use **lsblk** to list available drives                              |
| **Step 3:** Unmount the Drive      | **sudo umount /dev/sdX1** (Replace **X** with the appropriate drive)    |
| **Step 4:** Format the Drive       | **sudo mkfs.vfat /dev/sdX1** (Replace **X** with the appropriate drive) |
| **Step 5:** Eject the Drive        | **sudo eject /dev/sdX** (Replace **X** with the appropriate drive)      |

| windows                          | Command                                                         |
| ------------------------------ | --------------------------------------------------------------- |
| **Step 1:** Open Command Prompt    | Press **Win + R**, type **cmd**, and press Enter                        |
| **Step 2:** List Drives            | **wmic diskdrive list brief**                                       |
| **Step 3:** Select the Drive       | **select disk X **(Replace **X** with the appropriate drive number)     |
| **Step 4:** Clean the Drive        | **clean**                                                           |
| **Step 5:** Create a New Partition | **create partition primary**                                        |
| **Step 6:** Format the Partition   | **format fs=fat32 quick**                                           |
| **Step 7:** Assign a Drive Letter  | **assign letter=V** (Replace **V** with the desired drive letter)       |
| **Step 8:** Exit Diskpart          | Type **exit** and press Enter to exit Diskpart                      |



Remember to replace any placeholders (like X and V) with the actual drive numbers or letters on your system. If you have any further questions or need clarification on any step, feel free to ask!
