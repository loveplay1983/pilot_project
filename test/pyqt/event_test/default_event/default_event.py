from default_e_lib import *

class DefaultEvent(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init()

    def init(self):
        self.coord = QLabel('hello world', self)
        self.coord.setGeometry(QRect(50, 50, 190, 50))
        self.btn_center = QPushButton('btn_center', self)
        self.btn_center.setGeometry(QRect(50, 150, 190, 50))
        self.btn_move = QPushButton('btn_move', self)
        self.btn_move.setGeometry(QRect(50, 250, 190, 50))

    def event(self, event):
        """ overload superclass event """
        return super().event(event)

    def paintEvent(self, event):
        """ background image """
        painter = QPainter(self)
        pic = QPixmap('qt.png')
        painter.drawPixmap(0, 0, self.width(), self.height(), pic)

    def resizeEvent(self, event):
        """ no matter how you resize your window the btn_move button will always be centered """
        w = self.width()
        h = self.height()

        w_btn_move = self.btn_move.width()  # btn_move button width
        h_btn_move = self.btn_move.height()  # mosueclick button height

        # center btn_move button
        self.btn_move.setGeometry((w - w_btn_move) / 2, (h - h_btn_move) / 2, \
                                  w_btn_move, h_btn_move)

    def closeEvent(self, event):
        dlg_title = 'info'
        dlg_content = 'close event is triggered, quit??'
        default_btn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlg_title, dlg_content, QMessageBox.Yes | QMessageBox.No, \
                                      default_btn)
        if (result == QMessageBox.Yes):
            event.accept()
        else:
            event.ignore()

    def keyReleaseEvent(self, e):
        """ button pos control with A, D, W, S arrow left, right, up and down"""
        rect = self.btn_center.geometry()

        if e.key() in set([Qt.Key_A, Qt.Key_Left]):
            self.btn_center.setGeometry(rect.left() - 20, rect.top(), rect.width(), rect.height())

        elif e.key() in set([Qt.Key_D, Qt.Key_Right]):
            self.btn_center.setGeometry(rect.left() + 20, rect.top(), rect.width(), rect.height())

        elif e.key() in set([Qt.Key_W, Qt.Key_Up]):
            self.btn_center.setGeometry(rect.left(), rect.top() - 20, rect.width(), rect.height())
        elif e.key() in set([Qt.Key_S, Qt.Key_Down]):
            self.btn_center.setGeometry(rect.left(), rect.top() + 20, rect.width(), rect.height())

    def hideEvent(self, event):
        pass

    def showEvent(self, e):
        print('window is available')

    def mousePressEvent(self, e):
        pos = e.pos()       # current mouse coordinate, QPoint

        # pos = e.localPos()  # current mouse coordinate, QPointF
        # pos = e.windowPos() # current mouse coordinate, QpointF
        # pos = e.globalPos() # global coordinate, QPointF
        # pos = e.screenPos() # full screen coordinate, same as globalPos(), QPointF

        # if (e.buttons() and Qt.LeftButton) and (event.buttons() & Qt.RightButton): # press both left and right mouse
        if (e.button() == Qt.LeftButton):
            self.coord.setText('(x, y) = ({}, {})'.format(pos.x(), pos.y()))
            rect = self.coord.geometry()
            self.coord.setGeometry(pos.x(), pos.y(), rect.width(), rect.height())
        super().mousePressEvent(e)


if __name__ == '__main__':
    app = QApplication(argv)
    default_event = DefaultEvent()
    default_event.show()
    exit(app.exec_())
