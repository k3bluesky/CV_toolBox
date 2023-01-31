import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from GUI.Menu import Ui_menu
from core.MenuCore import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())