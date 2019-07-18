import form
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt


class mywindow(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def set_yes(self):
        pass

    def set_soso(self):
        pass

    def set_no(self):
        pass

    def save(self):
        pass

    def select_file(self):
        pass

    def last_query(self):
        pass

    def last_case(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
