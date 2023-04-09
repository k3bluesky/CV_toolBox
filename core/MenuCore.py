import sys
from PyQt5 import QtCore, QtWidgets
from GUI.Menu import Ui_menu
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication

from GUI.design import Ui_design


class MainWindow(QMainWindow,Ui_menu):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.designModel.clicked.connect(self.openDesign)
        self.designModel.clicked.connect(self.close)

        self.classicalModel.clicked.connect(self.openClassic)
        self.classicalModel.clicked.connect(self.close)

        self.importModel.clicked.connect(self.openUD)
        self.importModel.clicked.connect(self.close)

        self.toolboxModel.clicked.connect(self.openTB)
        self.toolboxModel.clicked.connect(self.close)

    def openTB(self):
        import core.datasetToolCore
        self.design = core.datasetToolCore.datasetToolWindow()
        self.design.show()

    def openDesign(self):
        import core.DesignCore
        self.design = core.DesignCore.designWindow()
        self.design.show()
    def openClassic(self):
        import core.ClassicCore
        self.design = core.ClassicCore.classicWindow()
        self.design.show()

    def openUD(self):
        import core.UDCore
        self.design = core.UDCore.UDWindow()
        self.design.show()




