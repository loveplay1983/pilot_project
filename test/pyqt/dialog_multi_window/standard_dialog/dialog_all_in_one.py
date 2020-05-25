from PyQt5.QtWidgets import (
    QPushButton, QPlainTextEdit, QGroupBox, QApplication, QLineEdit,
    QMessageBox, QWidget,
    QDialog, QFileDialog, QColorDialog, QFontDialog, QProgressDialog,
    QInputDialog,
    QGridLayout, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt, pyqtSlot, QDir, QTime, QFile
from PyQt5.QtGui import QPalette, QColor, QFont
from sys import argv, exit
from subprocess import run
from os import system


class MyDialog(QDialog):
    """ Dialog All In One """

    def __init__(self):
        super(MyDialog, self).__init__()
        self.setWindowTitle('standard dialog dmeo')
        self.ui()
        self.logic()

    def ui(self):
        # layout
        self.layout_main = QVBoxLayout(self)
        self.layout_dialog = QGridLayout()
        self.grid_standard_dialog = QGridLayout()
        self.grid_message_dialog = QGridLayout()
        self.grid_standard_input = QGridLayout()
        self.horizon_clear_quit = QHBoxLayout()

        # widgets
        self.grp_standard = QGroupBox('standard')
        self.grp_message = QGroupBox('message')
        self.grp_input = QGroupBox('input')
        self.grp_clear_quit = QGroupBox('leave')

        self.open = QPushButton('open file')
        self.open_m = QPushButton('open files')
        self.open_dir = QPushButton('open current directory')
        self.save_file = QPushButton('save file')
        self.color = QPushButton('change color')
        self.font = QPushButton('change font')
        self.progress_dia = QPushButton('progress dialog')

        self.question = QPushButton('quesetion')
        self.info = QPushButton('info')
        self.warn = QPushButton('warn')
        self.critical = QPushButton('critical')
        self.about = QPushButton('about')
        self.about_ = QPushButton('about QT')

        self.input_str = QPushButton('input str')
        self.input_int = QPushButton('input int')
        self.input_float = QPushButton('input float')
        self.input_items = QPushButton('input with items')

        self.clear = QPushButton('clear cotent')
        self.leave = QPushButton('quit')

        self.text_edit = QPlainTextEdit()

        # structure
        self.grp_standard.setLayout(self.grid_standard_dialog)
        self.grp_message.setLayout(self.grid_message_dialog)
        self.grp_input.setLayout(self.grid_standard_input)
        self.grp_clear_quit.setLayout(self.horizon_clear_quit)

        self.grid_standard_dialog.addWidget(self.open, 0, 0, 1, 1)
        self.grid_standard_dialog.addWidget(self.open_m, 0, 1, 1, 1)
        self.grid_standard_dialog.addWidget(self.open_dir, 1, 0, 1, 1)
        self.grid_standard_dialog.addWidget(self.save_file, 1, 1, 1, 1)
        self.grid_standard_dialog.addWidget(self.color, 2, 0, 1, 1)
        self.grid_standard_dialog.addWidget(self.font, 2, 1, 1, 1)
        self.grid_standard_dialog.addWidget(self.progress_dia, 3, 0, 1, 1)

        self.grid_message_dialog.addWidget(self.question, 0, 0, 1, 1)
        self.grid_message_dialog.addWidget(self.info, 0, 1, 1, 1)
        self.grid_message_dialog.addWidget(self.warn, 1, 0, 1, 1)
        self.grid_message_dialog.addWidget(self.critical, 1, 1, 1, 1)
        self.grid_message_dialog.addWidget(self.about, 2, 0, 1, 1)
        self.grid_message_dialog.addWidget(self.about_, 2, 1, 1, 1)

        self.grid_standard_input.addWidget(self.input_str, 0, 0, 1, 1)
        self.grid_standard_input.addWidget(self.input_int, 0, 1, 1, 1)
        self.grid_standard_input.addWidget(self.input_float, 1, 0, 1, 1)
        self.grid_standard_input.addWidget(self.input_items, 1, 1, 1, 1)

        self.horizon_clear_quit.addWidget(self.clear)
        self.horizon_clear_quit.addWidget(self.leave)

        self.layout_dialog.addWidget(self.grp_standard, 0, 0, 1, 1)
        self.layout_dialog.addWidget(self.grp_message, 0, 1, 1, 1)
        self.layout_dialog.addWidget(self.grp_input, 1, 0, 1, 1)
        self.layout_dialog.addWidget(self.grp_clear_quit, 1, 1, 1, 1)

        self.layout_main.addLayout(self.layout_dialog)
        self.layout_main.addWidget(self.text_edit)

    # logic
    def logic(self):
        self.open.clicked.connect(self.on_open_clicked)
        self.open_m.clicked.connect(self.on_open_m_clicked)
        self.open_dir.clicked.connect(self.on_open_dir_clicked)
        self.save_file.clicked.connect(self.on_save_file_clicked)
        self.color.clicked.connect(self.on_color_clicked)
        self.font.clicked.connect(self.on_font_clicked)
        self.progress_dia.clicked.connect(self.on_progress_dia_clicked)

    # logic details
    def on_open_clicked(self):
        cur_path = QDir.currentPath()
        dlg_title = 'Choose a File'
        filter = 'All(*.*);;Text File(*.txt);;Image File(*.jpg, *.png, *.gif);;Documentation(*.docx, *.xlsx, *.pptx)'
        file_name, filter_used = QFileDialog.getOpenFileName(self, dlg_title, cur_path, filter)
        self.text_edit.appendPlainText(file_name)
        self.text_edit.appendPlainText('\n' + filter_used)

    def on_open_m_clicked(self):
        cur_path = QDir.currentPath()
        dlg_title = 'Choose files'
        filter = 'All(*.*);;Text File(*.txt);;Image File(*.jpg, *.png, *.gif);;Documentation(*.docx, *.xlsx, *.pptx)'
        file_list, filter_used = QFileDialog.getOpenFileNames(self, dlg_title, cur_path, filter)
        for each in range(len(file_list)):
            self.text_edit.appendPlainText(file_list[each])
        self.text_edit.appendPlainText('\n' + filter_used)

    def on_open_dir_clicked(self):
        cur_path = QDir.currentPath()
        dlg_title = 'Choose a Directory'
        selected_dir = QFileDialog.getExistingDirectory(self, dlg_title, cur_path, QFileDialog.ShowDirsOnly)
        self.text_edit.appendPlainText('\n' + selected_dir)

    def on_save_file_clicked(self):
        cur_path = QDir.currentPath()
        dlg_title = 'Save your file'
        filter = 'All(*.*);;Text File(*.txt);;Image File(*.jpg, *.png, *.gif);;Documentation(*.docx, *.xlsx, *.pptx)'
        file_name, filter_used = QFileDialog.getSaveFileName(self, dlg_title, cur_path, filter)
        self.text_edit.appendPlainText(file_name)
        self.text_edit.appendPlainText('\n' + filter_used)

    def on_color_clicked(self):
        pal = self.text_edit.palette()
        cur_text_color = pal.color(QPalette.Text)
        color = QColorDialog.getColor(cur_text_color, self, 'Pick Color')
        if color.isValid():
            pal.setColor(QPalette.Text, color)
            self.text_edit.setPalette(pal)

    def on_font_clicked(self):
        cur_font = self.text_edit.font()
        font, ok = QFontDialog.getFont(cur_font)
        if ok:
            self.text_edit.setFont(font)

    def on_progress_dia_clicked(self):
        labText = "正在复制文件..."  # 文字信息
        btnText = "取消"  # "取消"按钮的标题
        minV = 0
        maxV = 200
        dlgProgress = QProgressDialog(labText, btnText, minV, maxV, self)
        dlgProgress.canceled.connect(self.progress_cancel)  # canceled信号

        dlgProgress.setWindowTitle("复制文件")
        dlgProgress.setWindowModality(Qt.WindowModal)  # 模态对话框

        dlgProgress.setAutoReset(True)  # calls reset() as soon as value() equals maximum()
        dlgProgress.setAutoClose(True)  # whether the dialog gets hidden by reset()

        msCounter = QTime()  # 计时器
        for i in range(minV, maxV + 1):
            dlgProgress.setValue(i)
            # dlgProgress.setLabelText("正在复制文件,第 %d 个"%i)

            msCounter.start()  # 计时器重新开始
            while (msCounter.elapsed() < 30):  # 延时 30ms
                None

            if (dlgProgress.wasCanceled()):  # 中途取消
                break

    def progress_cancel(self):
        self.text_edit.appendPlainText('progress canceled')


if __name__ == '__main__':
    app = QApplication(argv)
    dialog = MyDialog()
    dialog.show()
    exit(app.exec_())
