from wall_lib import *
# from win32gui import FindWindow, ShowWindow

class Wall(QMainWindow):

    def __init__(self, *args, **kw):
        super(Wall, self).__init__(*args, **kw)
        self.main_win()
        self.watch_key_mouse()

    ############# hook user action (key press and mouse click) ##########################

    def on_keyboard_event(self, e):
        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and e.KeyID == HookConstants.VKeyToID('VK_TAB'):
            return False
        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and e.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            return False
        if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and e.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            return False
        if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and e.KeyID == HookConstants.VKeyToID('VK_MENU'):
            print('got it')
        if e.Key == 'Lwin':
            return False

        # print(e.Key, e.KeyID, e.ScanCode)

        return True

    def watch_key_mouse(self):
        hook_manager = HookManager()
        hook_manager.KeyDown = self.on_keyboard_event
        hook_manager.HookKeyboard()

    ############# main window (wall) ##########################
    def main_win(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)

        btn_action = QPushButton('Quit', self)
        btn_action.clicked.connect(self.user_action)
        btn_action.setStyleSheet('background-color: red')
        btn_action.resize(100, 50)
        btn_action.move(self.width(), self.height())

        self.showFullScreen()
        self.disable_mgr()
        # self.disable_win_key()

    ############### disable mgr (effective way of disabling CTRL - ALT - DELETE ) ###########
    global path
    path = abspath(dirname(__file__))

    def disable_mgr(self):
        batch_path = join(path, 'taskmgr\disable_mgr.bat')
        call([batch_path])

    def enable_mgr(self):
        batch_path = join(path, 'taskmgr\enable_mgr.bat')
        call([batch_path])

    ################  disable win key (win32gui) ###############################
    # def disable_win_key(self):
    #     win1 = FindWindow('Button', None)
    #     win2 = FindWindow('Shell_TrayWnd', None)
    #
    #     ShowWindow(win1, 0)
    #     ShowWindow(win2, 0)
    #
    # def enable_win_key(self):
    #     win1 = FindWindow('Button', None)
    #     win2 = FindWindow('Shell_TrayWnd', None)
    #
    #     ShowWindow(win1, 1)
    #     ShowWindow(win2, 1)

    ############ disable win_R (run dialog) #######################
    # https://mos86.com/61823.html

    ############### main window event (pyqt event) ###########
    def closeEvent(self, e):
        e.ignore()

    ################ user action(main win call back)  ##############################
    def user_action(self):
        self.enable_mgr()
        # self.enable_win_key()
        QCoreApplication.instance().quit()






if __name__ == '__main__':
    app = QApplication(argv)
    wall = Wall()
    exit(app.exec_())
