from main_window import Ui_MainWindow
from timeout_window import Ui_timeout_window
from datetime import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
import json
import sys
import time


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # buttons
        self.ui.btnStart.clicked.connect(self.dispatcher)
        self.ui.btnStop.clicked.connect(self.stop_everything)
        self.ui.editButton.clicked.connect(self.edit_settings)
        self.ui.applyButton.clicked.connect(self.apply_settings)
        # settings
        with open('profiles.json', 'r') as profiles:
            j_profiles = json.loads(profiles.read())
            if j_profiles:
                self.settings = j_profiles
            else:
                self.settings = {"Session": "09:00:00", "Work": "00:01:00", "Rest": "00:15:00"}
        self.time_format = "%H:%M:%S"
        self.settings_refresh()
        # children
        self.rest_window = RestWindow(rest_seconds=self.rest_delta.seconds)
        self.rest_window.rest_window_closed.connect(self.work)
        self.work_thread = WorkThread(self.work_delta.seconds)
        self.work_thread.update_timers_main.connect(self.work_timer)
        self.work_thread.done.connect(self.show_rest_window)
        self.session_thread = SessionThread()
        self.session_thread.timer.connect(self.session_timer)

    def dispatcher(self):
        """ dispatcher of threads and windows """
        print('dispatcher started')
        self.session_thread.start()
        self.work_thread.start()
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        self.ui.tabsMain.setTabEnabled(1, False)

    def work(self):
        print('work started')
        self.work_thread.start()

    def show_rest_window(self, result):
        """ show rest window """
        if result:
            self.rest_window.exec_()

    def work_timer(self, timer):
        """ update work timer"""
        string = time.strftime(self.time_format, time.gmtime(timer))
        self.ui.lbTimerTimeout.setText(string)

    def session_timer(self, timer):
        """ update main timer"""
        string = time.strftime(self.time_format, time.gmtime(timer))
        self.ui.lbTimerSession.setText(string)

    def stop_everything(self):
        """ closes all threads and stuff """
        self.work_thread.terminate()
        self.session_thread.terminate()
        self.ui.btnStop.setEnabled(False)
        self.ui.btnStart.setEnabled(True)
        self.ui.tabsMain.setTabEnabled(1, True)

    def edit_settings(self):
        """ enable settings edit """
        self.ui.editButton.setEnabled(False)
        self.ui.applyButton.setEnabled(True)
        self.ui.timeoutTimeEdit.setEnabled(True)
        self.ui.sessionTimeEdit.setEnabled(True)
        self.ui.worktimeTimeEdit.setEnabled(True)

    def apply_settings(self):
        """ apply and save settings """
        settings_dict = {
            "Session": self.ui.sessionTimeEdit.time().toString("hh:mm:ss"),
            "Work": self.ui.worktimeTimeEdit.time().toString("hh:mm:ss"),
            "Rest": self.ui.timeoutTimeEdit.time().toString("hh:mm:ss")
        }
        with open('profiles.json', 'w') as profiles:
            json.dump(settings_dict, profiles)
        self.ui.applyButton.setEnabled(False)
        self.ui.editButton.setEnabled(True)
        self.ui.timeoutTimeEdit.setEnabled(False)
        self.ui.sessionTimeEdit.setEnabled(False)
        self.ui.worktimeTimeEdit.setEnabled(False)
        self.settings = settings_dict
        self.settings_refresh()

    def settings_refresh(self):
        """ refresh everything about settings """

        self.ui.lbTimerSession.setText(self.settings["Session"])
        self.ui.lbTimerTimeout.setText(self.settings["Work"])
        self.ui.sessionTimeEdit.setTime(QtCore.QTime.fromString(self.settings["Session"], 'hh:mm:ss'))
        self.ui.worktimeTimeEdit.setTime(QtCore.QTime.fromString(self.settings["Work"], 'hh:mm:ss'))
        self.ui.timeoutTimeEdit.setTime(QtCore.QTime.fromString(self.settings["Rest"], 'hh:mm:ss'))
        self.zero_point = datetime.strptime("00:00:00", self.time_format)
        self.end_point = datetime.strptime(self.settings["Session"], self.time_format)
        self.work_period = datetime.strptime(self.settings["Work"], self.time_format)
        self.rest_period = datetime.strptime(self.settings["Rest"], self.time_format)
        self.session_delta = self.end_point - self.zero_point
        self.work_delta = self.work_period - self.zero_point
        self.rest_delta = self.rest_period - self.zero_point



class RestWindow(QtWidgets.QDialog):
    """ rest window """
    rest_window_closed = QtCore.pyqtSignal(bool)

    def __init__(self, rest_seconds, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = Ui_timeout_window()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.rest_seconds = rest_seconds
        self.time_format = "%H:%M:%S"
        # children
        self.rest_session_thread = RestThread(self.rest_seconds)
        self.rest_session_thread.update_timer.connect(self.update_timer)

    def showEvent(self, a0: QtGui.QShowEvent):
        self.rest_session_thread.start()
        self.rest_session_thread.done.connect(self.close_window)

    def update_timer(self, timer):
        """ update timer of rest window """
        string = time.strftime(self.time_format, time.gmtime(timer))
        self.ui.ldTimeoutTimer.setText(string)

    def close_window(self):
        """ close """
        self.rest_session_thread.terminate()
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        """ event after closing of window """
        self.rest_session_thread.terminate()
        self.rest_window_closed.emit(True)


class WorkThread(QtCore.QThread):
    """ working session thread """

    # signals
    update_timers_main = QtCore.pyqtSignal(int)
    done = QtCore.pyqtSignal(bool)

    def __init__(self, work_seconds):
        super().__init__()
        self.work_seconds = work_seconds

    def run(self):
        """ main thread function """
        print('work thread started')
        for i in range(self.work_seconds):
            self.update_timers_main.emit(i)
            time.sleep(1)
        self.done.emit(True)
        self.quit()


class RestThread(QtCore.QThread):
    """ rest session thread """

    # signals
    update_timer = QtCore.pyqtSignal(int)
    done = QtCore.pyqtSignal(bool)

    def __init__(self, rest_seconds):
        super().__init__()
        self.rest_seconds = rest_seconds

    def run(self):
        """ main thread function """
        print('rest thread started')
        for i in range(self.rest_seconds):
            self.update_timer.emit(i)
            time.sleep(1)
        self.done.emit(True)
        self.quit()


class SessionThread(QtCore.QThread):
    """ session thread"""

    timer = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(86400):
            self.timer.emit(i)
            time.sleep(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    application.show()

    sys.exit(app.exec())
