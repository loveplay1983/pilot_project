from sys import argv, exit

from PyQt5.QtWidgets import (
    QApplication,
    QGroupBox, QGridLayout, QHBoxLayout, QVBoxLayout,
    QDialog, QLabel, QSpinBox, QPushButton
)
from PyQt5.QtCore import Qt


class DialogTabelSize(QDialog):

    def __init__(self, row=3, col=5, parent=None):
        super(DialogTabelSize, self).__init__(parent)
        self.ui()
        self.set_init_size(row, col)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

    def ui(self):
        # layout
        self.grp_table_size = QGroupBox('row and column')
        self.layout_main = QHBoxLayout(self)
        self.layout_btns = QVBoxLayout()
        self.layout_row_cols = QGridLayout()

        # widgets
        self.label_row = QLabel('row')
        self.label_col = QLabel('column')
        self.edit_row = QSpinBox()
        self.edit_row.setRange(1, 100)
        self.edit_row.setSingleStep(1)
        # self.edit_row.setMinimum(1)
        # self.edit_row.setMaximum(100)
        self.edit_col = QSpinBox()
        self.edit_col.setRange(1, 100)
        self.edit_col.setSingleStep(1)
        # self.edit_col.setMinimum(1)
        # self.edit_col.setMaximum(100)
        self.btn_yes = QPushButton('Yes')
        self.btn_yes.clicked.connect(self.accept)
        self.btn_no = QPushButton('Cancel')
        self.btn_no.clicked.connect(self.reject)

        # structure
        self.layout_row_cols.addWidget(self.label_row, 0, 0, 1, 1)
        self.layout_row_cols.addWidget(self.label_col, 1, 0, 1, 1)
        self.layout_row_cols.addWidget(self.edit_row, 0, 1, 1, 1)
        self.layout_row_cols.addWidget(self.edit_col, 1, 1, 1, 1)
        self.layout_btns.addWidget(self.btn_yes)
        self.layout_btns.addWidget(self.btn_no)
        self.grp_table_size.setLayout(self.layout_row_cols)
        self.layout_main.addWidget(self.grp_table_size)
        self.layout_main.addLayout(self.layout_btns)

    def set_init_size(self, row_num, col_num):
        self.edit_row.setValue(row_num)
        self.edit_col.setValue(col_num)

    def get_tbl_size(self):
        rows = self.edit_row.value()
        cols = self.edit_col.value()
        return rows, cols

    def __del__(self):
        print('dialog_table_size object has been deleted')

if __name__ == '__main__':
    app = QApplication(argv)
    table_size = DialogTabelSize()
    table_size.show()
    exit(app.exec_())
