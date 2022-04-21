## Disable Automatic Updates in Firefox ##

Ubuntu is configured by default to silently download and install security updates, and new Firefox versions are always considered security updates. This is what is happening. So you must do `sudo apt-mark hold firefox` as pointed above, or disable automatic security updates (bad idea).

## How to Install Firefox 83 on Ubuntu / CentOS 8/7 & Fedora 33/32 ##

`apt-get --purge autoremove firefox`

https://yehiweb.com/how-to-install-firefox-83-on-centos-8-7-fedora-33-32/

## Delete Firefox and all it's data: ## 
Thanks are also due to [snap question][1] and its [answers and comments][2]

I think this can be done in six easy steps, **please edit my answer - or tell me to - if it's not complete**: 
 
 Run `type firefox`.  You will either get 

 - `firefox is /usr/bin/firefox` or 
 - `firefox is /snap/bin/firefox`

If you get   

| Output                   | *Firefox* has been installed by |
| --------                     | -------------- |
| `firefox is /usr/bin/firefox`| apt          |
| `firefox is /snap/bin/firefox`   | snap            |

**Apt** and **snap** are ways to install packages. (package managers)
If the answer is *apt*, follow these steps . Steps for *snap* are after it.

**Steps to follow if `apt`**

 1. Run `sudo apt-get purge firefox`  _Unless you are serious about data privacy this step should be enough_

 2. Delete `.mozilla/firefox/` in your home directory, should it still be there

 3. Delete `.macromedia/` and `.adobe` in your home directory, these can contain "Flash Cookies" stored by the browser. The same is true, if applicable, for Silverlight (Moonlight) and other plugins, they can allow websites to store data on your computer.

 4. Delete `/etc/firefox/`, this is where your preferences and user-profiles are stored

 5. Delete `/usr/lib/firefox/` should it still be there

 6. Delete `/usr/lib/firefox-addons/` should it still be there

Mind the periods in front of file- and directory names: They indicate a hidden directory. You can tell your File Browser to show them by pressing <kbd>Ctrl</kbd>+<kbd>H</kbd>.

The 4th and 5th step must be done with superuser privileges. To start a the File Browser as a superuser, press <kbd>Alt</kbd>+<kbd>F2</kbd> and enter `gksu nautilus`. 

Finally, restart your computer to get rid of all temporary files. This should remove all traces of firefox ever being there.

Important:

 - Don't rely on this method if you've got sensitive information to protect! Deleting a file, in most cases, only means deleting a reference to it. The raw data will still be on your hard drive, and the proverbial bond-villain will be able to recover them. I'm only mentioning this *in case* it's applicable to anybody who reads this. The only way to *really* get rid of data is to shred the hard drive to bits.

-----
**Steps to follow if `snap`**

- `sudo snap remove firefox`


  [1]: https://askubuntu.com/q/1204337/707756
  [2]: https://askubuntu.com/a/1204350/707756
