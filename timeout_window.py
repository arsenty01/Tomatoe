# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeout_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_timeout_window(object):
    def setupUi(self, timeout_window):
        timeout_window.setObjectName("timeout_window")
        timeout_window.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(timeout_window.sizePolicy().hasHeightForWidth())
        timeout_window.setSizePolicy(sizePolicy)
        timeout_window.setMinimumSize(QtCore.QSize(300, 200))
        timeout_window.setMaximumSize(QtCore.QSize(300, 200))
        #timeout_window.setModal(True)
        self.makeButton = QtWidgets.QPushButton(timeout_window)
        self.makeButton.setGeometry(QtCore.QRect(90, 150, 121, 31))
        self.makeButton.setStyleSheet("font: 15px")
        self.makeButton.setObjectName("makeButton")
        self.lbTimeout = QtWidgets.QLabel(timeout_window)
        self.lbTimeout.setGeometry(QtCore.QRect(110, 0, 81, 71))
        self.lbTimeout.setStyleSheet("font-size: 20px;")
        self.lbTimeout.setObjectName("lbTimeout")
        self.ldTimeoutTimer = QtWidgets.QLabel(timeout_window)
        self.ldTimeoutTimer.setGeometry(QtCore.QRect(70, 50, 161, 91))
        self.ldTimeoutTimer.setStyleSheet("font-size: 40px;\n"
"")
        self.ldTimeoutTimer.setObjectName("ldTimeoutTimer")

        self.retranslateUi(timeout_window)
        #QtCore.QMetaObject.connectSlotsByName(timeout_window)

    def retranslateUi(self, timeout_window):
        _translate = QtCore.QCoreApplication.translate
        timeout_window.setWindowTitle(_translate("timeout_window", "Dialog"))
        self.makeButton.setText(_translate("timeout_window", "Сделать"))
        self.lbTimeout.setText(_translate("timeout_window", "Перерыв"))
        self.ldTimeoutTimer.setText(_translate("timeout_window", "00:00:00"))

