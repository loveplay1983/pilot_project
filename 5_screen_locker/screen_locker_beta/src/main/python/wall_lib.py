# wall.py
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QSizePolicy, QDesktopWidget)
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyHook3 import HookManager, GetKeyState, HookConstants
from os.path import abspath, join, dirname
from sys import argv, exit
from subprocess import run
# import win32gui
# import win32con
from validation.fixed_pattern.passwd_dialog import InputPasswd
from validation.random_SMS.validation_dialog import ValidDialog
# fbs libs
from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property

