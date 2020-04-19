# import time
# import win32api
# for i in range(10):
#    print(win32api.GetLastInputInfo())
#    time.sleep


import sys
from ctypes import *

if sys.platform == 'win32':

    class LASTINPUTINFO(Structure):
        _fields_ = [
            ('cbSize', c_uint),
            ('dwTime', c_int),
        ]

    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
            millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            return millis / 1000.0
        else:
            return 0
else:
    def get_idle_duration():
        return 0

if __name__ == '__main__':
    import time

    while True:
        duration = get_idle_duration()
        if duration >= 5.00:
            print('User idle for %.2f seconds.' % duration)
            print('Enter inactive mode')
        else:
            print('Enter active mode')
        time.sleep(3)
