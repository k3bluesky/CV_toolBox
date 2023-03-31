# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_design(QMainWindow):
    def setupUi(self, design):
        design.setObjectName("design")
        design.resize(863, 639)
        self.centralwidget = QtWidgets.QWidget(design)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(30, 490, 131, 71))
        self.backButton.setObjectName("backButton")
        self.nextToTrain = QtWidgets.QPushButton(self.centralwidget)
        self.nextToTrain.setGeometry(QtCore.QRect(720, 490, 121, 81))
        self.nextToTrain.setObjectName("nextToTrain")
        self.AddConv = QtWidgets.QPushButton(self.centralwidget)
        self.AddConv.setGeometry(QtCore.QRect(40, 110, 171, 71))
        self.AddConv.setObjectName("AddConv")
        self.AddPooling = QtWidgets.QPushButton(self.centralwidget)
        self.AddPooling.setGeometry(QtCore.QRect(40, 200, 171, 71))
        self.AddPooling.setObjectName("AddPooling")
        self.AddFully = QtWidgets.QPushButton(self.centralwidget)
        self.AddFully.setGeometry(QtCore.QRect(40, 380, 171, 71))
        self.AddFully.setObjectName("AddFully")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(410, 490, 121, 81))
        self.saveButton.setObjectName("saveButton")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(260, 490, 121, 81))
        self.loadButton.setObjectName("loadButton")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setGeometry(QtCore.QRect(560, 490, 121, 81))
        self.exportButton.setObjectName("exportButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(240, 90, 591, 381))
        self.listWidget.setObjectName("listWidget")
        self.inputShaplabel = QtWidgets.QLabel(self.centralwidget)
        self.inputShaplabel.setGeometry(QtCore.QRect(260, 40, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.inputShaplabel.setFont(font)
        self.inputShaplabel.setObjectName("inputShaplabel")
        self.xlabel = QtWidgets.QLabel(self.centralwidget)
        self.xlabel.setGeometry(QtCore.QRect(350, 40, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.xlabel.setFont(font)
        self.xlabel.setObjectName("xlabel")
        self.xlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xlineEdit.setGeometry(QtCore.QRect(370, 40, 113, 20))
        self.xlineEdit.setObjectName("xlineEdit")
        self.ylineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ylineEdit_2.setGeometry(QtCore.QRect(510, 40, 113, 20))
        self.ylineEdit_2.setObjectName("ylineEdit_2")
        self.ylabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.ylabel_3.setGeometry(QtCore.QRect(490, 40, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.ylabel_3.setFont(font)
        self.ylabel_3.setObjectName("ylabel_3")
        self.zlineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.zlineEdit_3.setGeometry(QtCore.QRect(650, 40, 113, 20))
        self.zlineEdit_3.setObjectName("zlineEdit_3")
        self.zlabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.zlabel_4.setGeometry(QtCore.QRect(630, 40, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.zlabel_4.setFont(font)
        self.zlabel_4.setObjectName("zlabel_4")
        self.flattenButton = QtWidgets.QPushButton(self.centralwidget)
        self.flattenButton.setGeometry(QtCore.QRect(40, 290, 171, 71))
        self.flattenButton.setObjectName("flattenButton")
        design.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(design)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        design.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(design)
        self.statusbar.setObjectName("statusbar")
        design.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(design)
        QtCore.QMetaObject.connectSlotsByName(design)

    def retranslateUi(self, design):
        _translate = QtCore.QCoreApplication.translate
        design.setWindowTitle(_translate("design", "design"))
        self.backButton.setText(_translate("design", "back"))
        self.nextToTrain.setText(_translate("design", "next"))
        self.AddConv.setText(_translate("design", "Add Convolution"))
        self.AddPooling.setText(_translate("design", "Add Pooling"))
        self.AddFully.setText(_translate("design", "Add Dense"))
        self.saveButton.setText(_translate("design", "save"))
        self.loadButton.setText(_translate("design", "load"))
        self.exportButton.setText(_translate("design", "export"))
        self.inputShaplabel.setText(_translate("design", "input shape："))
        self.xlabel.setText(_translate("design", "x"))
        self.ylabel_3.setText(_translate("design", "y"))
        self.zlabel_4.setText(_translate("design", "z"))
        self.flattenButton.setText(_translate("design", "Add Flatten"))
        self.menu.setTitle(_translate("design", "菜单"))
