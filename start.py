from main_window import Ui_MainWindow
from timeout_window import Ui_timeout_window
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import json
import time
import _thread

saveTimer = 0


class ModalWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_timeout_window()
        self.ui.setupUi(self)
        self.profiles = Application.get_profiles()
        self.setWindowIcon(QtGui.QIcon('tom.png'))
        self.timeoutDuration = Application.qtime_to_seconds(QtCore.QTime.fromString(self.profiles['Default']['timeout']))
        _thread.start_new_thread(self.hello, ())
        self.show()
        self.exec()

    def hello(self):
        global saveTimer
        y = 0
        saveTimer = 0
        zeroPoint = QtCore.QTime.fromString('00:00:00', 'hh:mm:ss')
        while self.timeoutDuration >= y:
            time.sleep(1)
            zeroPoint = zeroPoint.addSecs(1)
            self.ui.ldTimeoutTimer.setText(zeroPoint.toString())
            y += 1
            saveTimer = y
        self.close()


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profiles = self.get_profiles()
        self.session_flag = False
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.ui.sessionTimeEdit.setTime(QtCore.QTime.fromString(self.profiles['Default']['duration'], 'hh:mm:ss'))
        self.ui.worktimeTimeEdit.setTime(QtCore.QTime.fromString(self.profiles['Default']['workTime'], 'hh:mm:ss'))
        self.ui.timeoutTimeEdit.setTime(QtCore.QTime.fromString(self.profiles['Default']['timeout'], 'hh:mm:ss'))
        self.ui.lbTimerSession.setText(self.profiles['Default']['duration'])
        self.ui.lbTimerTimeout.setText(self.profiles['Default']['workTime'])
        self.ui.editButton.clicked.connect(self.edit_settings)
        self.ui.applyButton.clicked.connect(self.save_settings)
        self.ui.btnStart.clicked.connect(self.action)
        self.ui.btnStop.clicked.connect(self.stop_session)

    def action(self):
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        _thread.start_new_thread(self.start_session, ())

    def stop_session(self):
        self.session_flag = False
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)

    def edit_settings(self):
        self.ui.applyButton.setEnabled(True)
        self.ui.sessionTimeEdit.setEnabled(True)
        self.ui.worktimeTimeEdit.setEnabled(True)
        self.ui.timeoutTimeEdit.setEnabled(True)
        self.ui.editButton.setEnabled(False)

    @staticmethod
    def get_profiles():
        try:
            with open('profiles.json') as f:
                profiles = json.load(f)
        except FileNotFoundError:
            new_profiles = {
                "Default": {
                    'duration': '09:00:00',
                    'workTime': '00:45:00',
                    'timeout': '00:15:00'
                }
            }
            with open('profiles.json', 'w') as f:
                json.dump(new_profiles, f)
            with open('profiles.json') as f:
                profiles = json.load(f)
        return profiles

    def save_settings(self):
        duration = self.ui.sessionTimeEdit.time().toString()
        workTime = self.ui.worktimeTimeEdit.time().toString()
        timeout = self.ui.timeoutTimeEdit.time().toString()
        name = 'Default'
        self.profiles[name] = {
            'duration': duration,
            'workTime': workTime,
            'timeout': timeout
        }
        with open('profiles.json', 'w') as f:
            json.dump(self.profiles, f)
        self.ui.lbTimerTimeout.setText(workTime)
        self.ui.lbTimerSession.setText(duration)
        self.ui.applyButton.setEnabled(False)
        self.ui.sessionTimeEdit.setEnabled(False)
        self.ui.worktimeTimeEdit.setEnabled(False)
        self.ui.timeoutTimeEdit.setEnabled(False)
        self.ui.editButton.setEnabled(True)

    @staticmethod
    def qtime_to_seconds(qtime):
        hours = qtime.hour()
        minutes = qtime.minute()
        seconds = qtime.second()
        return hours * 3600 + minutes * 60 + seconds

    def start_session(self):
        global saveTimer
        self.session_flag = True
        current_profile = 'Default'
        zero_point = QtCore.QTime.fromString('00:00:00', 'hh:mm:ss')
        end_point = QtCore.QTime.fromString('23:59:59', 'hh:mm:ss')
        duration_time = QtCore.QTime.fromString(self.profiles[current_profile]['duration'])
        session_counter = zero_point
        workTime_counter = zero_point

        workTime = QtCore.QTime.fromString(self.profiles[current_profile]['workTime'])
        workTime_seconds = self.qtime_to_seconds(workTime)

        timeout_i = 0
        while session_counter < duration_time:
            if self.session_flag is False:
                self.ui.lbTimerSession.setText(self.profiles[current_profile]['duration'])
                self.ui.lbTimerTimeout.setText(self.profiles[current_profile]['workTime'])
                break
            timeout_i += 1
            session_counter = session_counter.addSecs(1)
            workTime_counter = workTime_counter.addSecs(1)
            if timeout_i == workTime_seconds:
                self.childwindow()
                session_counter = session_counter.addSecs(saveTimer)
                workTime_counter = zero_point
                timeout_i = 0
            time.sleep(1)
            self.ui.lbTimerSession.setText(session_counter.toString())
            self.ui.lbTimerTimeout.setText(workTime_counter.toString())

        timeout_e = 0
        self.ui.lbTimerTimeout.setText(self.profiles[current_profile]['workTime'])
        self.ui.lbTimerSession.setStyleSheet('font: bold 20px;color: red;')
        while session_counter != end_point:
            if self.session_flag is False:
                self.ui.lbTimerSession.setText(self.profiles[current_profile]['duration'])
                self.ui.lbTimerTimeout.setText(self.profiles[current_profile]['workTime'])
                break
            timeout_e += 1
            session_counter = session_counter.addSecs(1)
            time.sleep(1)
            self.ui.lbTimerSession.setText(session_counter.toString())
        self.ui.lbTimerSession.setText(self.profiles[current_profile]['duration'])
        self.ui.lbTimerSession.setStyleSheet('font: bold 20px;color: black;')
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)

    def childwindow(self):
        self.window = ModalWindow()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Application()
    application.setWindowIcon(QtGui.QIcon('tom.png'))

    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

