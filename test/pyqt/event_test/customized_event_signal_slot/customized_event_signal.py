from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent, QFont

from sys import argv, exit

class CustomLabel(QLabel):

    d_clicked = pyqtSignal()  # customized signal

    def mouseDoubleClickEvent(self, e):
        """ mouse double clicked event """
        self.d_clicked.emit()  # [send] double-clicked "signal" [within] a mouse double "clicked event"


class CustomWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 300)
        self.setWindowTitle('Event and Signal')

        custom_label = CustomLabel(self)
        custom_label.setText('click me')
        font = custom_label.font()
        font.setPointSize(20)
        font.setBold(True)
        custom_label.setFont(font)
        size = custom_label.sizeHint()
        custom_label.setGeometry(70, 80, size.width(), size.height())
        custom_label.d_clicked.connect(self.do_d_clicked)  # customized signal

    def do_d_clicked(self):
        print('label is d-clicked')

    def mouseDoubleClickEvent(self, e):
        print('window is d-clicked')

if __name__ == '__main__':
    app =QApplication(argv)
    custom_widget = CustomWidget()
    custom_widget.show()
    exit(app.exec_())

