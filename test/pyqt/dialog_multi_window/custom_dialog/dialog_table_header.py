from sys import argv, exit

from PyQt5.QtWidgets import (
    QApplication,
    QGroupBox, QHBoxLayout, QVBoxLayout,
    QDialog, QPushButton, QAbstractItemView, QListView
)
from PyQt5.QtCore import Qt, QStringListModel


class DialogTableHeader(QDialog):

    def __init__(self, parent=None):
        super(DialogTableHeader, self).__init__(parent)
        self.ui()
        self.table_view()

    def ui(self):
        # main window
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

        # layout
        self.layout_main = QHBoxLayout(self)
        self.layout_left = QVBoxLayout()
        self.layout_right = QVBoxLayout()
        self.group_left = QGroupBox('table title')

        # widgets
        self.list_view = QListView()  # Model/View
        self.btn_yes = QPushButton('yes')
        self.btn_yes.clicked.connect(self.accept)
        self.btn_no = QPushButton('no')
        self.btn_no.clicked.connect(self.reject)

        # structure
        self.group_left.setLayout(self.layout_left)
        self.layout_left.addWidget(self.list_view)
        self.layout_right.addWidget(self.btn_yes)
        self.layout_right.addWidget(self.btn_no)
        self.layout_main.addWidget(self.group_left)
        self.layout_main.addLayout(self.layout_right)

    def table_view(self):
        self.__model = QStringListModel()  # Model/View
        self.list_view.setModel(self.__model)
        self.list_view.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_view.setDefaultDropAction(Qt.MoveAction)
        self.list_view.setAlternatingRowColors(True)

    def set_header_list(self, str_list):
        self.__model.setStringList(str_list)

    def header_list(self):
        return self.__model.stringList()

    def __del__(self):
        print('Header obj is deleted.')


if __name__ == '__main__':
    app = QApplication(argv)
    table_header = DialogTableHeader()
    table_header.show()
    exit(app.exec_())
