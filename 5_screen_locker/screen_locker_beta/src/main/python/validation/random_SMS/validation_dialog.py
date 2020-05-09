from valid_lib import *


class ValidDialog(QDialog):
    """
    Dialog window for second validation which instruct you to
    input the phone number in order to receive the SMS
    """

    def __init__(self, *args, **kwargs):
        super(ValidDialog, self).__init__(*args, **kwargs)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                   Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.accepted.connect(self.reject)

        layout = QFormLayout()

        # first row
        self.label_input = QLabel('验证码手机号')
        self.edit_input = QLineEdit()
        self.edit_input.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit_input.setEchoMode(QLineEdit.Password)
        self.edit_input.setPlaceholderText('189********')
        self.edit_input.installEventFilter(self)
        self.button_sms = QPushButton('发送')
        self.button_sms.clicked.connect(self.send_sms)

        # second row
        self.label_valid = QLabel('输入验证码')
        self.edit_valid = QLineEdit()
        self.edit_valid.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit_valid.setEchoMode(QLineEdit.Password)
        self.edit_valid.setPlaceholderText('请输入您收到的短信验证码')
        self.edit_valid.installEventFilter(self)

        layout.addRow(self.label_input, self.edit_input)
        layout.addWidget(self.button_sms)
        layout.addRow(self.label_valid, self.edit_valid)
        layout.addWidget(buttons)

        self.setLayout(layout)
        self.setWindowTitle('二次验证')
        self.resize(300, 100)

    def eventFilter(self, object, event):
        """ passswd filter with regard to lineedit"""

        if object == (self.edit_input or self.edit_valid):
            if event.type() == QEvent.MouseMove or event.type == QEvent.MouseButtonDblClick:
                return True  # filter out mouse selection
            elif event.type == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True  # filter out keyboard selection, copy, paste, etc..
        return QDialog.eventFilter(self, object, event)

    def send_sms(self):
        """ Send sms to phone """

        # to-do
        # from passwd_sms import ...
        # call the class for sending sms
        # notice the phone number comes from self.edit_input
        # save random pass to local json file
        print(self.edit_input.text())
        send = SendSMS()
        print(type(send))
        send.request_send_sms(phone_num=self.edit_input.text())

    @staticmethod
    def read_code():
        """
        compare the received code on your phone and the code which has been saved
        on the local computer previously (JSON file, uuid_md5 code)

        if dialog_edit_valid.text() == '... valid code....':
        else:....
        """
        # read json file and get the valid code
        pass_path = r'C:\screen_locker\rand_pass\unlock.json'
        code = load(open(pass_path, 'r'))
        return code['rand_pass']

    @staticmethod
    def validation(parent=None):
        dialog = ValidDialog()
        dialog.edit_valid.setFocus()  # setFocus can only be set once the dialog is displayed
        result = dialog.exec_()
        if dialog.edit_valid.text() == dialog.read_code():
            return result == QDialog.Accepted
        else:
            msgBox = QMessageBox(QMessageBox.NoIcon, '提示', '您的验证码有误，请检查后重新输入')
            dialog.edit_valid.clear()
            msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(argv)
    valid_dialog = ValidDialog()
    valid_dialog.show()
    exit(app.exec_())
