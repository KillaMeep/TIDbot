import os
if os.name == 'nt':
    print('Installer built for linux.')
    exit
else:
    os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
    os.system('sudo apt install ./google-chrome-stable_current_amd64.deb')