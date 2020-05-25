from PyQt5.QtGui import QPixmap  # image component
from PyQt5.QtWidgets import (
    QWidget, QApplication,  # main component
    QLabel, QPlainTextEdit,  # widget component
    QVBoxLayout  # layout component
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize, QRect

from sys import argv, exit
from os import path


class DragDrop(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):

        # parent widget
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setAcceptDrops(True)
        self.setMaximumSize(QSize(680, 480))

        # plaintextedit
        self.info = QPlainTextEdit(self)
        self.info.setGeometry(QRect(9, 9, 450, 140))
        self.info.setMinimumSize(QSize(0, 140))
        self.info.setAcceptDrops(False)

        self.img = QLabel('', self)
        self.img.setGeometry(QRect(9, 155, 450, 298))
        self.img.setAcceptDrops(False)
        self.img.setScaledContents(True)

        # lyaout
        container = QVBoxLayout()
        container.addWidget(self.info)
        container.addWidget(self.img)
        self.setLayout(container)

    def dragEnterEvent(self, event):
        self.info.clear()
        self.info.appendPlainText('dragEnterEvent事件 mimeData()->formats()')
        for strLine in event.mimeData().formats():
            self.info.appendPlainText(strLine)

        self.info.appendPlainText('\ndragEnterEvent事件 mimeData()->urls()')
        for url in event.mimeData().urls():
            self.info.appendPlainText(url.path())

        if (event.mimeData().hasUrls()):
            file_name = event.mimeData().urls()[0].fileName()
            print(file_name, event.mimeData().urls())
            base_name, ext = path.splitext(file_name)
            ext = ext.upper()
            if (ext == '.PNG'):
                event.acceptProposedAction()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_name = event.mimeData().urls()[0].path()
        print(file_name)
        cnt = len(file_name)

        real_name = file_name[1:cnt]
        pixmap = QPixmap(real_name)
        self.img.setPixmap(pixmap)
        event.accept()


if __name__ == '__main__':
    app = QApplication(argv)
    drag_drop = DragDrop()
    drag_drop.show()
    exit(app.exec_())
