from watch_lib import *

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

    global idle_time

    while True:
        """
        Wait for user interaction, if more than duration then trigger the subprocess call
        total idle time should be the 'duration + sleep' 
        """
        duration = get_idle_duration()

        if duration >= 5:
            exe_path = r'C:\screen_locker'
            chdir(exe_path)
            run([exe_path+'\screen_locker.exe'])
            # print(exe_path+'\screen_locker.exe')
        else:
            pass
        sleep(10)
