import os
import urllib.request

modules = [
    'datetime',
    'win10toast'

]
import time

print ('TO CREATE A DESKTOP SHORTCUT, MAKE SURE TO RUN AS ADMINISTRSTOR. WINDOWS REQUIRES ADMIN TO CREATE SHORTCUTS. WITHOUT AADMINISTRATOR, EVERYTHING SHOULD STILL WORK AS NORMAL EXCEPT WITHOUT A DESKTOP SHORTCUT. YOU CAN CREATE A SHORTCUT TO "C:\\Bedrock\\ui2.py" MANUALLY IF YOU WANT.')
time.sleep(10)

for i in modules:
    os.system(f'pip install {i}')

try:
    os.mkdir('C:\Bedrock')
except:
    print('error creating directory: "C:\Bedrock"')
    import getpass
username = getpass.getuser()

# Define the URL and file path
url = 'https://github.com/CreepyTnt/Bedrock-Launcher/raw/main/bedrock_startup.py'
file_path = 'C:\Bedrock\startup.py'

# Download the file and save it to the specified path
urllib.request.urlretrieve(url, file_path)

url = 'https://github.com/CreepyTnt/Bedrock-Launcher/raw/main/bedrock_startup.py'
try:
    file_path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\BedrockLauncherBackups.pyw'

    # Download the file and save it to the specified path
    urllib.request.urlretrieve(url, file_path)
except:
    print ('error running backups on startup. try running as sudo/aadmin. the installation should continue as normal. to manually set up backups, visit my github repo.')


# Define the URL and file path
url = 'https://github.com/CreepyTnt/Bedrock-Launcher/raw/main/bedrock_tools.py'
file_path = r'C:\Bedrock\bedrock_tools.py'

# Download the file and save it to the specified path
urllib.request.urlretrieve(url, file_path)

# Define the URL and file path
url = 'https://github.com/CreepyTnt/Bedrock-Launcher/raw/main/ui.pyw'
file_path = 'C:\\Bedrock\\ui.py'

# Download the file and save it to the specified path
urllib.request.urlretrieve(url, file_path)


install_fov = input('would you like to install fov changer (https://github.com/xroix/MCBE-Win10-FOV-Changer) (credit: "xroix")? (y/n)')

if install_fov.lower == 'y' or 'yes':
    url = 'https://www.github.com/XroixHD/MCBE-Win10-FOV-Changer/releases/latest/download/FOV-Changer.zip'
    file_path = r'C:\Bedrock\fov_changer.zip'

    # Download the file and save it to the specified path
    urllib.request.urlretrieve(url, file_path)

    os.system(r'powershell -command "Expand-Archive -Path "C:\Bedrock\fov_changer.zip" -DestinationPath "C:\Bedrock""')

f = open(r'C:\Bedrock\backup_location.txt', 'w')
f.write('C:\\Bedrock\\backup')
f.close()

f = open(r'C:\Bedrock\days_between_backups.txt', 'w')
f.write('0')
f.close()

f = open(r'C:\Bedrock\last_backup.json', 'w')
f.write('[2007, 8, 6]')
f.close()



print (os.system(r'mklink "C:\Users\%USERNAME#\Desktop\Bedrock Launcher.ink" "C:\Bedrock\ui.py"'))
time.sleep(10)

