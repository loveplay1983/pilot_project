# coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication, Qt, QEvent
from PyQt5.QtGui import QKeyEvent


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 置顶
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无框窗口
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)  # 退出
        qbtn.resize(70, 30)
        qbtn.move(50, 50)
        self.showFullScreen()  # 窗口最大化且覆盖任务栏

    def closeEvent(self, event):
        """屏蔽ALT+F4"""
        event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
