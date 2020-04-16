import os
import time
import psutil

# app = '360chrome.exe'



# forever loop
while True:
    app = 'mspaint.exe'
    time.sleep(8)

    for process in psutil.process_iter():
        if process.name() == app:
            process.kill()
            print('process has been killed.')

    # os.chdir('J:/360Chrome/Chrome/Application/')
    # print('path changed.')
    # print(os.getcwd())

    # os.system('J:/360Chrome/Chrome/Application/360chrome.exe')
    # os.system('start mspaint')
    os.system(app)

    print('process restarted.')


