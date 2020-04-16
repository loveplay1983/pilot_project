import os
import time
import psutil

# app = '360chrome.exe'
app = 'mspaint.exe'

# restart comp at specific time
# os.system('at 5:00 shutdown -r -t 1')


# function  for restarting the app
def restart_app(app_name):
    for process in psutil.process_iter():
        if process.name() == app_name:
            process.kill()
    # os.system('J:/360Chrome/Chrome/Application/360chrome.exe')


# forever loop
while True:
    time.sleep(10)
    restart_app(app)
    os.system(app)



