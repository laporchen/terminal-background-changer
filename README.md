# WTBG
A simple script for changing background of Windows Terminal in wsl.
## Install
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
## Usage

```shell
wtbc
```
This will open a fuzzy finder. Just select an image you want to use.  
Press escape to end the script.
