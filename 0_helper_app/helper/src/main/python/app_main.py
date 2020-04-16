from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainwindow import MainWin


class AppContext(ApplicationContext):
    def run(self):
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def main_window(self):
        return MainWin(self)


if __name__ == '__main__':
    app_context = AppContext()
    exit_code = app_context.run()
    sys.exit(exit_code)
