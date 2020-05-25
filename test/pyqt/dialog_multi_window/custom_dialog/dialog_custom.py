from sys import argv, exit

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, qApp,
    QLabel, QDialog, QMenuBar, QToolBar, QStatusBar, QAction, QTableView, QDesktopWidget,
)

from PyQt5.QtCore import (
    pyqtSlot, pyqtSignal,
    Qt,
    QItemSelectionModel, QRect,
)

from PyQt5.QtGui import (
    QStandardItemModel,
)

from dialog_table_size import DialogTabelSize
from dialog_table_header import DialogTableHeader
from dialog_table_locate import DialogTableLocate


class DialogMain(QMainWindow):
    cell_index_changed = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.status = QStatusBar()
        self.ini()

    def ini(self):
        self.__dlg_set_headers = None  # Set header status, None initially
        self.ui()
        self.ui_()
        self.model_view()
        self.slots()

    def ui(self):
        # table view
        self.tbl_view = QTableView()

        # menu, toolbar, statusbar, etc...
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        self.tool_bar = QToolBar()
        self.addToolBar(self.tool_bar)
        self.setStatusBar(self.status)

        # actions
        self.action_set_size = QAction('Configure row and col')
        self.action_set_header = QAction('Configure table header')
        self.action_table_locate = QAction('Locate Cell')
        self.action_exit = QAction('Exit')

        # structure
        self.tool_bar.addAction(self.action_set_size)
        self.tool_bar.addAction(self.action_set_header)
        self.tool_bar.addAction(self.action_table_locate)
        self.tool_bar.addAction(self.action_exit)

    def ui_(self):
        """ adding more features such as statusbar, centralwidget"""

        # central widget
        window_frame = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_frame.moveCenter(center_point)
        self.move(window_frame.topLeft())
        self.resize(800, 600)
        self.setCentralWidget(self.tbl_view)

        # statusbar
        self.label_cell_pos = QLabel('Current Cell: ')
        self.label_cell_pos.setMinimumWidth(180)
        self.status.addWidget(self.label_cell_pos)

        self.label_cell_text = QLabel('Current Text: ')
        self.label_cell_text.setMinimumWidth(200)
        self.status.addWidget(self.label_cell_text)

    def model_view(self):
        self.item_model = QStandardItemModel(10, 5, self)
        self.selection_model = QItemSelectionModel(self.item_model)
        self.selection_model.currentChanged.connect(self.do_current_changed)
        self.tbl_view.setModel(self.item_model)
        self.tbl_view.setSelectionModel(self.selection_model)

    def __del__(self):
        print('dialog_custom obj is deleted')

    ##### slots #######
    def slots(self):
        self.action_set_size.triggered.connect(self.set_size_triggered)
        self.action_set_header.triggered.connect(self.set_header_triggered)
        self.action_table_locate.triggered.connect(self.tbl_locate_triggered)
        self.action_exit.triggered.connect(self.exit_triggered)

    def set_size_triggered(self):
        print('table size')
        dlg_tbl_size = DialogTabelSize()
        # initial configuration for table size which comes from the default model value
        dlg_tbl_size.set_init_size(self.item_model.rowCount(),
                                   self.item_model.columnCount())
        ret = dlg_tbl_size.exec_()  # Modal window
        if (ret == QDialog.Accepted):
            # set up the new item_modal rows and cols which comes from the dlg_tbl_size spinbox value
            rows, cols = dlg_tbl_size.get_tbl_size()
            self.item_model.setRowCount(rows)
            self.item_model.setColumnCount(cols)

    def set_header_triggered(self):
        print('table header', self.__dlg_set_headers)
        if (self.__dlg_set_headers == None):
            self.__dlg_set_headers = DialogTableHeader()
        count = len(self.__dlg_set_headers.header_list())
        if (count != self.item_model.columnCount()):
            str_list = []
            for each in range(self.item_model.columnCount()):
                text = str(self.item_model.headerData(each, Qt.Horizontal, Qt.DisplayRole))
                str_list.append(text)  # current headers
            self.__dlg_set_headers.set_header_list(str_list)
        ret = self.__dlg_set_headers.exec_()
        if (ret == QDialog.Accepted):
            str_list2 = self.__dlg_set_headers.header_list()
            self.item_model.setHorizontalHeaderLabels(str_list2)

    def tbl_locate_triggered(self):
        dlg_tbl_locate = DialogTableLocate()

        dlg_tbl_locate.set_spin_range(self.item_model.rowCount(),
                                      self.item_model.columnCount())
        dlg_tbl_locate.change_action_enabled.connect(self.do_set_locate_enabled)
        dlg_tbl_locate.change_cell_text.connect(self.do_set_cell_text)  # tbl_locate to this
        self.cell_index_changed.connect(DialogTableLocate.do_set_spin_value)  # this to tbl_locate
        # dlg_tbl_locate.setAttribute(Qt.WA_DeleteOnClose)  # Clean up the dialog automatically
        dlg_tbl_locate.exec_()  # None Modal window

    def do_current_changed(self, cur, pre):
        """ change happens from main dialog to locate dialog """
        if (cur != None):
            self.label_cell_pos.setText('Cell: {}row, {}col'.format(cur.row(), cur.column()))
            item = self.item_model.itemFromIndex((cur))
            self.label_cell_text.setText('Data: ' + item.text())
            # self.cell_index_changed.emit(cur.row(), cur.col())

    def do_set_locate_enabled(self, enable):
        self.action_table_locate.setEnabled(enable)

    def do_set_cell_text(self, row, col, text):
        index = self.item_model.index(row, col)
        self.selection_model.clearSelection()
        self.selection_model.setCurrentIndex(index, QItemSelectionModel.Select)
        self.item_model.setData(index, text, Qt.DisplayRole)

    def exit_triggered(self):
        qApp.instance().quit()


if __name__ == '__main__':
    app = QApplication(argv)
    dialog_main = DialogMain()
    dialog_main.show()
    exit(app.exec_())
