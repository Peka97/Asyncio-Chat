from PyQt5 import QtWidgets, uic
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('lesson_10/designs/connect.ui', self)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
