# wall.py
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QSizePolicy, QDesktopWidget)
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QImage, QPixmap, QFont
from pyHook import HookManager, GetKeyState, HookConstants
from os.path import abspath, join, dirname
from sys import argv, exit
from subprocess import call
