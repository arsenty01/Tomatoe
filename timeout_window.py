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
        timeout_window.setModal(True)
        self.label = QtWidgets.QLabel(timeout_window)
        self.label.setGeometry(QtCore.QRect(40, 10, 221, 141))
        self.label.setStyleSheet("text-align: center;\n"
"font: 20px bold;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(timeout_window)
        self.pushButton.setGeometry(QtCore.QRect(160, 152, 121, 31))
        self.pushButton.setStyleSheet("font: 15px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(timeout_window)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 152, 121, 31))
        self.pushButton_2.setStyleSheet("font: 15px")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(timeout_window)
        QtCore.QMetaObject.connectSlotsByName(timeout_window)

    def retranslateUi(self, timeout_window):
        _translate = QtCore.QCoreApplication.translate
        timeout_window.setWindowTitle(_translate("timeout_window", "Dialog"))
        self.label.setText(_translate("timeout_window", "Пора сделать перерыв!"))
        self.pushButton.setText(_translate("timeout_window", "Отложить"))
        self.pushButton_2.setText(_translate("timeout_window", "Сделать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    timeout_window = QtWidgets.QDialog()
    ui = Ui_timeout_window()
    ui.setupUi(timeout_window)
    timeout_window.show()
    sys.exit(app.exec_())

