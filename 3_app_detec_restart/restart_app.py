import os
import time
import psutil
# import pprint as prt

# count = 0

# app1 = 'SoftWedge.exe'
# app2 = 'notepad.exe'

# os.system('at 5:00 shutdown -r -t 1')

os.system('notepad.exe')


def restart_app(app_name):
    for process in psutil.process_iter():
        if process.name() == app_name:
            process.kill()
    # os.chdir('C:/Program\ Files/Metrologic\ Instruments/SoftWedge/')
    os.system(app_name)

while True:
    # time.sleep(3600)
    time.sleep(5)

    os.system("taskkill /im notepad.exe /f")
    os.system('notepad.exe')
    # restart_app(app2)

    # count += 1
    # print ('loop {} \n--------------------------------------------------------------------'.format(count))
