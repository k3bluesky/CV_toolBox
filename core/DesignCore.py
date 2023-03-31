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
                    data="tensorflow.keras.layers.Conv2D({0}, kernel_size={1}, strides={2},padding={3}, activation=\"{4}\")".format(i[2],i[3],i[4],i[5],i[6])

                elif i[1] == 1:
                    print("pool")
                    data="tensorflow.keras.layers.MaxPool2D(pool_size={0},strides={1},padding=\"{2}\")".format(i[2],i[3],i[4])
                elif i[1] == 2:
                    print("fc")
                    data="tensorflow.keras.layers.Dense({0},activation=\"{1}\")".format(i[2],i[3])
                elif i[1] == 3:
                    print("fc")
                    data = "tensorflow.keras.layers.Flatten()"
                self.update_date.emit(str(data))
                gl.designCount=0
                time.sleep(1)
class designWindow(Ui_design, Ui_menu):


    def __init__(self):
        super(designWindow, self).__init__()
        self.setupUi(self)
        #打开卷积设计器
        self.AddConv.clicked.connect(self.openAddConv)
        #打开池化设计器
        self.AddPooling.clicked.connect(self.openAddPooling)
        #打开全连接设计器
        self.AddFully.clicked.connect(self.openAddFCConv)
        #添加Flatten层
        self.flattenButton.clicked.connect(self.addFlatten)
        #返回按钮控制
        self.backButton.clicked.connect(self.openMenu)
        self.backButton.clicked.connect(self.close)
        self.backButton.clicked.connect(self.clearNet)
        #继续按钮控制
        self.nextToTrain.clicked.connect(self.openTrainWin)
        self.nextToTrain.clicked.connect(self.close)
        self.nextToTrain.clicked.connect(self.getXYZ)
        #多线程控制ListWidget更新
        self.backend = BackendThread()
        self.backend.update_date.connect(self.updateForm)
        self.listWidget.addItem(gl.layerList[0][0])
        self.backend.start()

    def addFlatten(self):
        layer = len(gl.layerList)
        layerClass = 3
        flattenList = [layer, layerClass]
        gl.layerList.append(flattenList)
        gl.designCount = 1
        print(flattenList)
        print(gl.layerList)
    #更新listWidge
    def updateForm(self,data):
        self.listWidget.addItem(data)

    #重置数据
    def clearNet(self):
        gl.layerList=[["网络显示器",""]]

    def getXYZ(self):
        gl.designX,gl.designY,gl.designZ = self.xlineEdit.text(),self.ylineEdit_2.text(),self.zlineEdit_3.text()
        print("get x,y,z"+gl.designX+","+gl.designY+","+gl.designZ)
        self.backend.quit()

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