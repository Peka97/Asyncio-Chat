import sys
from threading import Thread
from time import sleep

from PyQt5 import QtWidgets, uic
from designs.connect import Ui_Connect
from designs.messanger import Ui_Messanger
from designs.admin import Ui_Admin
from server import Server


class ServerWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyle("Fusion")

    def show_admin_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin()
        self.ui.setupUi(self.window)
        self.window.show()

    def start_server(self):
        server = Server()

        server_thread = Thread(target=server.start, daemon=True)
        ui_thread = Thread(target=self.show_admin_window, daemon=True)

        server_thread.start()
        ui_thread.start()

        while server_thread.is_alive():
            sleep(1)

        server.stop()


if __name__ == '__main__':
    window = ServerWindow()
    window.start_server()
    sys.exit(window.app.exec_())
