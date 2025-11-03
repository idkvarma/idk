````markdown
# 🔑 Reset Forgotten Ubuntu Password in Windows 11 (WSL)

If you installed Ubuntu from the Microsoft Store on Windows 11 and forgot your password — don’t worry!  
You can reset it easily using PowerShell.

---

## 🧭 Step 1: Open PowerShell as Administrator
1. Press the **Start** button.  
2. Type **PowerShell**.  
3. Right-click **Windows PowerShell** → choose **Run as administrator**.

---

## 🐧 Step 2: Find Your Installed Ubuntu Name
Type this command:
```bash
wsl -l -v
````

Example output:

```
  NAME            STATE           VERSION
* Ubuntu          Stopped         2
```

Remember your Ubuntu name (e.g., `Ubuntu`).

---

## 🔒 Step 3: Log In as Root (No Password Needed)

Type this command (replace `Ubuntu` with your distro name if different):

```bash
wsl -d Ubuntu -u root
```

Now you are logged in as **root** — the super admin.

---

## 🧑‍💻 Step 4: Change Your User Password

List all users:

```bash
cat /etc/passwd
```

Look for your username, for example:

```
idk:x:1000:1000:,,,:/home/idk:/bin/bash
```

Then reset your password:

```bash
passwd yourusername
```

Example:

```bash
passwd idk
```

Type your **new password** twice (it will not show while typing — that’s normal).

---

## ✅ Step 5: Exit and Reopen Ubuntu

Type:

```bash
exit
```

Then open **Ubuntu** again from the Start Menu.
Now log in using your **new password** 🎉

---

## ⚠️ Optional: If You Get an Error

If PowerShell says something like “Invalid user” or “Cannot find Ubuntu,”
try checking your exact distro name again using:

```bash
wsl -l -v
```

and use that name in the `-d` part of the command.

---

**Author:** idk
**Purpose:** Help anyone who forgot their Ubuntu WSL password on Windows 11 😊

```

---

Would you like me to **create and give you a downloadable `.md` file** for this too?
```
