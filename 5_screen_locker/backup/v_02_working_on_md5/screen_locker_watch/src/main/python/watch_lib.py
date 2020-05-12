# watch.py
from sys import platform
from time import sleep
from subprocess import run
from ctypes import (Structure, c_uint, c_int, sizeof, windll, byref)
# fbs libs
from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property

