import sys

from PyQt5 import QtWidgets, uic
from designs.connect import Ui_Connect
from designs.messanger import Ui_Messanger
from designs.admin import Ui_Admin
from client import Client


class Window:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyle("Fusion")

    def show_connect_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Connect()
        self.ui.setupUi(self.window)
        self.window.show()

        self.ui.btn_connect.clicked.connect(self.connect_to_server)

    def show_messanger_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Messanger()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_admin_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin()
        self.ui.setupUi(self.window)
        self.window.show()

    def connect_to_server(self):
        addr = self.ui.lineEdit_ip.text()
        port = self.ui.lineEdit_port.text()
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()

        client = Client(addr, port, login, password)

        try:
            client.start()
        except KeyboardInterrupt:
            client.stop()


if __name__ == '__main__':
    window = Window()
    window.show_connect_window()
    sys.exit(window.app.exec_())
