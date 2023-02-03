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
        design.resize(863, 630)
        self.centralwidget = QtWidgets.QWidget(design)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 490, 131, 71))
        self.back.setObjectName("back")
        self.nextToTrain = QtWidgets.QPushButton(self.centralwidget)
        self.nextToTrain.setGeometry(QtCore.QRect(720, 490, 121, 81))
        self.nextToTrain.setObjectName("nextToTrain")
        self.AddConv = QtWidgets.QPushButton(self.centralwidget)
        self.AddConv.setGeometry(QtCore.QRect(40, 130, 171, 71))
        self.AddConv.setObjectName("AddConv")
        self.AddPooling = QtWidgets.QPushButton(self.centralwidget)
        self.AddPooling.setGeometry(QtCore.QRect(40, 240, 171, 71))
        self.AddPooling.setObjectName("AddPooling")
        self.AddFully = QtWidgets.QPushButton(self.centralwidget)
        self.AddFully.setGeometry(QtCore.QRect(40, 350, 171, 71))
        self.AddFully.setObjectName("AddFully")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(260, 120, 581, 351))
        self.listView.setObjectName("listView")
        self.next_2 = QtWidgets.QPushButton(self.centralwidget)
        self.next_2.setGeometry(QtCore.QRect(410, 490, 121, 81))
        self.next_2.setObjectName("next_2")
        self.next_3 = QtWidgets.QPushButton(self.centralwidget)
        self.next_3.setGeometry(QtCore.QRect(260, 490, 121, 81))
        self.next_3.setObjectName("next_3")
        self.next_4 = QtWidgets.QPushButton(self.centralwidget)
        self.next_4.setGeometry(QtCore.QRect(560, 490, 121, 81))
        self.next_4.setObjectName("next_4")
        design.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(design)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 23))
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
        self.back.setText(_translate("design", "back"))
        self.nextToTrain.setText(_translate("design", "next"))
        self.AddConv.setText(_translate("design", "Add Convolution"))
        self.AddPooling.setText(_translate("design", "Add Pooling"))
        self.AddFully.setText(_translate("design", "Add Fully Connected"))
        self.next_2.setText(_translate("design", "save"))
        self.next_3.setText(_translate("design", "load"))
        self.next_4.setText(_translate("design", "export"))
        self.menu.setTitle(_translate("design", "菜单"))
