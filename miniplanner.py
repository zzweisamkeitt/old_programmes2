import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import datetime


class MiniPlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('minip.ui', self)

        self.events = []
        self.add_event.clicked.connect(self.show_event)

    def show_event(self):
        t = datetime.datetime(self.calendar.selectedDate().year(),
                              self.calendar.selectedDate().month(),
                              self.calendar.selectedDate().day(),
                              self.time.time().hour(),
                              self.time.time().minute())
        self.events.append(DiaryEvent(t, self.line.text()))
        self.list.clear()
        self.list.addItems([elem.to_str() for elem in self.events])


class DiaryEvent:
    def __init__(self, date_and_time, text):
        self.date_and_time = date_and_time
        self.text = text

    def to_str(self):
        return "{} - {}".format(self.date_and_time, self.text)

    def __str__(self):
        return self.to_str()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniPlanner()
    ex.show()
    sys.exit(app.exec())
