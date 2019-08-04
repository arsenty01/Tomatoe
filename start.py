from main_window import Ui_MainWindow
from timeout_window import Ui_timeout_window
from datetime import datetime
from PyQt5 import QtWidgets, QtCore
import sys
import time


class MainWindow(QtWidgets.QMainWindow):
    """ main window """

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.child = TimeoutWindow(self)
        self.ui.setupUi(self)
        self.ui.btnStart.clicked.connect(self.session_start)
        self.settings = {"Session": "09:00:00", "Work": "00:00:10", "Rest": "00:00:10"}

    def session_start(self):
        """ start to count """
        self.session_thead = WorkThread(self.settings)
        self.session_thead.show_window.connect(self.start_rest)
        self.session_thead.update_gui.connect(self.update_gui)

        self.session_thead.start()

    def start_rest(self, data=False):
        """ start to rest """
        # TODO figure out about the window
        print(data)
        if data:
            self.child.exec_()
        else:
            self.child.close()

    def update_gui(self, data):
        """ start to count """
        # TODO create updating method
        print(data)


class WorkThread(QtCore.QThread):
    """ session """

    show_window = QtCore.pyqtSignal(bool)
    update_gui = QtCore.pyqtSignal(dict)
    time_format = "%H:%M:%S"

    def __init__(self, settings):
        super().__init__()
        self.settings = settings

    def run(self):

        self.zero_point = datetime.strptime("00:00:00", self.time_format)
        self.end_point = datetime.strptime(self.settings["Session"], self.time_format)
        self.work_period = datetime.strptime(self.settings["Work"], self.time_format)
        self.rest_period = datetime.strptime(self.settings["Rest"], self.time_format)

        self.session_delta = self.end_point - self.zero_point
        self.work_delta = self.work_period - self.zero_point
        self.rest_delta = self.rest_period - self.zero_point

        self.median = self.session_delta.seconds // (self.work_delta.seconds + self.rest_delta.seconds)
        global_timer = 0
        for i in range(self.median):
            for w in range(self.work_delta.seconds):
                self.update_gui.emit({"m": time.strftime(self.time_format, time.gmtime(global_timer)),
                                      "a": time.strftime(self.time_format, time.gmtime(w))})
                global_timer += 1
                time.sleep(1)
            self.show_window.emit(True)
            # TODO how to manage user close the window
            time.sleep(self.rest_delta.seconds)
            self.show_window.emit(False)


class TimeoutWindow(QtWidgets.QDialog):
    """ timeout window """

    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = Ui_timeout_window()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
