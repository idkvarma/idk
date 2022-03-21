# LINUX

# Ubuntu Terminal autocomplete doesn't work properly

URL: https://askubuntu.com/questions/545540/terminal-autocomplete-doesnt-work-properly

`bash-completion` is a set of bash scripts which enables customized completion for specific commands.

This is not just for files and directories, but also e.g. for the commands. So you type partial of commands and by hitting <kbd>Tab</kbd> we get a auto completion of commands. 

### Installation
**Step 1:** Install bash-completion

    $ sudo apt-get install bash-completion

And some times it works if we re-installed it by the follwing command:

    $ sudo apt-get install --reinstall bash-completion

**Step 2:** Enable bash-completion in your `.bashrc` file

Open your `gedit ~/.bashrc` and if these content doesn't exist there, add them at the end of it and save it.

<!-- language: bash -->

    # enable bash completion in interactive shells
    if ! shopt -oq posix; then
      if [ -f /usr/share/bash-completion/bash_completion ]; then
        . /usr/share/bash-completion/bash_completion
      elif [ -f /etc/bash_completion ]; then
        . /etc/bash_completion
      fi
    fi

**Important:** After changing the file you need to source your ` ~/.bashrc` with `source ~/.bashrc` or reopen your Terminal. It should be fixed now.
