from drag_drop_list import *


class DragDropDemo(QWidget):
    """ Drag and Drop within list items """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.setup_ui()

    def init_ui(self):
        # Layout
        self.vertical_main = QVBoxLayout(self)
        self.horizon_up = QHBoxLayout()
        self.horizon_down = QHBoxLayout()
        self.vertical_objconf = QVBoxLayout()
        self.grid_drag_drop_args = QGridLayout()
        self.vertical_listsource = QVBoxLayout()
        self.vertical_listwidget = QVBoxLayout()
        self.vertical_treewidget = QVBoxLayout()
        self.vertical_tablewidget = QVBoxLayout()

        # Groupbox
        self.grpbox_objconf = QGroupBox('objects')
        self.grpbox_drag_drop_args = QGroupBox('parameters')
        self.grpbox_listsource = QGroupBox('listsource')
        self.grpbox_listwidget = QGroupBox('listwidget')
        self.grpbox_treewidget = QGroupBox('treewidget')
        self.grpbox_tblwidget = QGroupBox('tablewidget')

        # Widgets
        # setup objects
        self.objects_listsrc = QRadioButton('listsource', self.grpbox_objconf)
        self.objects_listwgt = QRadioButton('listwidget', self.grpbox_objconf)
        self.objects_treewgt = QRadioButton('treewidget', self.grpbox_objconf)
        self.objects_tblwgt = QRadioButton('tablewidget', self.grpbox_objconf)

        # setup parameters with gridlayout
        self.para_accept_drop = QCheckBox()
        self.para_accept_drop.setText('accept drops')
        self.drag_enabled = QCheckBox
        self.drag_enabled.setText('drag enabled')
        
    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(argv)
    demo = DragDropDemo()
    demo.show()
    exit(app.exec_())
