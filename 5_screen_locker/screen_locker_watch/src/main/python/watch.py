# from watch_lib import *
from sys import platform
from time import sleep
from subprocess import run
from ctypes import (Structure, c_uint, c_int, sizeof, windll, byref)
from os import chdir, getcwd

# from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property

if platform == 'win32':

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

    chdir('c:\screen_locker')
    print(getcwd())

    while True:
        """
        Wait for user interaction, if more than duration then trigger the subprocess call
        total idle time should be the 'duration + sleep' 
        """
        duration = get_idle_duration()

        if duration >= 5:
            run([r'screen_locker.exe'])
        else:
            pass
        sleep(10)
