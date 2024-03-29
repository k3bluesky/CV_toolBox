# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainClassic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_trainClassic(QMainWindow):
    def setupUi(self, trainClassic):
        trainClassic.setObjectName("trainClassic")
        trainClassic.resize(823, 591)
        self.centralwidget = QtWidgets.QWidget(trainClassic)
        self.centralwidget.setObjectName("centralwidget")
        self.trainButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainButton.setGeometry(QtCore.QRect(480, 60, 131, 71))
        self.trainButton.setObjectName("trainButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 71, 21))
        self.label_3.setObjectName("label_3")
        self.epochLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.epochLineEdit.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.epochLineEdit.setObjectName("epochLineEdit")
        self.batchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.batchLineEdit.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.batchLineEdit.setObjectName("batchLineEdit")
        self.datasetLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.datasetLineEdit.setGeometry(QtCore.QRect(130, 120, 251, 20))
        self.datasetLineEdit.setObjectName("datasetLineEdit")
        self.openPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.openPathButton.setGeometry(QtCore.QRect(380, 120, 31, 23))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(9)
        self.openPathButton.setFont(font)
        self.openPathButton.setObjectName("openPathButton")
        self.useModel = QtWidgets.QPushButton(self.centralwidget)
        self.useModel.setGeometry(QtCore.QRect(640, 60, 151, 71))
        self.useModel.setObjectName("useModel")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 40, 71, 21))
        self.label_4.setObjectName("label_4")
        self.structurComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.structurComboBox.setGeometry(QtCore.QRect(340, 40, 111, 22))
        self.structurComboBox.setObjectName("structurComboBox")
        self.trainScreen = QtWidgets.QTextEdit(self.centralwidget)
        self.trainScreen.setGeometry(QtCore.QRect(30, 160, 771, 391))
        self.trainScreen.setObjectName("trainScreen")
        self.xLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xLineEdit.setGeometry(QtCore.QRect(270, 80, 41, 24))
        self.xLineEdit.setObjectName("xLineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 80, 16, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 80, 16, 18))
        self.label_6.setObjectName("label_6")
        self.yLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yLineEdit.setGeometry(QtCore.QRect(340, 80, 41, 24))
        self.yLineEdit.setObjectName("yLineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 80, 16, 18))
        self.label_7.setObjectName("label_7")
        self.zLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.zLineEdit.setGeometry(QtCore.QRect(410, 80, 41, 24))
        self.zLineEdit.setObjectName("zLineEdit")
        trainClassic.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(trainClassic)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 22))
        self.menubar.setObjectName("menubar")
        trainClassic.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(trainClassic)
        self.statusbar.setObjectName("statusbar")
        trainClassic.setStatusBar(self.statusbar)

        self.retranslateUi(trainClassic)
        QtCore.QMetaObject.connectSlotsByName(trainClassic)

    def retranslateUi(self, trainClassic):
        _translate = QtCore.QCoreApplication.translate
        trainClassic.setWindowTitle(_translate("trainClassic", "train"))
        self.trainButton.setText(_translate("trainClassic", "train"))
        self.label.setText(_translate("trainClassic", "epochs"))
        self.label_2.setText(_translate("trainClassic", "batch size"))
        self.label_3.setText(_translate("trainClassic", "dataset"))
        self.openPathButton.setText(_translate("trainClassic", "..."))
        self.useModel.setText(_translate("trainClassic", "use model"))
        self.label_4.setText(_translate("trainClassic", "structure"))
        self.label_5.setText(_translate("trainClassic", "x"))
        self.label_6.setText(_translate("trainClassic", "y"))
        self.label_7.setText(_translate("trainClassic", "z"))
        structurList = ["VGG16", "MobileNet","ResNet50V2","DenseNet121"]
        self.structurComboBox.addItems(structurList)
