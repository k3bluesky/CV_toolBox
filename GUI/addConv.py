# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addConv.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddCon(object):
    def setupUi(self, AddCon):
        AddCon.setObjectName("AddCon")
        AddCon.resize(582, 214)
        self.label = QtWidgets.QLabel(AddCon)
        self.label.setGeometry(QtCore.QRect(30, 50, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddCon)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddCon)
        self.label_3.setGeometry(QtCore.QRect(380, 50, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddCon)
        self.label_4.setGeometry(QtCore.QRect(210, 110, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddCon)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(AddCon)
        self.lineEdit.setGeometry(QtCore.QRect(90, 50, 91, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(AddCon)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 50, 91, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(AddCon)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 50, 101, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(AddCon)
        self.comboBox.setGeometry(QtCore.QRect(100, 110, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(AddCon)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 110, 91, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(AddCon)
        self.pushButton.setGeometry(QtCore.QRect(320, 170, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AddCon)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 170, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(AddCon)
        QtCore.QMetaObject.connectSlotsByName(AddCon)

    def retranslateUi(self, AddCon):
        _translate = QtCore.QCoreApplication.translate
        AddCon.setWindowTitle(_translate("AddCon", "Add Convolution"))
        self.label.setText(_translate("AddCon", "filters"))
        self.label_2.setText(_translate("AddCon", "kernel_size"))
        self.label_3.setText(_translate("AddCon", "strides"))
        self.label_4.setText(_translate("AddCon", "activaton"))
        self.label_5.setText(_translate("AddCon", "padding "))
        self.pushButton.setText(_translate("AddCon", "确定"))
        self.pushButton_2.setText(_translate("AddCon", "取消"))