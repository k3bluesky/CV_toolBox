import json

from tensorflow.keras import models

from GUI.Menu import Ui_menu
from GUI.trainUD import Ui_trainWD
import os
import sys

from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QFileDialog

import core.global_data as gl

class codeThread(QThread):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    def __init__(self):
        super(codeThread, self).__init__()
        self.count = 0
    # 处理业务逻辑
    def run(self):
        print(gl.designX)
        exec(gl.code)

class Stream(QObject):
    """Redirects console output to text widget."""
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):  # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

class UDWindow(Ui_trainWD,Ui_menu):

    def __init__(self):
        super(UDWindow, self).__init__()
        self.setupUi(self)

        self.useModel.clicked.connect(self.openUseModel)
        self.trainButton.clicked.connect(self.trainModel)
        self.openPathButton.clicked.connect(self.choiseDatasetPath)

        self.openJsonPathButton.clicked.connect(self.choiseJsonModelPath)

    def choiseJsonModelPath(self):
        dir = QFileDialog()
        dir.setNameFilter('json文件(*.json)')
        dir.setFileMode(QFileDialog.ExistingFile)

        dir.setDirectory('..\\')

        if dir.exec_():
            self.jsModelLineEdit.setText(dir.selectedFiles()[0])

    def normalOutputWritten1(self, text):
        """Append text to the QTextEdit."""
        # Maybe QTextEdit.append() works as well, but this is how I do it:
        cursor1 = self.trainScreen.textCursor()
        cursor1.movePosition(QTextCursor.End)
        cursor1.insertText(text)
        self.trainScreen.setTextCursor(cursor1)
        self.trainScreen.ensureCursorVisible()


    def choiseDatasetPath(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.DirectoryOnly)
        dir.setDirectory('..\\')

        if dir.exec_():
            self.datasetLineEdit.setText(dir.selectedFiles()[0])
        gl.datalabel = os.listdir(dir.selectedFiles()[0])
        print(gl.datalabel)

    def getNetList(self):
        with open(self.jsModelLineEdit.text(), 'r') as f:
            model_json = f.read()

        # 构建模型
        model = models.model_from_json(model_json)

        # 编译模型
        model.compile(optimizer='adam', loss='categorical_crossentropy')

        # 创建一个空列表，用于保存层属性
        layers = []

        # 遍历模型的每一层
        for layer in model.layers:
            # 创建一个字典，用于保存该层的属性
            layer_dict = {}

            if layer.__class__.__name__ == 'Conv2D':
                layer_dict['class_name'] = 'Conv2D'
                layer_dict['filters'] = layer.filters
                layer_dict['kernel_size'] = layer.kernel_size
                layer_dict['strides'] = layer.strides
                layer_dict['padding'] = layer.padding
                layer_dict['activation'] = layer.activation.__name__ if hasattr(layer.activation, '__name__') else None
            elif layer.__class__.__name__ == 'Flatten':
                layer_dict['class_name'] = 'Flatten'
            elif layer.__class__.__name__ == 'MaxPooling2D':
                layer_dict['class_name'] = 'MaxPooling2D'
                layer_dict['pool_size'] = layer.pool_size
                layer_dict['strides'] = layer.strides
                layer_dict['padding'] = layer.padding
            elif layer.__class__.__name__ == 'Dense':
                layer_dict['class_name'] = 'Dense'
                layer_dict['units'] = layer.units
                layer_dict['activation'] = layer.activation.__name__ if hasattr(layer.activation, '__name__') else None

            layers.append(layer_dict)

        print(json.dumps(layers))
        new_list = []
        savelayers = json.dumps(layers)
        # 遍历字典列表中的每个字典
        for dict in json.loads(savelayers):
            # 创建一个空字符串
            new_str = ""
            # 将字典中的class_name添加到字符串中
            new_str += dict["class_name"]
            # 如果字典中有filters，将其添加到字符串中，并用逗号分隔
            if "filters" in dict:
                new_str += "," + str(dict["filters"])
            # 如果字典中有kernel_size，将其第一个元素添加到字符串中，并用逗号分隔
            if "kernel_size" in dict:
                new_str += "," + str(dict["kernel_size"][0])
            # 如果字典中有strides，将其第一个元素添加到字符串中，并用逗号分隔
            if "strides" in dict:
                new_str += "," + str(dict["strides"][0])
            # 如果字典中有padding，将其添加到字符串中，并用逗号分隔
            if "padding" in dict:
                new_str += "," + dict["padding"]
            # 如果字典中有activation，将其添加到字符串中，并用逗号分隔
            if "activation" in dict:
                new_str += "," + dict["activation"]
            # 如果字典中有units，将其添加到字符串中，并用逗号分隔
            if "units" in dict:
                new_str += "," + str(dict["units"])
            # 将字符串添加到新列表中
            new_list.append(new_str)

        # 创建一个空的二维数组
        new_array = []

        # 遍历新列表中的每个字符串
        for item in new_list:
            # 用split方法将字符串分割成一个子列表，以逗号为分隔符
            sub_list = item.split(",")
            # 将子列表添加到二维数组中
            new_array.append(sub_list)

        # 遍历二维数组中的每个子列表和它们的索引
        for index, sub_list in enumerate(new_array):
            # 在子列表的第一位插入索引
            sub_list.insert(0, index)
            # 判断子列表的第二位是什么
            if sub_list[1] == "Conv2D":
                # 将其更改为0
                sub_list[1] = 0
            elif sub_list[1] == "Flatten":
                # 将其更改为3
                sub_list[1] = 3
            elif sub_list[1] == "Dense":
                # 将其更改为2
                sub_list[1] = 2
        return new_array

    def readyCode(self):
        epochs = self.epochLineEdit.text()
        batchsize = self.batchLineEdit.text()
        datasetPath = self.datasetLineEdit.text()
        gl.designX = self.xLineEdit.text()
        gl.designY = self.yLineEdit.text()
        gl.designZ = self.zLineEdit.text()

        netList = self.getNetList()
        for i in netList:
            gl.layerList.append(i)
        importReady = [
            "print(\"importing tensorflow\")\n",
            "import tensorflow.keras as keras\n",
            "\n"
            "print(\"tensorflow imported\")\n",
            "epochs={0}\n".format(epochs),
            "\n"
        ]
        importDataset = [
            "train_data = keras.preprocessing.image_dataset_from_directory(\"{0}\",label_mode='categorical',validation_split=0.2,subset=\"training\",seed=123,image_size=({1}, {2}),batch_size={3})\n".format(
                datasetPath, gl.designX, gl.designY, batchsize),
            "val_data = keras.preprocessing.image_dataset_from_directory(\"{0}\", label_mode='categorical',validation_split=0.2,subset=\"validation\",seed=123,image_size=({1}, {2}),batch_size={3})\n".format(
                datasetPath, gl.designX, gl.designY, batchsize),
            "class_names = train_data.class_names\n",
            "print(class_names)\n",
            "class_num=len(class_names)\n"
        ]

        inputShape = "IMG_SHAPE = ({0},{1},{2})\n".format(gl.designX, gl.designY, gl.designZ)
        buildModel = [
            "model = keras.models.Sequential([\n",
            "    keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=IMG_SHAPE),\n"
        ]
        with open("./core/temp/temp.py", 'w', encoding="UTF-8") as file:
            for i in importReady:
                file.write(i)
            for i in importDataset:
                file.write(i)
            file.write(inputShape)
            for i in buildModel:
                file.write(i)
            file.close()
        for i in gl.layerList:
            if i[1] == 0:
                layer = "    keras.layers.Conv2D({0}, kernel_size={1}, strides={2},padding=\"{3}\", activation='{4}'),\n".format(
                    i[2], i[3], i[4], i[5].upper(), i[6])
                with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                    file.write(layer)
                    file.close()
            elif i[1] == 1:
                layer = "    keras.layers.MaxPool2D(pool_size={0},strides={1},padding=\"{2}\"),\n".format(i[2], i[3],
                                                                                                          i[4].upper())
                with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                    file.write(layer)
                    file.close()
            elif i[1] == 2:
                layer = "    keras.layers.Dense({0},activation='{1}'),\n".format(i[3], i[2])
                with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                    file.write(layer)
                    file.close()
            elif i[1] == 3:
                layer = "    keras.layers.Flatten(),\n"
                with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                    file.write(layer)
                    file.close()
        summaryAfit = [

            "    keras.layers.Dense(class_num, activation='softmax')\n",
            "])\n",
            "model.summary()\n",
            "model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])\n",
            "reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor='accuracy', factor=0.5, patience=4, min_lr=0.001,verbose=1)\n",
            "model.fit(train_data, validation_data=val_data,callbacks=[reduce_lr],epochs=epochs)\n",
            "model.save(\"./model.h5\")\n"
        ]
        with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
            for i in summaryAfit:
                file.write(i)
            file.close()
        return "ready"


    def trainModel(self):
        ready = self.readyCode()
        nowPath = os.path.split(os.path.realpath(__file__))[0]
        nowPath = nowPath + '\\temp\\temp.py'
        print(nowPath)

        print(ready)
        with open("./core/temp/temp.py", "r", encoding="UTF-8") as f:
            gl.code = f.read()
            sys.stdout = Stream(textWritten=self.normalOutputWritten1)
            sys.stder = Stream(textWritten=self.normalOutputWritten1)
            # exec(gl.code)
            # os.system('python '+nowPath)
        self.backend = codeThread()
        self.backend.start()
        # loop = QEventLoop()
        # QTimer.singleShot(2000, loop.quit)
        # loop.exec_()
        print("Please wait, programing.....")
        print("If you don't use GPU,It will be a long time.....")


    def openUseModel(self):
        import core.useModelCore
        self.design = core.useModelCore.useModelWindow()
        self.design.show()