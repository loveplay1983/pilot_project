from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication, Qt, QEvent
# from PyQt5.QtGui import QKeyEvent
import sys
import subprocess
# import pyHook
from pyHook import HookManager, GetKeyState, HookConstants
import os


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
        if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and GetKeyState(HookConstants.VKeyToID('VK_MENU')) and \
                event.KeyID == HookConstants.VKeyToID('VK_DELETE'):
            print('ctrl alt delete pressed')
            return False
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
        path = os.path.abspath(os.path.dirname(__file__))
        batch_path = os.path.join(path, 'disable_mgr\disable_taskmgr.bat')
        subprocess.call([batch_path])

    def enable_taskmgr(self):
        path = os.path.abspath(os.path.dirname(__file__))
        batch_path = os.path.join(path, 'disable_mgr\enable_taskmgr.bat')
        subprocess.call([batch_path])

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
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
