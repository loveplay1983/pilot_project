from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton,
    QSpinBox, QCheckBox, QLabel, QLineEdit, QGridLayout
)
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QEvent


class DialogTableLocate(QDialog):
    # Signals
    change_action_enabled = pyqtSignal(bool)
    change_cell_text = pyqtSignal(int, int, str)

    def __init__(self, parent=None):
        super(DialogTableLocate, self).__init__(parent)
        self.ui()

    def ui(self):
        """ ui configs """

        # main window
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # layout
        self.layout_main = QHBoxLayout(self)
        self.layout_left = QGridLayout()
        self.grp_left = QGroupBox('col, row, num, text config')
        self.layout_right = QVBoxLayout()

        # widgets
        self.label_col = QLabel('col num')
        self.label_row = QLabel('row num')
        self.spin_col = QSpinBox()
        self.spin_col.setMinimum(0)
        self.spin_row = QSpinBox()
        self.spin_row.setMinimum(0)
        self.chk_col = QCheckBox('col increment')
        self.chk_row = QCheckBox('row increment')
        self.label_set_text = QLabel('Set Text')
        self.line_edit_set_text = QLineEdit()
        self.btn_yes = QPushButton('yes')
        self.btn_yes.clicked.connect(self.accept)
        self.btn_no = QPushButton('no')
        self.btn_no.clicked.connect(self.reject)

        # structure
        self.layout_left.addWidget(self.label_col, 0, 0, 1, 1)
        self.layout_left.addWidget(self.spin_col, 0, 1, 1, 1)
        self.layout_left.addWidget(self.chk_col, 0, 2, 1, 1)
        self.layout_left.addWidget(self.label_row, 1, 0, 1, 1)
        self.layout_left.addWidget(self.spin_row, 1, 1, 1, 1)
        self.layout_left.addWidget(self.chk_row, 1, 2, 1, 1)
        self.layout_left.addWidget(self.label_set_text, 2, 0, 1, 1)
        self.layout_left.addWidget(self.line_edit_set_text, 2, 1, 1, 2)
        self.grp_left.setLayout(self.layout_left)

        self.layout_right.addWidget(self.btn_yes)
        self.layout_right.addWidget(self.btn_no)

        self.layout_main.addWidget(self.grp_left)
        self.layout_main.addLayout(self.layout_right)

    def set_spin_range(self, row, col):
        self.spin_row.setMaximum(row - 1)
        self.spin_col.setMaximum(col - 1)

    def showEvent(self, event):
        self.change_action_enabled.emit(False)  # set False when dialog shows
        super().showEvent(event)

    def closeEvent(self, event):
        self.change_action_enabled.emit(True)  # set True when dialog closed
        super().closeEvent(event)

    # slots methods
    def slots(self):
        self.btn_yes.clicked.connect(self.on_btn_yes_clicked)

    @pyqtSlot()
    def on_btn_yes_clicked(self):
        row = self.spin_row.value()  # row index
        col = self.spin_col.value()  # col index
        text = self.line_edit_set_text.text()  # text content

        self.change_cell_text.emit(row, col, text)  # signal emit

        if self.chk_row.isChecked():
            self.spin_row.setValue(1 + self.spin_row.value())  # row increment
        if self.chk_col.isChecked():
            self.spin_col.setValue(1 + self.spin_col.value())  # col increment

    @pyqtSlot(int, int)
    def do_set_spin_value(self, row_n, col_n):
        self.spin_row.setValue(row_n)
        self.spin_col.setValue(col_n)

    def __del__(self):
        print('DialogTableLocate is deleted')


if __name__ == '__main__':
    app = QApplication(argv)
    table_locate = DialogTableLocate()
    table_locate.show()
    exit(app.exec_())
