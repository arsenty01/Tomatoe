# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabsMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tabsMain.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.tabsMain.setObjectName("tabsMain")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.btnStart = QtWidgets.QPushButton(self.main)
        self.btnStart.setGeometry(QtCore.QRect(50, 30, 201, 81))
        self.btnStart.setObjectName("btnStart")
        self.cbProfileMain = QtWidgets.QComboBox(self.main)
        self.cbProfileMain.setGeometry(QtCore.QRect(50, 220, 201, 22))
        self.cbProfileMain.setObjectName("cbProfileMain")
        self.lbProfile = QtWidgets.QLabel(self.main)
        self.lbProfile.setGeometry(QtCore.QRect(50, 200, 201, 20))
        self.lbProfile.setObjectName("lbProfile")
        self.btnStop = QtWidgets.QPushButton(self.main)
        self.btnStop.setEnabled(False)
        self.btnStop.setGeometry(QtCore.QRect(50, 130, 201, 23))
        self.btnStop.setObjectName("btnStop")
        self.tabsMain.addTab(self.main, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.lbSessionDuration = QtWidgets.QLabel(self.settings)
        self.lbSessionDuration.setGeometry(QtCore.QRect(10, 80, 151, 16))
        self.lbSessionDuration.setObjectName("lbSessionDuration")
        self.session_duration = QtWidgets.QTimeEdit(self.settings)
        self.session_duration.setGeometry(QtCore.QRect(10, 100, 271, 22))
        self.session_duration.setCalendarPopup(False)
        self.session_duration.setObjectName("session_duration")
        self.lbTimeout = QtWidgets.QLabel(self.settings)
        self.lbTimeout.setGeometry(QtCore.QRect(10, 130, 271, 20))
        self.lbTimeout.setObjectName("lbTimeout")
        self.leTimeout = QtWidgets.QLineEdit(self.settings)
        self.leTimeout.setGeometry(QtCore.QRect(10, 150, 271, 20))
        self.leTimeout.setText("")
        self.leTimeout.setMaxLength(1)
        self.leTimeout.setClearButtonEnabled(False)
        self.leTimeout.setObjectName("leTimeout")
        self.btnSaveProfile = QtWidgets.QPushButton(self.settings)
        self.btnSaveProfile.setGeometry(QtCore.QRect(80, 230, 131, 31))
        self.btnSaveProfile.setObjectName("btnSaveProfile")
        self.lbProfilename = QtWidgets.QLabel(self.settings)
        self.lbProfilename.setGeometry(QtCore.QRect(10, 180, 271, 20))
        self.lbProfilename.setObjectName("lbProfilename")
        self.leProfileName = QtWidgets.QLineEdit(self.settings)
        self.leProfileName.setGeometry(QtCore.QRect(10, 200, 271, 20))
        self.leProfileName.setObjectName("leProfileName")
        self.cbProfileSettings = QtWidgets.QComboBox(self.settings)
        self.cbProfileSettings.setGeometry(QtCore.QRect(10, 40, 271, 22))
        self.cbProfileSettings.setObjectName("cbProfileSettings")
        self.lbPrfile = QtWidgets.QLabel(self.settings)
        self.lbPrfile.setGeometry(QtCore.QRect(10, 20, 271, 20))
        self.lbPrfile.setObjectName("lbPrfile")
        self.tabsMain.addTab(self.settings, "")
        self.statistic = QtWidgets.QWidget()
        self.statistic.setObjectName("statistic")
        self.lbStatistics = QtWidgets.QLabel(self.statistic)
        self.lbStatistics.setGeometry(QtCore.QRect(20, 130, 261, 20))
        self.lbStatistics.setAlignment(QtCore.Qt.AlignCenter)
        self.lbStatistics.setObjectName("lbStatistics")
        self.tabsMain.addTab(self.statistic, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        self.tabsMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tomatoe"))
        self.btnStart.setText(_translate("MainWindow", "СТАРТ"))
        self.lbProfile.setText(_translate("MainWindow", "Профиль"))
        self.btnStop.setText(_translate("MainWindow", "СТОП"))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.main), _translate("MainWindow", "Основное"))
        self.lbSessionDuration.setText(_translate("MainWindow", "Продолжительность сессии"))
        self.session_duration.setDisplayFormat(_translate("MainWindow", "H:mm:ss"))
        self.lbTimeout.setText(_translate("MainWindow", "Перерыв через (мин)"))
        self.leTimeout.setInputMask(_translate("MainWindow", "9"))
        self.btnSaveProfile.setText(_translate("MainWindow", "Сохранить профиль"))
        self.lbProfilename.setText(_translate("MainWindow", "Имя профиля"))
        self.lbPrfile.setText(_translate("MainWindow", "Профиль"))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.settings), _translate("MainWindow", "Настройки"))
        self.lbStatistics.setText(_translate("MainWindow", "Грядет в версии 2.0"))
        self.tabsMain.setTabText(self.tabsMain.indexOf(self.statistic), _translate("MainWindow", "Статистика"))
        self.action.setText(_translate("MainWindow", "Настройки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

