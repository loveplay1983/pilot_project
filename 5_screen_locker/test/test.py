from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication, Qt, QEvent
# from PyQt5.QtGui import QKeyEvent
import sys
import subprocess
# import pyHook
from pyHook import HookManager, GetKeyState, HookConstants


# import pythoncom


class Test(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.mainwin()
        self.watch_keyboard_mouse()

    ############################################
    ########### listen user action #############
    ############################################
    def onKeyboardEvent(self, event):
        global is_pressed
        # if (event.MessageName != "mouse move"):
        #     print(event.MessageName)
        # print(event.Key)
        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and event.KeyID == HookConstants.VKeyToID('VK_TAB'):
            return False
        # if event.Key.lower() in ['ctrl', 'lwin', 'delete']:
        #     return False
        return True

    def onMouseEvent(self, event):
        global is_clicked
        # print(event.MessageName)
        return True

    def watch_keyboard_mouse(self):
        while True:
            hm = HookManager()

            hm.KeyDown = self.onKeyboardEvent
            hm.HookKeyboard()

            hm.MouseAll = self.onMouseEvent
            hm.HookMouse()

        # listen user action
        if self.onKeyboardEvent:
            print('THE key pressed')
            self.showFullScreen()
        else:
            print('afk')

        if self.onMouseEvent:
            print('THE mouse moved')
        else:
            print('afk')

    #################################################
    ####### show window #############################
    ################################################
    def mainwin(self):

        self.hide()
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # stay on top and frameless
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # stay on top
        self.setWindowFlags(Qt.FramelessWindowHint)  # frameless

        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QCoreApplication.instance().quit)
        btn_quit.setStyleSheet('background-color: red')
        btn_quit.resize(100, 50)
        btn_quit.move(self.width(), self.height())

    #####################################
    ## disable and enable taskmgr #######
    #####################################
    # def disable_taskmgr(self):

    #####################################
    # listen and block user intervention#
    #####################################
    def closeEvent(self, event):
        event.ignore()

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())
