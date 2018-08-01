from main_window import Ui_MainWindow
from timeout_window import Ui_timeout_window
from PyQt5 import QtWidgets, QtCore
import sys
import json
import time
import _thread
import threading


class ModalWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.ui = Ui_timeout_window()
        self.ui.setupUi(self)
        self.show()
        self.exec()

    @QtCore.pyqtSlot()
    def on_makeButton_clicked(self):
        pass



class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profiles = {}
        self.session_flag = False
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        self.get_profiles()
        self.ui.leProfileName.setText("Default")
        self.ui.teSessionDuration.setTime(QtCore.QTime.fromString(self.profiles['Default']['duration'], 'hh:mm:ss'))
        self.ui.teTimeout.setTime(QtCore.QTime.fromString(self.profiles['Default']['timeout'], 'h:mm'))
        self.ui.lbTimerSession.setText(self.profiles['Default']['duration'])
        self.ui.lbTimerTimeout.setText(self.profiles['Default']['timeout'])
        self.ui.btnSaveProfile.clicked.connect(self.save_settings)
        self.ui.btnStart.clicked.connect(self.action)
        self.ui.btnStop.clicked.connect(self.stop_session)

    def action(self):
        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)
        _thread.start_new_thread(self.start_session, ())
        #threading.Thread(target=self.start_session)

    def stop_session(self):
        self.session_flag = False
        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)

    def get_profiles(self):
        try:
            with open('profiles.json') as f:
                self.profiles = json.load(f)
        except FileNotFoundError:
            new_profiles = {
                "Default": {
                    'duration': '09:00:00',
                    'timeout': '0:45'
                }
            }
            with open('profiles.json', 'w') as f:
                json.dump(new_profiles, f)
            with open('profiles.json') as f:
                self.profiles = json.load(f)
        self.ui.cbSavedProfiles.clear()
        for key in self.profiles:
            self.ui.cbSavedProfiles.addItem(key)

    def save_settings(self):
        duration = self.ui.teSessionDuration.time().toString()
        timeout = self.ui.teTimeout.text()
        name = self.ui.leProfileName.text()
        self.profiles[name] = {
            'duration': duration,
            'timeout': timeout
        }
        with open('profiles.json', 'w') as f:
            json.dump(self.profiles, f)
        self.get_profiles()
        self.ui.cbSavedProfiles.setCurrentText(name)
        self.ui.lbTimerTimeout.setText(timeout)

    def start_session(self):
        self.session_flag = True
        current_profile = self.ui.cbSavedProfiles.currentText()
        duration_time = QtCore.QTime.fromString(self.profiles[current_profile]['duration'])
        timeout_minutes = self.profiles[current_profile]['timeout'].split(':')[1]
        timeout_seconds = int(timeout_minutes) * 60
        zero_point = QtCore.QTime.fromString('00:00:00', 'hh:mm:ss')
        timeout = 0
        while zero_point != duration_time:
            if self.session_flag is False:
                self.ui.lbTimerSession.setText(self.profiles[current_profile]['duration'])
                break
            timeout += 1
            print(timeout)
            zero_point = zero_point.addSecs(1)
            if timeout == timeout_seconds:
                #threading.Thread(target=self.childwindow).start()
                 _thread.start_new_thread(self.childwindow, ())
            time.sleep(1)
            self.ui.lbTimerSession.setText(zero_point.toString())

    def childwindow(self):
        self.window = ModalWindow()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Application()

    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

