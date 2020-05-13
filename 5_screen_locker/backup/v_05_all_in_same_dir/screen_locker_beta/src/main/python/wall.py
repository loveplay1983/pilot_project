from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QSizePolicy)
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyHook3 import HookManager, GetKeyState, HookConstants
from os.path import join, abspath, dirname
from sys import exit
from subprocess import run
from passwd_dialog import InputPasswd  # password module
from validation_dialog import ValidDialog  # password module
from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property  # fbs module


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

        self.showFullScreen()

    ############### call batch files  (disable some system functionality) ###########
    global path
    path = abspath(dirname(__file__))

    def disable_sys_func(self):
        batch_path = join(path, 'disable_sys_func.bat')
        print(batch_path)
        run([batch_path])

    def enable_sys_func(self):
        batch_path = join(path, 'enable_sys_func.bat')
        run([batch_path])

    ############### main window event (pyqt event) ##################################
    def closeEvent(self, e):
        e.ignore()

    ################ user action(main win call back)  ##############################
    def user_action(self):
        # call first validation
        pass_ok = InputPasswd.validation()
        if pass_ok:
            # call second valid dialog
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


if __name__ == '__main__':
    app_context = AppContext()
    exit_code = app_context.run()
    exit(exit_code)
