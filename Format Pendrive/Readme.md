# Linux Disk / Pendrive Formatting Guide

> Be careful while formatting disks.  
> Formatting removes data permanently.

---

# Method1: Simple Format

Use this when:

- pendrive already works
- only want to erase files
- no partition problems

## Unmount Partition

```bash
sudo umount /dev/sdb1
```

## Format as EXT4

```bash
sudo mkfs.ext4 /dev/sdb1
```

Linux only.

Compatibility:

- Linux ✅
- Windows ❌
- macOS ❌

---

## Format as FAT32

```bash
sudo mkfs.fat -F 32 /dev/sdb1
```

Works almost everywhere.

Compatibility:

- Linux ✅
- Windows ✅
- macOS ✅

---

## Format as NTFS

```bash
sudo mkfs.ntfs /dev/sdb1
```

Best for Windows.

Compatibility:

- Linux ✅
- Windows ✅
- macOS ⚠️

---

# Method2 — Full Reset (Complete Clean + Rebuild)

Use this when:

- USB corrupted
- bootable USB issues
- partition table damaged
- want completely fresh disk

---

## Unmount All Partitions

```bash
sudo umount /dev/sdb*
```

Unmounts ALL partitions from the disk.

---

## Remove Filesystem Signatures

```bash
sudo wipefs -a /dev/sdb
```

Removes old filesystem metadata/signatures.

---

## Remove Partition Tables

```bash
sudo sgdisk --zap-all /dev/sdb
```

Removes GPT/MBR partition tables completely.

---

## Create New Partition

```bash
sudo fdisk /dev/sdb
```

Inside `fdisk`:

```text
n
Enter
Enter
Enter
w
```

Meaning:

- `n` → create new partition
- `Enter` → use default settings
- `w` → save and exit

---

# Format the New Partition

## EXT4

```bash
sudo mkfs.ext4 /dev/sdb1
```

Linux only.

Compatibility:

- Linux ✅
- Windows ❌
- macOS ❌

---

## FAT32

```bash
sudo mkfs.fat -F 32 /dev/sdb1
```

Compatibility:

- Linux ✅
- Windows ✅
- macOS ✅

---

## NTFS

```bash
sudo mkfs.ntfs /dev/sdb1
```

Best for Windows.

Compatibility:

- Linux ✅
- Windows ✅
- macOS ⚠️

---

# Important Notes

## Difference Between `/dev/sdb` and `/dev/sdb1`

| Device | Meaning |
|---|---|
| `/dev/sdb` | Whole Disk |
| `/dev/sdb1` | Partition 1 |
| `/dev/sdb2` | Partition 2 |

---

# Safety Warning

Always check disks before formatting:

```bash
lsblk
```

Formatting the wrong disk can destroy your operating system.



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
| **Step 2:** List Drives            | Type **diskpart** new window will open type **list disk**                                       |
| **Step 3:** Select the Drive       | **select disk X** (Replace **X** with the appropriate drive number)     |
| **Step 4:** Clean the Drive        | **clean**                                                           |
| **Step 5:** Create a New Partition | **create partition primary**                                        |
| **Step 6:** Format the Partition   | **format fs=fat32 quick**                                           |
| **Step 7:** Assign a Drive Letter  | **assign letter=V** (Replace **V** with the desired drive letter)       |
| **Step 8:** Exit Diskpart          | Type **exit** and press Enter to exit Diskpart                      |



Remember to replace any placeholders (like X and V) with the actual drive numbers or letters on your system. If you have any further questions or need clarification on any step, feel free to ask!


