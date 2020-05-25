from event_filter_lib import *

class ClassFilter(QWidget):

    def __init__(self, *args, **kwargs):
        super(ClassFilter, self).__init__(*args, **kwargs)
        self.init_ui()

    def init_ui(self):
        container = QVBoxLayout()

        self.btn_hover = QPushButton('Hover and Click', self)
        self.btn_hover.installEventFilter(self)

        self.btn_d_click = QPushButton('Double Click', self)
        self.btn_d_click.installEventFilter(self)

        container.addWidget(self.btn_hover)
        container.addWidget(self.btn_d_click)
        self.setLayout(container)

        # 通俗点来说就是，正在干的事情太耗时间了，
        # 加了processEvents函数后，会把这个耗时间的东西踢出来，
        # 自己一个去慢慢耗。我继续去监控其他的事件
        qApp.processEvents()


    def eventFilter(self, watch, e):
        if (watch == self.btn_hover):
            if (e.type() == QEvent.Enter): # mouse enter the object
                self.btn_hover.setStyleSheet('background-color: rgb(125, 50, 30);')
            elif(e.type() == QEvent.Leave): # mouse leave the object
                self.btn_hover.setStyleSheet('')
                self.btn_hover.setText('Hover and Click')
            elif(e.type() == QEvent.MouseButtonPress):
                self.btn_hover.setText('Button pressed')
            elif(e.type() == QEvent.MouseButtonRelease):
                self.btn_hover.setText('Button released')

        if (watch == self.btn_d_click):
            if(e.type() == QEvent.Enter):
                self.btn_d_click.setStyleSheet('background-color: rgb(111,111,111);')
            elif(e.type() == QEvent.Leave):
                self.btn_d_click.setStyleSheet('')
                self.btn_d_click.setText('Btn D Click')
            elif(e.type() == QEvent.MouseButtonDblClick):
                self.btn_d_click.setText('D clicked')

        return super().eventFilter(watch, e)  # Making sure the evnet filter runs correctly





if __name__ == '__main__':
    app = QApplication(argv)
    class_filter = ClassFilter()
    class_filter.show()
    exit(app.exec_())