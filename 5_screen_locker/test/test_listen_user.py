from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication, Qt
from pyHook import HookManager, GetKeyState, HookConstants
from ctypes import *
import sys
import subprocess
import time

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


class Test(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.mainwin()
        self.watch_keyboard_mouse()

    ############################################
    ########### listen user action #############
    ############################################
    def onKeyboardEvent(self, event):
        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and event.KeyID == HookConstants.VKeyToID('VK_TAB'):
            return False
        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and event.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            return False
        # if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and GetKeyState(HookConstants.VKeyToID('VK_MENU')) and \
        #         event.KeyID == HookConstants.VKeyToID('VK_DELETE'):
        #     print('ctrl alt delete pressed')
        #     return False
        return True

    def watch_keyboard_mouse(self):
        hm = HookManager()
        hm.KeyDown = self.onKeyboardEvent
        hm.HookKeyboard()

    #################################################
    ####### show window #############################
    ################################################
    def mainwin(self):
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # stay on top and frameless
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # stay on top
        self.setWindowFlags(Qt.FramelessWindowHint)  # frameless

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(self.quit_app)
        btn_quit.setStyleSheet('background-color: red')
        btn_quit.resize(100, 50)
        btn_quit.move(self.width(), self.height())

        self.showFullScreen()

        self.disable_taskmgr()

    #####################################
    ## disable and enable taskmgr #######
    #####################################
    def disable_taskmgr(self):
        subprocess.call([r'E:\Applications\5_screen_locker\test\disable_mgr\disable_taskmgr.bat'])

    def enable_taskmgr(self):
        subprocess.call([r'E:\Applications\5_screen_locker\test\disable_mgr\enable_taskmgr.bat'])

    #####################################
    # listen and block user intervention#
    #####################################
    def closeEvent(self, event):
        event.ignore()

    #####################################
    # user interaction#
    #####################################
    def quit_app(self):
        self.enable_taskmgr()
        QCoreApplication.instance().quit()


if __name__ == '__main__':
    while True:
        """
        Wait for user interaction, if more than duration then trigger the subprocess call
        total idle time should be the 'duration + sleep' 
        """
        duration = get_idle_duration()

        if duration >= 10.00:
            subprocess.call([r'E:\Applications\0_helper_app\helper\target\helper\helper.exe'])
        else:
            print('Enter active mode')
        time.sleep(10)
