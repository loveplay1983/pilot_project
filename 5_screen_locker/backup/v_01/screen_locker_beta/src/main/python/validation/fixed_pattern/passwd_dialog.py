from dialog_lib import *


class InputPasswd(QDialog):
    """ password dialog with fixed pattern and the symbolic day of month+week """

    def __init__(self, *args, **kwargs):
        super(InputPasswd, self).__init__(*args, **kwargs)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                   Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QFormLayout()

        self.label_input = QLabel('请输入密码')
        self.passwd_input = QLineEdit()
        self.passwd_input.setContextMenuPolicy(Qt.NoContextMenu)
        self.passwd_input.setEchoMode(QLineEdit.Password)
        self.passwd_input.setPlaceholderText('固定组合+约定信号')
        self.passwd_input.installEventFilter(self)  # relates this line to def eventFilter(...)

        layout.addRow(self.label_input, self.passwd_input)
        layout.addWidget(buttons)

        self.setLayout(layout)
        self.setWindowTitle('首次验证')
        self.resize(250, 100)

    def eventFilter(self, object, event):
        """ passswd filter with regard to lineedit"""

        if object == self.passwd_input:
            if event.type() == QEvent.MouseMove or event.type == QEvent.MouseButtonDblClick:
                return True  # filter out mouse selection
            elif event.type == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True  # filter out keyboard selection, copy, paste, etc..
        return QDialog.eventFilter(self, object, event)

    @staticmethod
    def validation(parent=None):
        dialog = InputPasswd()
        dialog.passwd_input.setFocus()  # setFocus can only be set once the dialog is displayed
        result = dialog.exec_()
        if dialog.passwd_input.text() == 'zjrmyy' + strftime('%w') + strftime('%d'):
            return result == QDialog.Accepted
        else:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提示', '您的输入有误，请重新输入')
            dialog.passwd_input.clear()
            msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(argv)
    passwd_dialog = InputPasswd()
    passwd_dialog.show()
    exit(app.exec_())
