# wall.py
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QSizePolicy, QDesktopWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyHook3 import HookManager, GetKeyState, HookConstants
from os.path import abspath, join, dirname
from sys import argv, exit
from subprocess import call
from validation.fixed_pattern.passwd_dialog import InputPasswd

from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property

