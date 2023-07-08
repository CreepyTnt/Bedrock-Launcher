# Bedrock-Launcher
A launcher for Minecraft Bedrock on windows that has add-on and world management, and automatic backups. 
Bedrock Launcher is based on [Bedrock tools](https://github.com/CreepyTnt/Bedrock-tools) 

# Bedrock Launcher only works on windows 10/11

# Installation

### Python is required to run Bedrock Launcher. Python isn't pre installed with Windows so you will have to install it from [here](python.org/downloads)
Download and run "Bedrock Launcher Installer.py" as administrator. Without administrator permissions, the installer cannot create a desktop shortcut, however, you can also create a shortcut manually to "C:\Bedrock\ui.py".     
*You will most likely get errors in bright red text, this is perfectly normal. If you get errors and Bedrock Launcher doesn't install properly (or at all) contact me and I will be glad to help! The reason you will get errors in red text is due to the installer installing every package needed, whether it is already installed or not. Some packages that are pre installed with python, for instance, will throw the error.
During installation, you will be prompted to install [fov changer](https://github.com/xroix/MCBE-Win10-FOV-Changer). Fov changer is a free, open source zoom mod for Minecraft Bedrock written in Python. You can use the bedrock launcher to launch fov changer along-side the actuall game. (I did not make fov changer, please report problems with fov changer to [the creator](https://github.com/xroix).

### Automatic Backups
The auto-backup script is already set to run on startup, however, as long as backup frequency is set to 0 (you can change this in the backup tab of the luancher) it will not backup the game. In the backup tab of the launcher, click "auto backup" and choose a folder to back up to and the backup frequency. It is reccomended to store backups in a seperate drive in case something happens to your entire main drive.
