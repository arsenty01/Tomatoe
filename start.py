from main_window import Ui_MainWindow
from timeout_window import Ui_timeout_window
from PyQt5 import QtWidgets, QtCore
import sys
import json
import time
import _thread


class ModalWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ModalWindow, self).__init__()
        self.ui = Ui_timeout_window()
        self.ui.setupUi(self)


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profiles = {}
        self.session_flag = False
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.get_profiles()
        self.ui.btnSaveProfile.clicked.connect(self.save_settings)
        self.ui.btnStart.clicked.connect(self.action)
        self.ui.btnStop.clicked.connect(self.stop_session)

    def action(self):
        self.ui.btnStart.setEnabled(False)
        #self.ui.cbCurrentProfile.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        _thread.start_new_thread(self.start_session, ())

    def stop_session(self):
        self.session_flag = False
        self.ui.btnStart.setEnabled(True)
        #self.ui.cbCurrentProfile.setEnabled(True)
        self.ui.btnStop.setEnabled(False)

    def get_profiles(self):
        try:
            with open('profiles.json') as f:
                self.profiles = json.load(f)
        except FileNotFoundError:
            new_profiles = {
                "Default": {
                    'duration': '09:00:00',
                    'timeout': '45'
                }
            }
            with open('profiles.json', 'w') as f:
                json.dump(new_profiles, f)
            with open('profiles.json') as f:
                self.profiles = json.load(f)

        self.ui.cbSavedProfiles.clear()
        #self.ui.cbCurrentProfile.clear()
        for key in self.profiles:
            self.ui.cbSavedProfiles.addItem(key)
            #self.ui.cbCurrentProfile.addItem(key)

    def save_settings(self):
        duration = self.ui.teSessionDuration.time().toString()
        timeout = self.ui.teTimeout.text()
        name = self.ui.leProfileName.text()

        print(duration)
        print(timeout)
        print(name)
        self.profiles[name] = {
            'duration': duration,
            'timeout': timeout
        }
        with open('profiles.json', 'w') as f:
            json.dump(self.profiles, f)

        self.get_profiles()
        self.ui.cbSavedProfiles.setCurrentText(name)

    def start_session(self):
        self.session_flag = True
        current_profile = self.ui.cbSavedProfiles.currentText()
        start = QtCore.QTime(0, 0, 0)
        duration_time = QtCore.QTime.fromString(self.profiles[current_profile]['duration'])
        timeout_minutes = self.profiles[current_profile]['timeout']
        timeout_seconds = int(timeout_minutes)*60
        start_date = QtCore.QDateTime.currentSecsSinceEpoch()
        duration_secs = start.secsTo(duration_time)
        finish_time = start_date + duration_secs
        finish_date = QtCore.QDateTime.fromSecsSinceEpoch(finish_time)
        current_date = QtCore.QDateTime.currentDateTime()
        timeout_counter = 0
        while finish_date > current_date:
            if self.session_flag is False:
                break
            time.sleep(1)
            timeout_counter += 1
            current_date = current_date.addSecs(1)
            if timeout_counter == timeout_seconds:
                timeout_counter = 0
                print('notify!')
            else:
                print('everything ok yet', timeout_counter, timeout_seconds)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Application()

    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

