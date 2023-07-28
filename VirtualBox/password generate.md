
# Generate SHA-512 password hash for the password 'securepassword'

The command openssl passwd -1 'password' generates an MD5-based password hash of the provided password. The -1 flag indicates that the MD5 encryption method should be used. Note that MD5 is considered a weaker encryption method, and more secure options like SHA-256 (-5 flag) or SHA-512 (-6 flag) are recommended.

```
openssl passwd -6 'securepassword'
```
or
```
openssl passwd -6 'password'
```
or
```
openssl passwd -6 '123'
```
