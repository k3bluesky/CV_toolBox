import os
import sys

from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QFileDialog

from GUI.Menu import Ui_menu
from GUI.trainClassic import Ui_trainClassic
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
class classicWindow(Ui_trainClassic, Ui_menu):

    def __init__(self):
        super(classicWindow, self).__init__()
        self.setupUi(self)

        self.useModel.clicked.connect(self.openUseModel)
        self.trainButton.clicked.connect(self.trainModel)
        self.openPathButton.clicked.connect(self.choiseDatasetPath)

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

    def readyCode(self):#大改
        epochs = self.epochLineEdit.text()
        batchsize = self.batchLineEdit.text()
        datasetPath = self.datasetLineEdit.text()
        gl.designX = self.xLineEdit.text()
        gl.designY = self.yLineEdit.text()
        gl.designZ = self.zLineEdit.text()
        modelChoice = self.structurComboBox.currentText()
        '''

        '''
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
        if modelChoice == 'VGG16':
            importPackeg = "from tensorflow.keras.applications import vgg16\n"
            layer = "choose_model = vgg16.VGG16(weights='imagenet',include_top=False,input_shape=({0},{1},{2}))\n".format(gl.designX, gl.designY, gl.designZ)
            with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                file.write(importPackeg)
                file.write(layer)
                file.close()
        elif modelChoice == 'MobileNet':
            importPackeg = "from tensorflow.keras.applications import mobilenet\n"
            layer = "choose_model = mobilenet.MobileNet(include_top=False,input_shape=({0},{1},{2}))\n".format(gl.designX,gl.designY,gl.designZ)
            with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                file.write(importPackeg)
                file.write(layer)
                file.close()
        elif modelChoice == 'ResNet50V2':
            importPackeg = "from tensorflow.keras.applications import resnet_v2\n"
            layer = "choose_model = resnet_v2.ResNet50V2(weights='imagenet',include_top=False,input_shape=({0},{1},{2}))\n".format(gl.designX, gl.designY,gl.designZ)
            with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                file.write(importPackeg)
                file.write(layer)
                file.close()
        elif modelChoice == 'DenseNet121':
            importPackeg = "from tensorflow.keras.applications import densenet\n"
            layer = "choose_model = densenet.DenseNet121(include_top=False,input_shape=({0},{1},{2}))\n".format(gl.designX, gl.designY,gl.designZ)
            with open("./core/temp/temp.py", 'a', encoding="UTF-8") as file:
                file.write(importPackeg)
                file.write(layer)
                file.close()
        summaryAfit = [
            "rmodel = keras.models.Sequential()\n",
            "rmodel.add(keras.layers.Flatten(input_shape=choose_model.output_shape[1:]))\n",
            "rmodel.add(keras.layers.Dense(class_num, activation='softmax'))\n",
            "model = keras.models.Sequential()\n",
            "model.add(choose_model)\n",
            "model.add(rmodel)\n",
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