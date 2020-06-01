from ui_main import Ui_MainWindow
from sys import argv, exit
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog,
    QAbstractItemView, QMessageBox, QDataWidgetMapper
)
from PyQt5.QtCore import (
    pyqtSlot, Qt, QItemSelectionModel,
    QModelIndex, QFile, QIODevice, QCoreApplication
)
from PyQt5.QtSql import (QSqlDatabase, QSqlTableModel, QSqlRecord)
from PyQt5.QtGui import QPixmap
from my_delegates import QmyComboBoxDelegate


class MainWindow(QMainWindow):
    """ main window class """

    def __init__(self, parent=None):
        """ Initialize the class """
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.middle_line)
        self.conf_tbl_view()
        self.open_table('employee', 'NO')  # Can be slots for different functionality
        self.act_slots()

    def conf_tbl_view(self):
        """ Configure tableview widget """
        self.ui.tbl_view_show_data.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tbl_view_show_data.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tbl_view_show_data.setAlternatingRowColors(True)
        self.ui.tbl_view_show_data.verticalHeader().setDefaultSectionSize(22)
        self.ui.tbl_view_show_data.horizontalHeader().setDefaultSectionSize(66)

    def __get_db_args(self, db_name):
        """ Return the target database args """
        db_args = {}
        if db_name == 'local':
            db_args['host'] = '2SHT10DXY4OQ4VQ\XUANDB'
            db_args['db'] = 'xuan_test_db'
            db_args['user'] = 'sa'
            db_args['passwd'] = 'pgjdcwn040506'
        elif db_name == 'tj':
            db_args['host'] = 'JDFYHISBAK\ZJRMYY'
            db_args['db'] = 'medical'
            db_args['user'] = 'zjrmyy'
            db_args['passwd'] = 'zjrmyy'
        else:
            pass
        return (db_args['host'], db_args['db'], db_args['user'], db_args['passwd'])

    def __connect_db(self, db_name):
        """ Create database connection """
        host, db, user, passwd = self.__get_db_args(db_name)
        conn_str = f'DRIVER={{SQL Server}};SERVER={host};DATABASE={db}'
        is_db = QSqlDatabase.addDatabase('QODBC')
        is_db.setDatabaseName(conn_str)
        is_db.setUserName(user)
        is_db.setPassword(passwd)
        return is_db

    def __get_fields(self, db_model):
        """ Get the name of all fields """
        empty_record = db_model.record()
        field_index = {}
        for each in range(empty_record.count()):
            field_name = empty_record.fieldName(each)
            self.ui.combo_sort_col_names.addItem(field_name)
            field_index.setdefault(field_name)
            field_index[field_name] = each
        return field_index

    def __create_model(self, db_name, table_name, sort_index):
        """ Generate the sql model for db connection """
        tab_model = QSqlTableModel(self, db_name)
        tab_model.setTable(table_name)
        tab_model.setEditStrategy(QSqlTableModel.OnManualSubmit)  # The modification of data will be submitted manually
        # tab_model.setSort(tab_model.fieldIndex(sort_index), Qt.AscendingOrder)  # Table data display in ascending order
        tab_model.setSort(tab_model.fieldIndex(sort_index), Qt.DescendingOrder)  # Table data display in ascending order

        if (tab_model.select() == False):
            # Query failed
            QMessageBox.critical(self, 'Error Message',
                                 'Open database table failed!\n' + self.tab_model.lastError().text())
            return
        return tab_model

    def open_table(self, table_name, sort_index):
        """ Open the default table """
        self.db = self.__connect_db('local')  # Connect to database
        if self.db.open():
            self.model = self.__create_model(self.db, table_name, sort_index)  # Create database model
            self.field_index = self.__get_fields(self.model)  # Retrieve the fields dictionary

            # Set up table header data
            self.model.setHeaderData(self.field_index['NO'], Qt.Horizontal, 'ID Number')
            self.model.setHeaderData(self.field_index['NAME'], Qt.Horizontal, 'Name')
            self.model.setHeaderData(self.field_index['GENDER'], Qt.Horizontal, 'Gender')
            self.model.setHeaderData(self.field_index['BIRTH'], Qt.Horizontal, 'Birth')
            self.model.setHeaderData(self.field_index['PROVINCE'], Qt.Horizontal, 'Province')
            self.model.setHeaderData(self.field_index['DEPT'], Qt.Horizontal, 'Department')
            self.model.setHeaderData(self.field_index['SALARY'], Qt.Horizontal, 'Salary')
            self.model.setHeaderData(self.field_index['PHOTO'], Qt.Horizontal, 'Photo')
            self.model.setHeaderData(self.field_index['MEMO'], Qt.Horizontal, 'Memo')

            # Set up mapping between table data and display widgets
            self.mapper = QDataWidgetMapper()
            self.mapper.setModel(self.model)
            self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
            self.mapper.addMapping(self.ui.spin_info_id, self.field_index['NO'])
            self.mapper.addMapping(self.ui.lineedit_name, self.field_index['NAME'])
            self.mapper.addMapping(self.ui.combo_info_sex, self.field_index['GENDER'])
            self.mapper.addMapping(self.ui.dateedit_brith_year, self.field_index['BIRTH'])
            self.mapper.addMapping(self.ui.combo_info_birth_addr, self.field_index['PROVINCE'])
            self.mapper.addMapping(self.ui.combo_info_dept, self.field_index['DEPT'])
            self.mapper.addMapping(self.ui.combo_info_salary, self.field_index['SALARY'])
            self.mapper.addMapping(self.ui.textedit_memo, self.field_index['MEMO'])
            self.mapper.toFirst()

            # Set up Selection model for each row of table
            self.sel_model = QItemSelectionModel(self.model)
            self.sel_model.currentChanged.connect(self.act_cur_changed)
            self.sel_model.currentRowChanged.connect(self.act_cur_row_changed)

            # Connect table view and table model
            self.ui.tbl_view_show_data.setModel(self.model)
            self.ui.tbl_view_show_data.setSelectionModel(self.sel_model)
            self.ui.tbl_view_show_data.setColumnHidden(self.field_index['PHOTO'], True)
            self.ui.tbl_view_show_data.setColumnHidden(self.field_index['MEMO'], True)

            # Customized delegates for table data
            sex_list = ['Male', 'Female']
            self.__delegate_sex = QmyComboBoxDelegate()
            self.__delegate_sex.setItems(sex_list, False)  # Link sex list and delegate, not editable
            self.ui.tbl_view_show_data.setItemDelegateForColumn(self.field_index['GENDER'], self.__delegate_sex)
            dept_list = ['CS', 'AI', 'Network', 'Unix', 'Business']
            self.__delegate_dept = QmyComboBoxDelegate()
            self.__delegate_dept.setItems(dept_list, True)  # Link dept list and delegate, editable
            self.ui.tbl_view_show_data.setItemDelegateForColumn(self.field_index['DEPT'], self.__delegate_dept)

            # Enable and Disable actions
            self.ui.act_add.setEnabled(True)
            self.ui.act_insert.setEnabled(True)
            self.ui.act_del.setEnabled(True)
            self.ui.group_sort.setEnabled(True)
        else:
            QMessageBox.warning(self, 'Error', 'Open database failed')

    ###################### Action slots  ##################################
    def act_slots(self):
        self.ui.act_add.triggered.connect(self.act_add)
        self.ui.act_insert.triggered.connect(self.act_insert)
        self.ui.act_del.triggered.connect(self.act_del)
        # self.ui.act_new_photo.triggered.connect(self.act_new_photo)
        # self.ui.act_del_photo.triggered.connect(self.act_del_photo)
        self.ui.act_save.triggered.connect(self.act_save)
        self.ui.act_cancel_change.triggered.connect(self.act_cancel)
        self.ui.act_exit.triggered.connect(QCoreApplication.instance().quit)  # Exit

    def act_add(self):
        self.ui.act_save.setEnabled(True)
        self.ui.act_cancel_change.setEnabled(True)
        self.model.insertRow(self.model.rowCount(), QModelIndex())  # Insert new row after the last line of data
        cur_index = self.model.index(self.model.rowCount() - 1, 0)
        self.sel_model.clearSelection()
        # Set inserted row to the current selection
        self.sel_model.setCurrentIndex(cur_index, QItemSelectionModel.Select)
        cur_row = cur_index.row()
        # self.model.setData(self.model.index(cur_row, self.field_index['NO']),  # field_index['NO'] = 0
        #                    self.model.rowCount())
        self.model.setData(self.model.index(cur_row, self.field_index['GENDER']),
                           'Male')

    def act_insert(self):
        # cur_index = self.ui.tbl_view_show_data.currentIndex()
        self.ui.act_save.setEnabled(True)
        self.ui.act_cancel_change.setEnabled(True)
        cur_index = self.sel_model.currentIndex()
        self.model.insertRow(cur_index.row(), QModelIndex())
        self.sel_model.clearSelection()
        self.sel_model.setCurrentIndex(cur_index, QItemSelectionModel.Select)

    def act_del(self):
        cur_index = self.sel_model.currentIndex()  # Get current row index
        self.model.removeRow(cur_index.row())  # Delete current row by row index

    # def act_new_photo(self):
    #     f_name, filt = QFileDialog.getOpenFileName(self,
    #                                                'Choose image file',
    #                                                '',
    #                                                'image(*.jpg *.png *.gif);;All(*.*)')
    #     if(f_name==''):
    #         return
    #     file = QFile(f_name)
    #     file.open(QIODevice.ReadOnly)
    #     try:
    #         data = file.readAll()
    #     finally:
    #         file.close()
    #
    #     # cur_rec_num = self.sel_model.currentIndex().row()
    #     cur_rec_num = self.ui.tbl_view_show_data.currentIndex().row()
    #     cur_rec = self.model.record(cur_rec_num)
    #     cur_rec.setValue('PHOTO', data)
    #     self.model.setRecord(cur_rec_num, cur_rec)
    #
    #     img = QPixmap()
    #     img.loadFromData(data)
    #     # img_w = self.ui.?.width()
    #       self.ui.?.setPixmap(img.scaledToWidth(img_w))

    def act_del_photo(self):
        pass

    def act_save(self):
        result = self.model.submitAll()
        if (result == False):
            QMessageBox.information(self, 'Info',
                                    'Save data failed! ' + self.model.lastError().text()
                                    )
        else:
            # set save and cancel to False after the data has been saved
            self.ui.act_save.setEnabled(False)
            self.ui.act_cancel_change.setEnabled(False)

    def act_cancel(self):
        self.model.revertAll()
        self.ui.act_save.setEnabled(False)
        self.ui.act_cancel_change.setEnabled(False)

    ################## Sorting and Filtering ###################################
    @pyqtSlot(int)
    def on_combo_sort_col_names_currentIndexChanged(self, index):
        """ Sorting the display of your current table view by the index """
        if self.ui.sort_radio_asc.isChecked():
            self.model.setSort(index, Qt.AscendingOrder)
        else:
            self.model.setSort(index, Qt.DescendingOrder)
        self.model.select()

    @pyqtSlot()
    def on_sort_radio_asc_clicked(self):
        # Same as "SELECT * FROM xxx ORDER BY 'column' "
        self.model.setSort(self.ui.combo_sort_col_names.currentIndex(), Qt.AscendingOrder)
        self.model.select()

    @pyqtSlot()
    def on_sort_radio_desc_clicked(self):
        self.model.setSort(self.ui.combo_sort_col_names.currentIndex(), Qt.DescendingOrder)
        self.model.select()

    @pyqtSlot()
    def on_sort_radio_male_clicked(self):
        # Same as "SELECT * FROM xxx WHERE Gender='Male' "
        self.model.setFilter('GENDER="Male"')

    @pyqtSlot()
    def on_sort_radio_female_clicked(self):
        pass

    @pyqtSlot()
    def on_sort_radio_all_clicked(self):
        pass

    ############################# Customized slots  #####################################
    def act_cur_changed(self):
        pass

    def act_cur_row_changed(self, current, previous):
        self.mapper.setCurrentIndex(current.row())


if __name__ == '__main__':
    app = QApplication(argv)
    main = MainWindow()
    main.show()
    exit(app.exec_())
