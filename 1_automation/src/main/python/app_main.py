from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
import sys
import os
import pyautogui as auto

from PyQt5.QtGui import (QIcon, QKeySequence)
from PyQt5.QtWidgets import (qApp, QApplication, QSystemTrayIcon, QFileDialog,
                             QAction, QWidget, QMenu, QInputDialog, QShortcut)
from change_mouse_coord import MouseInit


# Context class
class AppContext(ApplicationContext):

    def run(self):
        # self.app.setQuitOnLastWindowClosed(False)
        self.main_win
        return self.app.exec_()

    @cached_property
    def main_win(self):
        return MedicineConfirm(self)

    @cached_property
    def icon_main(self):
        return self.get_resource(os.path.join('images', 'medicine.png'))

    @cached_property
    def icon_action_confirm(self):
        return self.get_resource(os.path.join('images', 'hospital.png'))


# Main class
class MedicineConfirm(QWidget):

    def __init__(self, ctx):
        super(MedicineConfirm, self).__init__()
        self.ctx = ctx  # MedicineConfirm has been wrapped within Appcontext class(see line 11)
        self.init_ui()
        self.x_init = 1080
        self.y_init = 110

    def init_ui(self):
        icon = QIcon(self.ctx.icon_main)
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.setVisible(True)

        # menu
        self.menu_main = QMenu()
        self.menu_confirm = QMenu('发药')
        self.menu_config = QMenu('设置')

        # actions
        self.action_confirm = QAction(QIcon(self.ctx.icon_action_confirm), '发药确认')
        self.action_confirm.triggered.connect(self.auto_confirm)
        self.action_config_locator = QAction('起始坐标定位')
        self.action_config_locator.triggered.connect(self.cursor_init_coord)
        self.action_config_change_mouse_init = QAction('修改鼠标起始位置')
        self.action_config_change_mouse_init.triggered.connect(self.change_cursor_init_coord)

        self.action_close = QAction('退出')
        self.action_close.triggered.connect(QApplication.instance().quit)

        # hook menu and actions
        self.menu_main.addMenu(self.menu_confirm)
        self.menu_main.addMenu(self.menu_config)
        self.menu_confirm.addAction(self.action_confirm)
        self.menu_config.addAction(self.action_config_locator)
        self.menu_config.addAction(self.action_config_change_mouse_init)
        self.menu_main.addAction((self.action_close))

        # put menu on tray
        self.tray.setContextMenu(self.menu_main)

    def auto_confirm(self):
        confirm_num, ok = QInputDialog.getInt(self, '发药确认', '请输入确认次数', min=1)
        if ok:
            for each_confirm in range(confirm_num):
                auto.moveTo(self.x_init, self.y_init)
                auto.click(clicks=2)
                auto.press('enter')
                auto.press('f2')
                auto.press('enter')

    def cursor_init_coord(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open File', '', ('Executable(*.exe);;'
                                                                       'All(*.*)'))
        os.system(fname)

    def change_cursor_init_coord(self):
        x, y, ok = MouseInit.get_coord()
        # print(x, y)
        if ok:
            self.x_init = x
            self.y_init = y


if __name__ == '__main__':
    app_context = AppContext()
    qApp.setQuitOnLastWindowClosed(False)  # Maintain the tray app after sub-window is closed
    exit_code = app_context.run()
    sys.exit(exit_code)
