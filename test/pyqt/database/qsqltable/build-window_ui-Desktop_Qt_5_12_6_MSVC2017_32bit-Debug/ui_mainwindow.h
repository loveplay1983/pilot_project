/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDateEdit>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableView>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *act_add;
    QAction *act_insert;
    QAction *act_del;
    QAction *act_new_photo;
    QAction *act_del_photo;
    QAction *act_save;
    QAction *act_cancel_change;
    QAction *act_exit;
    QWidget *main_widget;
    QSplitter *middle_line;
    QGroupBox *group_sort;
    QTableView *tbl_view_show_data;
    QFrame *frame;
    QGroupBox *groupBox;
    QLabel *label_sort_col_names;
    QLabel *label_sort_names;
    QRadioButton *sort_radio_asc;
    QRadioButton *sort_radio_male;
    QLabel *label_sort_sex;
    QRadioButton *sort_radio_female;
    QComboBox *combo_sort_col_names;
    QRadioButton *sort_radio_all;
    QLineEdit *lineedit_sort_names;
    QRadioButton *sort_radio_desc;
    QGroupBox *group_info;
    QWidget *widget;
    QGridLayout *layout_grid_info;
    QLabel *label_info_id;
    QPlainTextEdit *textedit_memo;
    QLabel *label_info_memo;
    QComboBox *combo_info_birth_addr;
    QComboBox *combo_info_salary;
    QSpinBox *spin_info_id;
    QComboBox *combo_info_sex;
    QLabel *label_info_name;
    QLabel *label_info_salary;
    QDateEdit *dateedit_brith_year;
    QLabel *label_info_birth_year;
    QLineEdit *lineedit_name;
    QLabel *label_info_sex;
    QLabel *label_info_birth_addr;
    QLabel *label_info_dept;
    QComboBox *combo_info_dept;
    QMenuBar *menubar;
    QStatusBar *statusbar;
    QToolBar *toolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(976, 644);
        act_add = new QAction(MainWindow);
        act_add->setObjectName(QString::fromUtf8("act_add"));
        act_insert = new QAction(MainWindow);
        act_insert->setObjectName(QString::fromUtf8("act_insert"));
        act_del = new QAction(MainWindow);
        act_del->setObjectName(QString::fromUtf8("act_del"));
        act_new_photo = new QAction(MainWindow);
        act_new_photo->setObjectName(QString::fromUtf8("act_new_photo"));
        act_del_photo = new QAction(MainWindow);
        act_del_photo->setObjectName(QString::fromUtf8("act_del_photo"));
        act_save = new QAction(MainWindow);
        act_save->setObjectName(QString::fromUtf8("act_save"));
        act_cancel_change = new QAction(MainWindow);
        act_cancel_change->setObjectName(QString::fromUtf8("act_cancel_change"));
        act_exit = new QAction(MainWindow);
        act_exit->setObjectName(QString::fromUtf8("act_exit"));
        main_widget = new QWidget(MainWindow);
        main_widget->setObjectName(QString::fromUtf8("main_widget"));
        middle_line = new QSplitter(main_widget);
        middle_line->setObjectName(QString::fromUtf8("middle_line"));
        middle_line->setGeometry(QRect(10, 10, 921, 531));
        middle_line->setOrientation(Qt::Horizontal);
        group_sort = new QGroupBox(middle_line);
        group_sort->setObjectName(QString::fromUtf8("group_sort"));
        tbl_view_show_data = new QTableView(group_sort);
        tbl_view_show_data->setObjectName(QString::fromUtf8("tbl_view_show_data"));
        tbl_view_show_data->setGeometry(QRect(10, 210, 421, 331));
        frame = new QFrame(group_sort);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(10, 20, 421, 171));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        groupBox = new QGroupBox(frame);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(0, 0, 431, 181));
        label_sort_col_names = new QLabel(groupBox);
        label_sort_col_names->setObjectName(QString::fromUtf8("label_sort_col_names"));
        label_sort_col_names->setGeometry(QRect(20, 20, 72, 18));
        label_sort_names = new QLabel(groupBox);
        label_sort_names->setObjectName(QString::fromUtf8("label_sort_names"));
        label_sort_names->setGeometry(QRect(20, 120, 151, 16));
        sort_radio_asc = new QRadioButton(groupBox);
        sort_radio_asc->setObjectName(QString::fromUtf8("sort_radio_asc"));
        sort_radio_asc->setGeometry(QRect(180, 51, 51, 19));
        sort_radio_male = new QRadioButton(groupBox);
        sort_radio_male->setObjectName(QString::fromUtf8("sort_radio_male"));
        sort_radio_male->setGeometry(QRect(130, 80, 61, 19));
        label_sort_sex = new QLabel(groupBox);
        label_sort_sex->setObjectName(QString::fromUtf8("label_sort_sex"));
        label_sort_sex->setGeometry(QRect(20, 80, 101, 16));
        sort_radio_female = new QRadioButton(groupBox);
        sort_radio_female->setObjectName(QString::fromUtf8("sort_radio_female"));
        sort_radio_female->setGeometry(QRect(220, 80, 81, 19));
        combo_sort_col_names = new QComboBox(groupBox);
        combo_sort_col_names->setObjectName(QString::fromUtf8("combo_sort_col_names"));
        combo_sort_col_names->setGeometry(QRect(130, 20, 261, 24));
        sort_radio_all = new QRadioButton(groupBox);
        sort_radio_all->setObjectName(QString::fromUtf8("sort_radio_all"));
        sort_radio_all->setGeometry(QRect(330, 80, 81, 19));
        lineedit_sort_names = new QLineEdit(groupBox);
        lineedit_sort_names->setObjectName(QString::fromUtf8("lineedit_sort_names"));
        lineedit_sort_names->setGeometry(QRect(130, 120, 261, 21));
        sort_radio_desc = new QRadioButton(groupBox);
        sort_radio_desc->setObjectName(QString::fromUtf8("sort_radio_desc"));
        sort_radio_desc->setGeometry(QRect(270, 51, 59, 19));
        middle_line->addWidget(group_sort);
        group_info = new QGroupBox(middle_line);
        group_info->setObjectName(QString::fromUtf8("group_info"));
        widget = new QWidget(group_info);
        widget->setObjectName(QString::fromUtf8("widget"));
        widget->setGeometry(QRect(30, 30, 411, 481));
        layout_grid_info = new QGridLayout(widget);
        layout_grid_info->setObjectName(QString::fromUtf8("layout_grid_info"));
        layout_grid_info->setContentsMargins(0, 0, 0, 0);
        label_info_id = new QLabel(widget);
        label_info_id->setObjectName(QString::fromUtf8("label_info_id"));
        label_info_id->setLayoutDirection(Qt::LeftToRight);
        label_info_id->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_id, 0, 0, 1, 1);

        textedit_memo = new QPlainTextEdit(widget);
        textedit_memo->setObjectName(QString::fromUtf8("textedit_memo"));

        layout_grid_info->addWidget(textedit_memo, 9, 1, 1, 2);

        label_info_memo = new QLabel(widget);
        label_info_memo->setObjectName(QString::fromUtf8("label_info_memo"));
        label_info_memo->setLayoutDirection(Qt::LeftToRight);
        label_info_memo->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_memo, 9, 0, 1, 1);

        combo_info_birth_addr = new QComboBox(widget);
        combo_info_birth_addr->setObjectName(QString::fromUtf8("combo_info_birth_addr"));

        layout_grid_info->addWidget(combo_info_birth_addr, 4, 1, 1, 2);

        combo_info_salary = new QComboBox(widget);
        combo_info_salary->setObjectName(QString::fromUtf8("combo_info_salary"));

        layout_grid_info->addWidget(combo_info_salary, 8, 1, 1, 2);

        spin_info_id = new QSpinBox(widget);
        spin_info_id->setObjectName(QString::fromUtf8("spin_info_id"));

        layout_grid_info->addWidget(spin_info_id, 0, 1, 1, 2);

        combo_info_sex = new QComboBox(widget);
        combo_info_sex->setObjectName(QString::fromUtf8("combo_info_sex"));

        layout_grid_info->addWidget(combo_info_sex, 2, 1, 1, 2);

        label_info_name = new QLabel(widget);
        label_info_name->setObjectName(QString::fromUtf8("label_info_name"));
        label_info_name->setLayoutDirection(Qt::LeftToRight);
        label_info_name->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_name, 1, 0, 1, 1);

        label_info_salary = new QLabel(widget);
        label_info_salary->setObjectName(QString::fromUtf8("label_info_salary"));
        label_info_salary->setLayoutDirection(Qt::LeftToRight);
        label_info_salary->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_salary, 7, 0, 2, 1);

        dateedit_brith_year = new QDateEdit(widget);
        dateedit_brith_year->setObjectName(QString::fromUtf8("dateedit_brith_year"));
        dateedit_brith_year->setCalendarPopup(true);

        layout_grid_info->addWidget(dateedit_brith_year, 3, 1, 1, 2);

        label_info_birth_year = new QLabel(widget);
        label_info_birth_year->setObjectName(QString::fromUtf8("label_info_birth_year"));
        label_info_birth_year->setLayoutDirection(Qt::LeftToRight);
        label_info_birth_year->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_birth_year, 3, 0, 1, 1);

        lineedit_name = new QLineEdit(widget);
        lineedit_name->setObjectName(QString::fromUtf8("lineedit_name"));

        layout_grid_info->addWidget(lineedit_name, 1, 1, 1, 2);

        label_info_sex = new QLabel(widget);
        label_info_sex->setObjectName(QString::fromUtf8("label_info_sex"));
        label_info_sex->setLayoutDirection(Qt::LeftToRight);
        label_info_sex->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_sex, 2, 0, 1, 1);

        label_info_birth_addr = new QLabel(widget);
        label_info_birth_addr->setObjectName(QString::fromUtf8("label_info_birth_addr"));
        label_info_birth_addr->setLayoutDirection(Qt::LeftToRight);
        label_info_birth_addr->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_birth_addr, 4, 0, 1, 1);

        label_info_dept = new QLabel(widget);
        label_info_dept->setObjectName(QString::fromUtf8("label_info_dept"));
        label_info_dept->setLayoutDirection(Qt::LeftToRight);
        label_info_dept->setAlignment(Qt::AlignCenter);

        layout_grid_info->addWidget(label_info_dept, 5, 0, 1, 1);

        combo_info_dept = new QComboBox(widget);
        combo_info_dept->setObjectName(QString::fromUtf8("combo_info_dept"));

        layout_grid_info->addWidget(combo_info_dept, 5, 1, 1, 2);

        middle_line->addWidget(group_info);
        MainWindow->setCentralWidget(main_widget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 976, 26));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);
        toolBar = new QToolBar(MainWindow);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, toolBar);

        toolBar->addAction(act_add);
        toolBar->addAction(act_insert);
        toolBar->addAction(act_del);
        toolBar->addSeparator();
        toolBar->addAction(act_new_photo);
        toolBar->addAction(act_del_photo);
        toolBar->addSeparator();
        toolBar->addAction(act_save);
        toolBar->addAction(act_cancel_change);
        toolBar->addSeparator();
        toolBar->addAction(act_exit);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        act_add->setText(QApplication::translate("MainWindow", "Add", nullptr));
#ifndef QT_NO_TOOLTIP
        act_add->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>Add new line of data</p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        act_insert->setText(QApplication::translate("MainWindow", "insert", nullptr));
#ifndef QT_NO_TOOLTIP
        act_insert->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>insert new line of data into certain location</p><p><br/></p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        act_del->setText(QApplication::translate("MainWindow", "del", nullptr));
#ifndef QT_NO_TOOLTIP
        act_del->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>Delete current line of data</p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        act_new_photo->setText(QApplication::translate("MainWindow", "add_photo", nullptr));
#ifndef QT_NO_TOOLTIP
        act_new_photo->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>Add new image</p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        act_del_photo->setText(QApplication::translate("MainWindow", "del_photo", nullptr));
#ifndef QT_NO_TOOLTIP
        act_del_photo->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>Delete current photo</p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        act_save->setText(QApplication::translate("MainWindow", "save", nullptr));
#ifndef QT_NO_TOOLTIP
        act_save->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>Save changes</p><p><br/></p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        act_cancel_change->setText(QApplication::translate("MainWindow", "cancel_change", nullptr));
#ifndef QT_NO_TOOLTIP
        act_cancel_change->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>Cancel changes</p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        act_exit->setText(QApplication::translate("MainWindow", "exit", nullptr));
#ifndef QT_NO_TOOLTIP
        act_exit->setToolTip(QApplication::translate("MainWindow", "<html><head/><body><p>Quit program</p><p><br/></p></body></html>", nullptr));
#endif // QT_NO_TOOLTIP
        group_sort->setTitle(QApplication::translate("MainWindow", "Sort", nullptr));
        groupBox->setTitle(QString());
        label_sort_col_names->setText(QApplication::translate("MainWindow", "Col Name", nullptr));
        label_sort_names->setText(QApplication::translate("MainWindow", "Sort Name", nullptr));
        sort_radio_asc->setText(QApplication::translate("MainWindow", "Asc", nullptr));
        sort_radio_male->setText(QApplication::translate("MainWindow", "Male", nullptr));
        label_sort_sex->setText(QApplication::translate("MainWindow", "Sort Sex", nullptr));
        sort_radio_female->setText(QApplication::translate("MainWindow", "Female", nullptr));
        sort_radio_all->setText(QApplication::translate("MainWindow", "All", nullptr));
        sort_radio_desc->setText(QApplication::translate("MainWindow", "Desc", nullptr));
        group_info->setTitle(QApplication::translate("MainWindow", "Employee Info", nullptr));
        label_info_id->setText(QApplication::translate("MainWindow", "ID", nullptr));
        label_info_memo->setText(QApplication::translate("MainWindow", "Memo", nullptr));
        label_info_name->setText(QApplication::translate("MainWindow", "Name", nullptr));
        label_info_salary->setText(QApplication::translate("MainWindow", "Salary", nullptr));
        label_info_birth_year->setText(QApplication::translate("MainWindow", "Birth Year", nullptr));
        label_info_sex->setText(QApplication::translate("MainWindow", "Sex", nullptr));
        label_info_birth_addr->setText(QApplication::translate("MainWindow", "Birth Addr", nullptr));
        label_info_dept->setText(QApplication::translate("MainWindow", "Dept", nullptr));
        toolBar->setWindowTitle(QApplication::translate("MainWindow", "toolBar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
