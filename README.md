# Terminal Background Changer
A simple script for changing background of of terminal in commandline.
## Current Support
* wsl in Windows Terminal
## Install
### wsl in Windows Terminal
Make sure you have these two packages installed
> [fzf](https://github.com/junegunn/fzf#using-linux-package-managers)  
> [wslu](https://wslutiliti.es/wslu/install.html)

```sh
git clone https://github.com/laporchen/wtbc.git
cd wtbc
chmod +x ./wtbc.sh
# move it to /bin for eaiser use
sudo mv ./wtbc.sh /bin/wtbc
```
Add this environment variable to your shell

> WTIMAGEFOLDER="absolute path to the image folder you want to search"


### iTerm2
Requirements
> [fzf](https://github.com/junegunn/fzf#using-linux-package-managers)  
> install python3 packages with requirement.txt in /iterm  
> Enable python API in iTerm2 perference 

```sh
git clone https://github.com/laporchen/wtbc.git
cd wtbc/iterm
## Location suggested in iTerm2 document.
cp ./main.py $HOME/Library/ApplicationSupport/iTerm2/Scripts/changeBackground.py
```
And I just use an alias for it.
```sh
alias cbg="python3 $HOME/Library/ApplicationSupport/iTerm2/Scripts/changeBackground.py"
```
Add this environment variable to your shell

> ITERMIMAGEFOLDER="absolute path to the image folder you want to search"

## Usage

This script will open a fuzzy finder. Just select an image you want to use.  
Press escape to end the script.
