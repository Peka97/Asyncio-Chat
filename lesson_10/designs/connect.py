# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Connect(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 242)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 10, 271, 125))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_ip = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ip.setObjectName("label_ip")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_ip)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ip)
        self.label_port = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_port.setObjectName("label_port")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_port)
        self.label_login = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_login.setObjectName("label_login")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_login)
        self.lineEdit_login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_login)
        self.label_password = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        self.btn_connect.setGeometry(QtCore.QRect(120, 200, 93, 28))
        self.btn_connect.setObjectName("btn_connect")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(30, 140, 271, 41))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Подключение к серверу"))
        self.label_ip.setText(_translate("MainWindow", "IP:"))
        self.lineEdit_ip.setText(_translate("MainWindow", "127.0.0.1"))
        self.label_port.setText(_translate("MainWindow", "Порт: "))
        self.lineEdit_port.setText(_translate("MainWindow", "7777"))
        self.label_login.setText(_translate("MainWindow", "Логин:"))
        self.label_password.setText(_translate("MainWindow", "Пароль:"))
        self.btn_connect.setText(_translate("MainWindow", "Подключиться"))
