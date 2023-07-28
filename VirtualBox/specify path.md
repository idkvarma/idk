# How to specify a path where the user has to be created.

Below command will create testuser in "/" directory

```
useradd -m -d /testuser -s /bin/bash -p $(openssl passwd -1 'password') testuser
```

Below command will create testuser in "/home/" directory

```
useradd -m -d /home/testuser -s /bin/bash -p $(openssl passwd -1 'password') testuser
```
