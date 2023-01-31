import sys
from PyQt5 import QtCore, QtWidgets
from GUI.Menu import Ui_menu
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow,Ui_menu):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.designModel.clicked.connect(self.openDesign)

    def openDesign(self):
        import core.DesignCore as dc
        self.design = dc.designWindow()
        self.design.show()


