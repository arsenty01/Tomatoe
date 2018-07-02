from main_window import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
import sys
import json


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profiles = {}

        self.get_profiles()
        self.ui.btnSaveProfile.clicked.connect(self.save_settings)
        self.ui.btnStart.clicked.connect(self.start_session)

    def load_profiles(self):
        pass

    def get_profiles(self):
        try:
            with open('profiles.json') as f:
                self.profiles = json.load(f)
        except FileNotFoundError:
            new_profiles = {
                "Default": {
                    'duration': '',
                    'timeout': ''
                }
            }
            with open('profiles.json', 'w') as f:
                json.dump(new_profiles, f)
            with open('profiles.json') as f:
                self.profiles = json.load(f)

        self.ui.cbProfileSettings.clear()
        self.ui.cbProfileMain.clear()
        for key in self.profiles:
            self.ui.cbProfileMain.addItem(key)
            self.ui.cbProfileSettings.addItem(key)

    def save_settings(self):
        duration = self.ui.session_duration.time().toString()
        timeout = self.ui.leTimeout.text()
        name = self.ui.leProfileName.text() or self.ui.cbProfileSettings.currentText()
        self.profiles[name] = {
            'duration': duration,
            'timeout': timeout
        }
        with open('profiles.json', 'w') as f:
            json.dump(self.profiles, f)

        self.get_profiles()
        self.ui.cbProfileSettings.setCurrentText(name)

    def start_session(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Application()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

