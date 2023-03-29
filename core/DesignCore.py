import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QDateTime, QThread

from GUI.Menu import Ui_menu
from GUI.design import Ui_design
from PyQt5.QtWidgets import QMainWindow, QApplication
import core.global_data as gl

class BackendThread(QThread):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    def __init__(self):
        super(BackendThread, self).__init__()
        self.count = 0
    # 处理业务逻辑
    def run(self):
        while True:
            if gl.designCount==1:
                i=[]
                i=gl.layerList[len(gl.layerList)-1]
                if i[1] == 0:
                    print("conv")
                    data="conv"
                elif i[1] == 1:
                    print("pool")
                    data="pool"
                elif i[1] == 2:
                    print("fc")
                    data="fc"
                self.update_date.emit(str(data))
                gl.designCount=0
            time.sleep(1)
class designWindow(Ui_design, Ui_menu):


    def __init__(self):
        super(designWindow, self).__init__()
        self.setupUi(self)

        self.AddConv.clicked.connect(self.openAddConv)

        self.AddPooling.clicked.connect(self.openAddPooling)

        self.AddFully.clicked.connect(self.openAddFCConv)

        self.backButton.clicked.connect(self.openMenu)
        self.backButton.clicked.connect(self.close)

        self.nextToTrain.clicked.connect(self.openTrainWin)
        self.nextToTrain.clicked.connect(self.close)
        #线程
        self.backend = BackendThread()
        # 连接信号
        self.backend.update_date.connect(self.updateForm)
        # self.thread = QThread()
        #
        # self.backend.moveToThread(self.thread)
        # # 开始线程
        #
        # self.thread.started.connect(self.backend.run)

        self.backend.start()


    def updateForm(self,data):
        self.listWidget.addItem(data)

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