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
            return False  # disable alt - tab
        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and e.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            return False  # disable alt - esc
        if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and e.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            return False  # disable control - esc (start menu)
        if e.Key == 'Lwin':
            return False  # disable win key (start menu)
        if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and GetKeyState(HookConstants.VKeyToID('VK_LMENU')) \
                and e.KeyID == HookConstants.VKeyToID('VK_DELETE'):
            return False  # not working ( was going to disable tasmgr or CAD[control alt delete])
        # print(e.Key, e.KeyID, e.ScanCode)  # display the content of the particular keystroke

        return True

    def watch_key_mouse(self):
        hook_manager = HookManager()
        hook_manager.KeyDown = self.on_keyboard_event
        hook_manager.HookKeyboard()

    ############# main window (wall) ##########################
    def main_win(self):

        # set bg image
        if False:
            self.image_label = QLabel()
            self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self.setCentralWidget(self.image_label)
            self.image = QImage()
            if self.image.load('image path'):
                self.image_label.setPixmap(QPixmap.fromImage(self.image))
                self.resize(self.image.width(), self.image.height())

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)

        btn_action = QPushButton('出口', self)
        btn_action.clicked.connect(self.user_action)
        btn_action.setStyleSheet('background-color: red')
        btn_action.resize(100, 50)
        btn_action.move(900, 630)

        # set topic
        font = QFont()
        font.setPointSize(70)
        font.setBold(True)
        self.bg_label = QLabel('诸暨市人民医院计算机中心', self)
        self.bg_label.setFont(font)
        self.bg_label.setStyleSheet('border: 2px solid black')
        self.bg_label.setGeometry(230, 250, 1500, 300)


        self.showFullScreen()
        self.disable_sys_func()

    ############### call batch files  (disable some system functionality) ###########
    global path
    path = abspath(dirname(__file__))

    def disable_sys_func(self):
        batch_path = join(path, 'batch\disable_sys_func.bat')
        call([batch_path])

    def enable_sys_func(self):
        batch_path = join(path, 'batch\enable_sys_func.bat')
        call([batch_path])

    ############### main window event (pyqt event) ##################################
    def closeEvent(self, e):
        e.ignore()

    ################ user action(main win call back)  ##############################
    def user_action(self):
        self.enable_sys_func()
        QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(argv)
    wall = Wall()
    exit(app.exec_())
