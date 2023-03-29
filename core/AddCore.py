from GUI.design import Ui_design
from GUI.addConv import Ui_AddCon
from GUI.addPooling import Ui_AddPooling
from GUI.addFullConnect import Ui_addFC
import core.global_data as gl

class addConvWindow(Ui_AddCon, Ui_design):

    def __init__(self):
        super(addConvWindow, self).__init__()
        self.setupUi(self)

        self.continueButton.clicked.connect(self.getConvForm)
        self.continueButton.clicked.connect(self.close)

        self.cancelButton.clicked.connect(self.close)

    def getConvForm(self):
        layer = len(gl.layerList)
        layerClass=0
        filter = self.filterEdit.text()
        kernel_size = self.kernelSizeEdit.text()
        strides = self.stridesEdit.text()
        padding = self.paddingComboBox.currentText()
        activation = self.activationComboBox.currentText()
        convList = [layer,layerClass, filter, kernel_size, strides, padding, activation]
        gl.layerList.append(convList)
        gl.designCount = 1
        print(convList)
        print(gl.layerList)

class addPoolingWindow(Ui_AddPooling, Ui_design):

    def __init__(self):
        super(addPoolingWindow, self).__init__()
        self.setupUi(self)

        self.continueButton.clicked.connect(self.getPoolForm)
        self.continueButton.clicked.connect(self.close)

        self.cancelButton.clicked.connect(self.close)

    def getPoolForm(self):
        layer = len(gl.layerList)
        layerClass = 1
        pool_size = self.poolSizeEdit.text()
        strides = self.stridesEdit.text()
        padding = self.paddingComboBox.currentText()

        poolList = [layer,layerClass,pool_size,strides,padding]
        gl.layerList.append(poolList)
        gl.designCount = 1
        print(poolList)
        print(gl.layerList)

class addFCWindow(Ui_addFC, Ui_design):

    def __init__(self):
        super(addFCWindow, self).__init__()
        self.setupUi(self)

        self.continueButton.clicked.connect(self.getFCForm)
        self.continueButton.clicked.connect(self.close)

        self.cancelButton.clicked.connect(self.close)

    def getFCForm(self):
        layer = len(gl.layerList)
        layerClass = 2
        units = self.unitsEdit.text()
        activation = self.activationComboBox.currentText()

        FCList = [layer,layerClass,units,activation]
        gl.layerList.append(FCList)
        gl.designCount=1
        print(FCList)
        print(gl.layerList)