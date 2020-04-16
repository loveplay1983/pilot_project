from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QAbstractItemView, QMessageBox, QDialog,
                             QStatusBar)

from PyQt5.QtCore import pyqtSlot, Qt, QItemSelectionModel, QModelIndex

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlRecord, QSqlQuery

from ui_mainwindow import Ui_MainWindow

######################## DataBase Login info #################################
if False:
    SERVER_NAME = '2SHT10DXY4OQ4VQ\XUANDB'
    DATABASE_NAME = 'AdventureWorksLT2008R2'
    USER_NAME = 'sa'
    PASSWD = 'pgjdcwn040506'

if True:
    SERVER_NAME = 'EAHIS'
    DATABASE_NAME = 'zjyy'
    USER_NAME = 'ssa'
    PASSWD = '20130111'


class MainWin(QMainWindow):
    """ Main window for this application """

    def __init__(self, parent=None):
        """ Main window entry """

        ###################### Init main window  ########################
        super().__init__(parent=None)  # Calling super class init function

        ########################  Ui init   #############################
        self.parent = parent
        self.ui = Ui_MainWindow()  # Create Ui Mainwindow instance
        self.ui.setupUi(self)  # Set up Ui interface

        ##########################   UI  ################################
        self.ui.unreg_grpbox.hide()  # Hide unreg window at the beginning
        # # tableView property
        # self.ui.unreg_view.setAlternatingRowColors(True)
        # self.ui.unreg_view.verticalHeader().setDefaultSectionSize(30)
        # self.ui.unreg_view.horizontalHeader().setDefaultSectionSize(60)

        ##########################  Logic structure  ################################
        self.ui.menu_db_unreg.triggered.connect(self.unreg_ui_show)  # show the unregistration ui
        self.ui.menu_db_quit.triggered.connect(self.close)  # Quit the whole program
        self.ui.menu_help_about.triggered.connect(self.hide_main_open_about)
        self.ui.unreg_search.clicked.connect(self.clinic_records)
        self.ui.unreg_modification.clicked.connect(self.clinic_records_deletion)


    ##########################  Logic details  ################################
    def unreg_ui_show(self):
        """ Show the unreg window """
        self.ui.unreg_grpbox.show()
        self.setCentralWidget(self.ui.unreg_grpbox)  # Centering the tableView

    # The above code can also be replaced by the following lines
    # @pyqtSlot()
    # def on_menu_db_unreg_triggered(self):
    #     self.ui.unreg_grpbox.show()

    # ################################  Unreg start  #################################################
    # Search and view clinic records
    def clinic_records(self):
        """ View patient clinic records"""
        # {{}} turns "SQL Server" to a string value
        # {} takes the variable that's defined above
        conn_string = f'DRIVER={{SQL Server}}; \
                            SERVER={SERVER_NAME}; \
                            DATABASE={DATABASE_NAME}'

        self.db = QSqlDatabase.addDatabase('QODBC')
        self.db.setDatabaseName(conn_string)
        self.db.setUserName(USER_NAME)
        self.db.setPassword(PASSWD)

        if self.db.open():
            self.__open_table()
            self.statusBar().showMessage('退费处理中......')
        else:
            QMessageBox.warning(self, '错误', '打开数据库失败')

    # Open table
    def __open_table(self):
        """ Open the table view of clinic patient records """
        self.query_model = QSqlQueryModel(self)
        self.query_model.setQuery('''
                                  SELECT zdk.id as ID, bm.bmm as 科别, zdk.jzysh as 医生号, 
                                         zdk.zlsj as 时间, zdk.zyh as 就诊号
                                  FROM   dbo.bazdk as zdk, dbo.zd_bm as bm
                                  WHERE  zdk.zyh = {}
                                  AND    zdk.mzkb=bm.bmh 
                                  AND    zdk.zlsj >= CONVERT(VARCHAR(10),GETDATE(),120)
                                  ORDER BY zdk.zlsj DESC'''.format(self.ui.unreg_input.text()))

        # TO DO  - add more details of filter or error message
        ########### for example if user input is not a number or correct data type

        # if (self.ui.unreg_input.text()

        if self.query_model.lastError().isValid():
            QMessageBox.critical(self, '错误', '数据查询出错, 出错信息:\n' + self.query_model.lastError().text())
            return

        self.ui.statusbar.showMessage('记录条数：{}'.format(self.query_model.rowCount()))

        ## Columns
        self.query_model.setHeaderData(0, Qt.Horizontal, 'ID')
        self.query_model.setHeaderData(1, Qt.Horizontal, '科别')
        self.query_model.setHeaderData(2, Qt.Horizontal, '医生号')
        self.query_model.setHeaderData(3, Qt.Horizontal, '时间')
        self.query_model.setHeaderData(4, Qt.Horizontal, '就诊号')

        ## Convert query model to item selectable model
        self.sel_model = QItemSelectionModel(self.query_model)

        ## Associate with model
        self.ui.unreg_table_view.setModel(self.query_model)
        self.ui.unreg_table_view.setSelectionModel(self.sel_model)

    def clinic_records_deletion(self):
        """ Modify the view content which you may choose one line of record """
        cur_rec_num = self.sel_model.currentIndex().row()
        cur_rec = self.query_model.record(cur_rec_num)
        if(cur_rec.isEmpty()):
            return

        cur_id = cur_rec.value('id')

        query = QSqlQuery(self.db)
        query.prepare('''UPDATE dbo.bazdk
                         SET jzysh=NULL, zlsj=NULL
                         WHERE id=:patient_id''')
        query.bindValue(':patient_id', cur_id)

        if (query.exec_() == False):
            QMessageBox.critical(self, '出错了', '错误记录出现\n' + query.lastError().text())
        else:
            self.statusBar().showMessage('退号处理完毕')
    # ###################################### Unreg end #######################################

    ##################################### About start############################################
    def hide_main_open_about(self):
        """ Hide main window and show about dialog """
        self.hide()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('帮助程序')
        msg.setInformativeText('常见问题及相关工具等，程序开发学习尝试中......')
        msg.setWindowTitle('关于本程序')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.msg_yes)
        msg.exec_()

    def msg_yes(self):
        self.show()
        self.ui.unreg_grpbox.hide()
    # ###############################   About end  #############################################
