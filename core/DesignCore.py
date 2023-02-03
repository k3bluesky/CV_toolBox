import sys
from PyQt5 import QtCore, QtWidgets

from GUI.Menu import Ui_menu
from GUI.design import Ui_design
from PyQt5.QtWidgets import QMainWindow


class designWindow(Ui_design, Ui_menu):

    def __init__(self):
        super(designWindow, self).__init__()
        self.setupUi(self)

        self.AddConv.clicked.connect(self.openAddConv)

        self.AddPooling.clicked.connect(self.openAddConv)

        self.AddFully.clicked.connect(self.openAddConv)

        self.back.clicked.connect(self.openMenu)
        self.back.clicked.connect(self.close)

        self.nextToTrain.clicked.connect(self.openTrainWin)
        self.nextToTrain.clicked.connect(self.close)

    def openAddConv(self):
        import core.AddCore
        self.design = core.AddCore.addConvWindow()
        self.design.show()

    def openAddPooling(self):
        import core.AddCore
        self.design = core.AddCore.addPoolingWindow()
        self.design.show()

    def openAddFCConv(self):
        import core.AddCore
        self.design = core.AddCore.addFCWindow()
        self.design.show()

    def openTrainWin(self):
        import core.TrainWinCore
        self.design = core.TrainWinCore.trainWindow()
        self.design.show()

    def openMenu(self):
        import core.MenuCore
        self.design = core.MenuCore.MainWindow()
        self.design.show()