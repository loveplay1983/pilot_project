#############################################################
# TO-DO
# Add QTimer for lock and watch combination
# Try to kill task-mgr every single second
###########################################################

from wall_lib import *


################### context class ########################
class AppContext(ApplicationContext):

    def run(self):
        self.wall_app
        return self.app.exec_()

    @cached_property
    def wall_app(self):
        return Wall(self)

    @cached_property
    def wall_bg(self):
        return self.get_resource(join('img', 'wall_.jpg'))


############### main class ################################
class Wall(QMainWindow):

    def __init__(self, ctx):
        super(Wall, self).__init__()
        self.ctx = ctx
        self.watch_key_mouse()
        self.main_win()

    ############# hook user action (key press and mouse click) ##########################

    def on_keyboard_event(self, e):

        # print(e.Key, e.KeyID, e.ScanCode)  # display the content of the particular keystroke

        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and e.KeyID == HookConstants.VKeyToID('VK_TAB'):
            return False  # disable alt - tab
        if GetKeyState(HookConstants.VKeyToID('VK_MENU')) and e.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            return False  # disable alt - esc
        if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and e.KeyID == HookConstants.VKeyToID('VK_ESCAPE'):
            return False  # disable control - esc (start menu)
        if e.Key == 'Lwin':
            return False  # disable win key (start menu)
        return True

    def watch_key_mouse(self):
        hook_manager = HookManager()
        hook_manager.KeyDown = self.on_keyboard_event
        hook_manager.HookKeyboard()
        self.disable_sys_func()

    ############# main window (wall) ##########################
    def main_win(self):

        # set top window
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # set bg image
        self.image_label = QLabel()
        self.image_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setCentralWidget(self.image_label)
        self.image = QImage()
        if self.image.load(self.ctx.wall_bg):
            self.image_label.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())

        btn_action = QPushButton('出口', self)
        btn_action.clicked.connect(self.user_action)
        btn_action.setStyleSheet('background-color: red')
        btn_action.resize(100, 50)
        btn_action.move(866, 566)
        btn_action.setWindowFlags(Qt.WindowStaysOnTopHint)

        # set topic
        font = QFont()
        font.setPointSize(72)
        font.setBold(True)
        self.bg_label = QLabel('诸暨市人民医院计算机中心', self)
        self.bg_label.setFont(font)
        self.bg_label.setStyleSheet('border: 6px solid black')
        self.bg_label.setGeometry(190, 230, 1520, 260)

        # show window
        self.showFullScreen()
        # self.set_top_level_window()

    ############### call batch files  (disable some system functionality) ###########
    global path
    path = abspath(dirname(__file__))

    def disable_sys_func(self):
        batch_path = join(path, 'batch\disable_sys_func.bat')
        run([batch_path])

    def enable_sys_func(self):
        batch_path = join(path, 'batch\enable_sys_func.bat')
        run([batch_path])

    ############### main window event (pyqt event) ##################################
    def closeEvent(self, e):
        e.ignore()

    ################ user action(main win call back)  ##############################
    def user_action(self):
        # call first validation
        pass_ok = InputPasswd.validation()
        if pass_ok:
            ok = ValidDialog.validation()
            if ok:
                self.enable_sys_func()
                QCoreApplication.instance().quit()

    ################ check windows status ##############################
    def set_top_level_window(self):
        if self.windowState() != Qt.WindowMaximized:
            self.showMaximized()
            self.showNormal()

        else:
            self.showNormal()
            self.showMaximized()

        self.raise_()
        self.activateWindow()

        # hwnd = win32gui.GetForegroundWindow()
        # win32gui.SetWindowPos(hWnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        #                       win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


if __name__ == '__main__':
    app_context = AppContext()
    QApplication.setQuitOnLastWindowClosed(False)
    exit_code = app_context.run()
    exit(exit_code)
