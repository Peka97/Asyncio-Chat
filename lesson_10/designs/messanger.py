# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messanger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messanger(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_messages_field = QtWidgets.QPlainTextEdit(
            self.centralwidget)
        self.plainTextEdit_messages_field.setReadOnly(True)
        self.plainTextEdit_messages_field.setObjectName(
            "plainTextEdit_messages_field")
        self.gridLayout.addWidget(
            self.plainTextEdit_messages_field, 0, 0, 1, 1)
        self.listWidget_contacts = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_contacts.setObjectName("listWidget_contacts")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_contacts.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_contacts.addItem(item)
        self.gridLayout.addWidget(self.listWidget_contacts, 0, 1, 1, 2)
        self.lineEdit_user_text = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit_user_text.sizePolicy().hasHeightForWidth())
        self.lineEdit_user_text.setSizePolicy(sizePolicy)
        self.lineEdit_user_text.setObjectName("lineEdit_user_text")
        self.gridLayout.addWidget(self.lineEdit_user_text, 1, 0, 2, 1)
        self.gridLayout_btns = QtWidgets.QGridLayout()
        self.gridLayout_btns.setObjectName("gridLayout_btns")
        self.btn_send_message = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send_message.setObjectName("btn_send_message")
        self.gridLayout_btns.addWidget(self.btn_send_message, 0, 0, 1, 1)
        self.btn_add_contact = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_contact.setObjectName("btn_add_contact")
        self.gridLayout_btns.addWidget(self.btn_add_contact, 0, 1, 1, 1)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setObjectName("btn_exit")
        self.gridLayout_btns.addWidget(self.btn_exit, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_btns, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мессенджер"))
        self.plainTextEdit_messages_field.setPlainText(_translate("MainWindow", "User_1 00:00 Hi!\n"
                                                                  "User_2 00:01 Hello!\n"
                                                                  ""))
        __sortingEnabled = self.listWidget_contacts.isSortingEnabled()
        self.listWidget_contacts.setSortingEnabled(False)
        item = self.listWidget_contacts.item(0)
        item.setText(_translate("MainWindow", "user_1"))
        item = self.listWidget_contacts.item(1)
        item.setText(_translate("MainWindow", "user_2"))
        self.listWidget_contacts.setSortingEnabled(__sortingEnabled)
        self.btn_send_message.setText(_translate("MainWindow", "Отправить"))
        self.btn_add_contact.setText(
            _translate("MainWindow", "Добавить контакт"))
        self.btn_exit.setText(_translate("MainWindow", "Выход"))
