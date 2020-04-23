from PyQt5.QtWidgets import (QApplication, QPushButton, QLabel, QWidget,
                             QFormLayout, QLineEdit, QDialog, QDialogButtonBox)
from PyQt5.QtCore import Qt
import sys


class MouseInit(QDialog):
    """  Mouse coordination init input dialog """

    def __init__(self):
        super(MouseInit, self).__init__()
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                   Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QFormLayout()

        self.coord_x = QLabel('输入X坐标')
        self.coord_y = QLabel('输入Y坐标')

        self.coord_x_input = QLineEdit()
        self.coord_y_input = QLineEdit()

        layout.addRow(self.coord_x, self.coord_x_input)
        layout.addRow(self.coord_y, self.coord_y_input)
        layout.addWidget(buttons)

        self.setLayout(layout)
        self.setWindowTitle('鼠标起始位置设定')
        self.resize(100, 60)

    def change_x(self):
        return int(self.coord_x_input.text())

    def chang_y(self):
        return int(self.coord_y_input.text())

    @staticmethod
    def get_coord(parent=None):
        dialog = MouseInit()
        result = dialog.exec_()
        x = dialog.change_x()
        y = dialog.chang_y()
        return (x, y, result == QDialog.Accepted)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MouseInit()
    main.show()
    sys.exit(app.exec_())
