sudo git clone https://github.com/KillaMeep/TIDbot.git
cd TIDbot
echo BOT_ID= > .env
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
sudo apt-get install unzip python3-pip xvfb
sudo rm -rf google-chrome-stable_current_amd64.deb
pip install -r requirements.txt
sudo rm -rf requirements.txt
cd utils
sudo wget https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo rm -rf chromedriver_linux64.zip
cd ../..
sudo chmod ugo+rwx TIDbot/
echo Install complete. Edit .env with bot id.
echo Removing installer.
sudo rm -rf inst.sh
