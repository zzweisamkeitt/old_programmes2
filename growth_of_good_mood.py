import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Smile(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('growth_of_good_mood.ui', self)

        self.setGeometry(200, 200, 470, 450)
        self.setWindowTitle('Рост хорошего настроения')

        self.value = 150
        self.slider.valueChanged[int].connect(self.changesize)

    def changesize(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(0, 0, self.value, self.value)
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(self.value // 5, self.value // 5, self.value // 5, self.value // 5)
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(self.value // 5 * 3, self.value // 5, self.value // 5, self.value // 5)
        qp.setPen(QColor(255, 0, 0))
        qp.drawArc(self.value // 5, self.value // 3, self.value // 2 + self.value // 12, self.value // 2,
                   0 * 16, -180 * 16)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Smile()
    ex.show()
    sys.exit(app.exec())
