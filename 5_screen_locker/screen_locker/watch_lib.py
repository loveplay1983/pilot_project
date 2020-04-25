# watch.py
from sys import platform
from time import sleep
from subprocess import run
from ctypes import (Structure, c_uint, c_int, sizeof, windll, byref)
from os.path import abspath, join, dirname
from os import chdir