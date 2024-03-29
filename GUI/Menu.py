# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(576, 302)
        self.centralwidget = QtWidgets.QWidget(menu)
        self.centralwidget.setObjectName("centralwidget")
        self.importModel = QtWidgets.QPushButton(self.centralwidget)
        self.importModel.setGeometry(QtCore.QRect(310, 40, 241, 91))
        self.importModel.setObjectName("importModel")
        self.classicalModel = QtWidgets.QPushButton(self.centralwidget)
        self.classicalModel.setGeometry(QtCore.QRect(40, 140, 241, 91))
        self.classicalModel.setObjectName("classicalModel")
        self.designModel = QtWidgets.QPushButton(self.centralwidget)
        self.designModel.setGeometry(QtCore.QRect(40, 40, 241, 91))
        self.designModel.setObjectName("designModel")
        self.toolboxModel = QtWidgets.QPushButton(self.centralwidget)
        self.toolboxModel.setGeometry(QtCore.QRect(310, 140, 241, 91))
        self.toolboxModel.setObjectName("toolboxModel")
        menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 26))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu)
        self.statusbar.setObjectName("statusbar")
        menu.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(menu)
        self.designModel.clicked.connect(menu.openDesign)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "menu"))
        self.importModel.setText(_translate("menu", "导入模型"))
        self.classicalModel.setText(_translate("menu", "经典框架"))
        self.designModel.setText(_translate("menu", "自行设计"))
        self.toolboxModel.setText(_translate("menu", "数据集工具盒"))
        self.menu_2.setTitle(_translate("menu", "菜单"))
