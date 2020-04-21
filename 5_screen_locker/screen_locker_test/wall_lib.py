# wall.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication, Qt
from pyHook import HookManager, GetKeyState, HookConstants
from os.path import abspath, join, dirname
from sys import argv, exit
from subprocess import call
